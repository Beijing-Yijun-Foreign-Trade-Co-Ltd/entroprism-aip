# Entroprism

> Adversary behavior validation set
> 600 non-duplicate adversary-behavior architecture diagrams
> 3 packs × 200 diagrams · STIX 2.1 format
> For defensive detection, security testing, and compliance validation ONLY.

**Published by**: Beijing Yijun Foreign Trade Co., Ltd.

---

## What is this

Entroprism is an adversary-behavior validation set built for **blue teams, SOC analysts, and threat hunters**. Each pack contains 200 non-duplicate architecture diagrams. Every diagram describes a complete adversary-behavior implementation path (a five-stage behavior chain), anchored to public ATT&CK techniques and CVE vulnerabilities.

This repository publishes **3 free packs (600 diagrams in total)** for learning, validation, and detection-rule tuning.

## What each diagram contains

| Element | Description |
|---|---|
| **ATT&CK anchoring** | Technique + sub-technique, mapped to the correct platform |
| **CVE association** | Public vulnerabilities with CVSS severity and EPSS exploit probability |
| **Five-stage behavior chain** | Initial access → Execution → Persistence → Evasion → C2 |
| **Freshness grade** | A (<30d), B (30–90d), C (>90d) — every pack mixes A+B and caps C ≤100 |
| **Actionable detection points** | Sigma / YARA detection rules (labeled actionable / heuristic) |
| **Reproducible scenarios** | Validation scenarios with event counts |
| **Traceability hash** | Unique traceHash per diagram, fully traceable |

## Coverage

- **17 ATT&CK techniques** / **~121 implementation paths** per pack
- Covers initial access, execution, persistence, privilege escalation, defense evasion, command & control, and more
- 200 diagrams per pack, 3 packs = 600 diagrams, **all non-duplicate** (verified by full traceHash deduplication)
- Each pack mixes freshness grades: **A** (latest CVEs, <30 days) + **B** (30–90 days), with **C** (older) capped at 100

## Data format

```
bundles/
  FREE-20261103015629.json   STIX 2.1 bundle (200 diagrams)
  FREE-20261103015632.json
  FREE-20261103015635.json
```

Each bundle is standard STIX 2.1:
- `identity` — publisher
- `attack-pattern` — ATT&CK technique anchor (with MITRE external_id)
- `report` — each architecture diagram (with CVE external_references)

> **Auto-sync**: this repository auto-syncs the latest free packs daily via GitHub Actions from the public TAXII 2.1 endpoint at entroprism.net (see `scripts/sync_free_packs.py`).

## License & notice

- **Defensive use ONLY**: for defensive detection, security testing, and compliance validation. Any illegal or offensive use is prohibited.
- Data is sourced from public threat intelligence (NVD, CISA KEV, MITRE ATT&CK, etc.).
- This repository is the free public edition; the commercial edition offers per-order watermarks, subscription TAXII endpoints, API-key based daily access, and more complete deliveries.
- Copyright © 2026 Beijing Yijun Foreign Trade Co., Ltd.

## Learn more

🌐 Website: **[entroprism.net](https://entroprism.net)**

- Daily 12:00 (UTC+8) release of a new pack at a flat price of **HK$399** (7-day sale window)
- Enterprise subscription: **HK$2,999/month** or **HK$29,999/year** with API-key based daily access and customization
- Paid edition includes per-order watermarks, STIX 2.1 + TAXII 2.1 subscription endpoints, and Sigma/YARA rule sets

---

# Entroprism 无序散射

> 对抗行为验证集
> 600 张互不重复的对抗行为架构图
> 3 个包 × 200 张 · STIX 2.1 标准格式
> 仅用于防御检测、安全测试与合规验证

**发布方**：Beijing Yijun Foreign Trade Co., Ltd.（北京懿俊外贸有限公司）

---

## 这是什么

Entroprism 无序散射是一套面向 **蓝队 / SOC / 威胁狩猎团队** 的对抗行为验证集。每个包包含 200 张互不重复的架构图，每张图描述一条完整的对抗行为实现路径（五阶段行为链），并锚定到公开的 ATT&CK 技术与 CVE 漏洞。

本仓库公开了 **3 个免费包（共 600 张架构图）**，供安全从业者学习、验证与调优检测规则。

## 每张架构图包含

| 要素 | 说明 |
|---|---|
| **ATT&CK 锚定** | 粗技术 + 子技术双锚定，按平台正确映射 |
| **CVE 关联** | 关联公开漏洞（CVSS 严重度、EPSS 利用概率）|
| **五阶段行为链** | 入口 → 执行 → 持久化 → 逃逸 → C2 |
| **新鲜度分级** | A（<30 天）/ B（30–90 天）/ C（>90 天），每包混合 A+B 且 C 级 ≤100 张 |
| **可落地检测点** | Sigma / YARA 检测规则（标注 actionable / heuristic）|
| **可复现场景** | 验证场景与事件数 |
| **溯源哈希** | 每张图唯一 traceHash，可追溯 |

## 覆盖范围

- **17 个 ATT&CK 技术** / **约 121 条实现路径**（每包）
- 覆盖初始访问、执行、持久化、权限提升、防御规避、命令控制等战术阶段
- 每包 200 张图，3 包共 600 张，**互不重复**（traceHash 全量去重校验通过）
- 每包混合新鲜度：**A 级**（最新 CVE，<30 天）+ **B 级**（30–90 天），**C 级**（较旧）不超过 100 张

## 数据格式

```
bundles/
  FREE-20261103015629.json   STIX 2.1 bundle（200 张架构图）
  FREE-20261103015632.json
  FREE-20261103015635.json
```

每个 bundle 是标准 STIX 2.1 格式：
- `identity` — 发布方
- `attack-pattern` — ATT&CK 技术锚点（含 MITRE external_id）
- `report` — 每张架构图（含 CVE external_references）

> **自动更新**：本仓库通过 GitHub Actions 每天自动从 entroprism.net 的公开 TAXII 2.1 端点同步最新免费包（见 `scripts/sync_free_packs.py`）。

## 使用许可与声明

- **仅限防御用途**：仅用于防御检测、安全测试、合规验证，禁止任何非法或攻击性用途。
- 数据来源为公开威胁情报（NVD、CISA KEV、MITRE ATT&CK 等）。
- 本仓库为免费公开版；商业版提供按订单差异化水印、订阅 TAXII 端点、API Key 按日期获取与更完整交付。
- 版权 © 2026 Beijing Yijun Foreign Trade Co., Ltd.（北京懿俊外贸有限公司）

## 了解更多

🌐 官网：**[entroprism.net](https://entroprism.net)**

- 每日 12:00（UTC+8）发售全新包，统一售价 **HK$399**（7 天销售期）
- 企业订阅：**HK$2,999/月** 或 **HK$29,999/年**，API Key 按日期获取 + 定制化
- 付费版含按订单差异化水印、STIX 2.1 + TAXII 2.1 订阅端点、Sigma/YARA 规则集
