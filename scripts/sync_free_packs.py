#!/usr/bin/env python3
"""
Sync Entroprism AIP free packs from entroprism.net (public TAXII 2.1 endpoint).

Fetches the public collections list, filters FREE- packs, and downloads any
pack whose bundle is not already in the repository's bundles/ directory.
Rebuilds a STIX 2.1 bundle wrapper around the objects returned by TAXII.
"""
import json
import os
import sys
import urllib.request

BASE = "https://entroprism.net/api/website/taxii2"
BUNDLES_DIR = os.path.join(os.path.dirname(__file__), "..", "bundles")


def get_json(url, timeout=30):
    req = urllib.request.Request(url, headers={"User-Agent": "Entroprism-AIP-sync/1.0"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read().decode("utf-8"))


def bundle_id(lot_id):
    # 与后端一致的 bundle-- 前缀，用 lot_id 稳定生成
    return "bundle--" + lot_id.lower().replace("free-", "aip-")


def main():
    os.makedirs(BUNDLES_DIR, exist_ok=True)

    collections = get_json(f"{BASE}/root/collections")
    ids = [c["id"] for c in collections.get("collections", []) if c.get("id", "").startswith("FREE-")]

    added = []
    for cid in ids:
        out_path = os.path.join(BUNDLES_DIR, f"{cid}.json")
        if os.path.exists(out_path):
            continue
        # 分页拉取 objects（当前免费包单包 <= 226 个对象，一页足够）
        resp = get_json(f"{BASE}/root/collections/{cid}/objects")
        objects = resp.get("objects", [])
        if not objects:
            print(f"  {cid}: no objects, skip", file=sys.stderr)
            continue
        bundle = {
            "type": "bundle",
            "id": bundle_id(cid),
            "spec_version": "2.1",
            "objects": objects,
        }
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(bundle, f, ensure_ascii=False, indent=2)
            f.write("\n")
        added.append(cid)
        print(f"  added {cid} ({len(objects)} objects)")

    print(f"Synced {len(added)} new packs (total FREE packs online: {len(ids)})")
    # 输出供后续步骤判断是否有变更
    if added:
        with open(os.environ.get("GITHUB_OUTPUT", "/dev/null"), "a") as f:
            f.write(f"changed=true\n")
            f.write(f"added_count={len(added)}\n")


if __name__ == "__main__":
    main()
