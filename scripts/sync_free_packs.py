#!/usr/bin/env python3
"""
Sync Entroprism AIP free packs from entroprism.net (public TAXII 2.1 endpoint).

Fetches the public collections list, filters FREE- packs, and keeps the 3 most
recent packs (600 diagrams) in the repository's bundles/ directory — older packs
are removed so the public repository always reflects the latest 3 free packs.
Rebuilds a STIX 2.1 bundle wrapper around the objects returned by TAXII.
"""
import json
import os
import sys
import urllib.request

BASE = "https://entroprism.net/api/website/taxii2"
BUNDLES_DIR = os.path.join(os.path.dirname(__file__), "..", "bundles")
KEEP = 3  # 公开 3 个最新免费包 = 600 张图


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
    # 只保留最新的 KEEP 个（lot_id 后缀是时间戳，倒序即最新在前）
    ids = sorted(ids, reverse=True)[:KEEP]

    added = []
    for cid in ids:
        out_path = os.path.join(BUNDLES_DIR, f"{cid}.json")
        if os.path.exists(out_path):
            continue
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

    # 删除不在最新 KEEP 个里的旧 bundle
    keep_set = set(ids)
    removed = []
    for fn in os.listdir(BUNDLES_DIR):
        if not fn.endswith(".json"):
            continue
        cid = fn[:-5]
        if cid not in keep_set:
            os.remove(os.path.join(BUNDLES_DIR, fn))
            removed.append(cid)
    if removed:
        print(f"  removed old packs: {', '.join(removed)}")

    print(f"Synced {len(added)} new packs (kept {len(ids)} latest FREE packs)")
    if added or removed:
        with open(os.environ.get("GITHUB_OUTPUT", "/dev/null"), "a") as f:
            f.write("changed=true\n")
            f.write(f"added_count={len(added)}\n")


if __name__ == "__main__":
    main()
