# AIP 覆盖矩阵摘要（Coverage Summary）

> 5 个免费包 × 200 张 = **1000 张互不重复**架构图，全量 traceHash 去重校验通过。

## 覆盖统计

| 指标 | 值 |
|---|---|
| 架构图总数 | 1000 |
| 覆盖 ATT&CK 技术 | 25 |
| 实现路径 | 85（每包） |
| 关联 CVE | 7 |
| 去重 | 1000/1000 唯一 traceHash |

## ATT&CK 技术清单（25 项）

| 技术 | 战术 |
|---|---|
| T1190 | Exploit Public-Facing Application |
| T1566 | Phishing |
| T1091 | Replication Through Removable Media |
| T1189 | Drive-by Compromise |
| T1078 | Valid Accounts |
| T1110 | Brute Force |
| T1053 | Scheduled Task/Job |
| T1547 | Boot or Logon Autostart Execution |
| T1546 | Event Triggered Execution |
| T1543 | Create or Modify System Process |
| T1574 | Hijack Execution Flow |
| T1542 | Pre-OS Boot |
| T1055 | Process Injection |
| T1036 | Masquerading |
| T1564 | Hide Artifacts |
| T1027 | Obfuscated Files or Information |
| T1562 | Impair Defenses |
| T1106 | Native API |
| T1497 | Virtualization/Sandbox Evasion |
| T1071 | Application Layer Protocol |
| T1095 | Non-Application Layer Protocol |
| T1090 | Proxy |
| T1568 | Dynamic Resolution |
| T1048 | Exfiltration Over Alternative Protocol |
| T1102 | Web Service |

## 关联 CVE

CVE-2021-21972 · CVE-2020-3992 · CVE-2021-40539 · CVE-2021-22005 · CVE-2020-10189 · CVE-2021-27561 · CVE-2022-22954

---

*完整 1000 张架构图见 `bundles/` 目录（STIX 2.1 bundle）。*
