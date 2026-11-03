# AIP 覆盖矩阵摘要（Coverage Summary）

> 3 个免费包 × 200 张 = **600 张互不重复**架构图，全量 traceHash 去重校验通过。

## 覆盖统计

| 指标 | 值 |
|---|---|
| 架构图总数 | 600（3 包 × 200） |
| 覆盖 ATT&CK 技术 | 17 |
| 实现路径 | ~121（每包） |
| 关联 CVE | 17 |
| 去重 | 600/600 唯一 traceHash |
| 新鲜度分布 | A（<30天）约 130 / B（30–90天）约 60 / C（>90天）约 12 |

## 新鲜度分级

每包 200 张图按 CVE 发布日分级，混合「最新漏洞」与「中等新鲜度」，旧漏洞（C 级）严格控制在 100 张以内：

| 分级 | 定义 | 每包数量 |
|---|---|---|
| **A** | CVE 发布 < 30 天 | ~130 |
| **B** | CVE 发布 30–90 天 | ~60 |
| **C** | CVE 发布 > 90 天 | ~12（≤100） |

## ATT&CK 技术清单（17 项）

| 技术 | 战术 | 路径数 |
|---|---|---|
| T1027 | Obfuscated Files or Information（混淆） | 14 |
| T1053 | Scheduled Task/Job（计划任务） | 17 |
| T1055 | Process Injection（进程注入） | 10 |
| T1059 | Command and Scripting Interpreter（命令/脚本） | 17 |
| T1071 | Application Layer Protocol（应用层协议） | 16 |
| T1078 | Valid Accounts（有效账户） | 3 |
| T1091 | Replication Through Removable Media（移动介质） | 1 |
| T1095 | Non-Application Layer Protocol（非应用层协议） | 2 |
| T1110 | Brute Force（暴力破解） | 2 |
| T1190 | Exploit Public-Facing Application（面向公网利用） | 4 |
| T1203 | Exploitation for Client Execution（客户端利用） | 7 |
| T1497 | Virtualization/Sandbox Evasion（沙箱逃逸） | 3 |
| T1542 | Pre-OS Boot（预启动） | 2 |
| T1543 | Create or Modify System Process（系统进程） | 12 |
| T1547 | Boot or Logon Autostart Execution（自启动） | 4 |
| T1562 | Impair Defenses（削弱防御） | 4 |
| T1574 | Hijack Execution Flow（劫持执行流） | 3 |

> 数据版本：ATT&CK v16 / NVD 2026-11-03
