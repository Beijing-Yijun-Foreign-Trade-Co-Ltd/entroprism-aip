# Entroprism

> Adversary behavior validation set
> 1,000 non-duplicate adversary-behavior architecture diagrams
> 5 packs × 200 diagrams · STIX 2.1 format
> For defensive detection, security testing, and compliance validation ONLY.

**Published by**: Beijing Yijun Foreign Trade Co., Ltd.

---

## What is this

Entroprism is an adversary-behavior validation set built for **blue teams, SOC analysts, and threat hunters**. Each pack contains 200 non-duplicate architecture diagrams. Every diagram describes a complete adversary-behavior implementation path (a six-stage behavior chain), anchored to public ATT&CK techniques and CVE vulnerabilities.

This repository publishes **5 free packs (1,000 diagrams in total)** for learning, validation, and detection-rule tuning.

## What each diagram contains

| Element | Description |
|---|---|
| **ATT&CK anchoring** | Technique + sub-technique |
| **CVE association** | Public vulnerabilities with CVSS severity and EPSS exploit probability |
| **Six-stage behavior chain** | Initial access → obfuscation → replication → payload → persistence → C2 |
| **Actionable detection points** | Sigma / YARA detection rules (labeled actionable / heuristic) |
| **Reproducible scenarios** | Validation scenarios with event counts |
| **Traceability hash** | Unique traceHash per diagram, fully traceable |

## Coverage

- **25 ATT&CK techniques** / **85 implementation paths** per pack
- Covers initial access, persistence, privilege escalation, defense evasion, command & control, and more
- 200 diagrams per pack, 5 packs = 1,000 diagrams, **all non-duplicate** (verified by full traceHash deduplication)

## Data format

```
bundles/
  FREE-20261101.json   STIX 2.1 bundle (200 diagrams)
  FREE-20261102.json
  FREE-20261103.json
  FREE-20261104.json
  FREE-20261105.json
```

Each bundle is standard STIX 2.1:
- `identity` — publisher
- `attack-pattern` — ATT&CK technique anchor (with MITRE external_id)
- `report` — each architecture diagram (with CVE external_references)

> **Auto-sync**: this repository auto-syncs the latest free packs daily via GitHub Actions from the public TAXII 2.1 endpoint at entroprism.net (see `scripts/sync_free_packs.py`).

## License & notice

- **Defensive use ONLY**: for defensive detection, security testing, and compliance validation. Any illegal or offensive use is prohibited.
- Data is sourced from public threat intelligence (NVD, CISA KEV, MITRE ATT&CK, etc.).
- This repository is the free public edition; the commercial edition (daily limited auction) offers per-order watermarks, subscription TAXII endpoints, and more complete deliveries.
- Copyright © 2026 Beijing Yijun Foreign Trade Co., Ltd.

## Learn more

🌐 Website: **[entroprism.net](https://entroprism.net)**

- Daily 12:00 (UTC+8) limited release of new packs
- Three-tier pricing, per-pack independent countdown
- Paid edition includes per-order watermarks, STIX 2.1 + TAXII 2.1 subscription endpoints, and Sigma/YARA rule sets

---

# Entroprism 无序散射

> 对抗行为验证集
> 1000 张互不重复的对抗行为架构图
> 5 个包 × 200 张 · STIX 2.1 标准格式
> 仅用于防御检测、安全测试与合规验证

**发布方**：Beijing Yijun Foreign Trade Co., Ltd.（北京懿俊外贸有限公司）

---

## 这是什么

Entroprism 无序散射是一套面向 **蓝队 / SOC / 威胁狩猎团队** 的对抗行为验证集。每个包包含 200 张互不重复的架构图，每张图描述一条完整的对抗行为实现路径（六阶段行为链），并锚定到公开的 ATT&CK 技术与 CVE 漏洞。

本仓库公开了 **5 个免费包（共 1000 张架构图）**，供安全从业者学习、验证与调优检测规则。

## 每张架构图包含

| 要素 | 说明 |
|---|---|
| **ATT&CK 锚定** | 粗技术 + 子技术双锚定 |
| **CVE 关联** | 关联公开漏洞（CVSS 严重度、EPSS 利用概率）|
| **六阶段行为链** | 入口 → 混淆 → 复制 → 载荷 → 持久化 → C2 |
| **可落地检测点** | Sigma / YARA 检测规则（标注 actionable / heuristic）|
| **可复现场景** | 验证场景与事件数 |
| **溯源哈希** | 每张图唯一 traceHash，可追溯 |

## 覆盖范围

- **25 个 ATT&CK 技术** / **85 条实现路径**（每包）
- 覆盖初始访问、持久化、权限提升、防御规避、命令控制等战术阶段
- 每包 200 张图，5 包共 1000 张，**互不重复**（traceHash 全量去重校验通过）

## 数据格式

```
bundles/
  FREE-20261101.json   STIX 2.1 bundle（200 张架构图）
  FREE-20261102.json
  FREE-20261103.json
  FREE-20261104.json
  FREE-20261105.json
```

每个 bundle 是标准 STIX 2.1 格式：
- `identity` — 发布方
- `attack-pattern` — ATT&CK 技术锚点（含 MITRE external_id）
- `report` — 每张架构图（含 CVE external_references）

> **自动更新**：本仓库通过 GitHub Actions 每天自动从 entroprism.net 的公开 TAXII 2.1 端点同步最新免费包（见 `scripts/sync_free_packs.py`）。

## 使用许可与声明

- **仅限防御用途**：仅用于防御检测、安全测试、合规验证，禁止任何非法或攻击性用途。
- 数据来源为公开威胁情报（NVD、CISA KEV、MITRE ATT&CK 等）。
- 本仓库为免费公开版；商业版（每日限量拍卖）提供差异化水印、订阅 TAXII 端点与更完整交付。
- 版权 © 2026 Beijing Yijun Foreign Trade Co., Ltd.（北京懿俊外贸有限公司）

## 了解更多

🌐 官网：**[entroprism.net](https://entroprism.net)**

- 每日 12:00（UTC+8）限量发售全新包
- 三档阶梯定价，每包独立计时
- 付费版含按订单差异化水印、STIX 2.1 + TAXII 2.1 订阅端点、Sigma/YARA 规则集
