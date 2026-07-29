# 🏢 通用型虛擬企業範本庫 (Generic Virtual Enterprise Template Repository)

本儲存庫為 **通用型虛擬企業 (Virtual Enterprise / Digital Twin of Organization)** 之 AI 原生骨架範本。採用 **Enterprise-as-Code**、**L0-L4 團隊級層次化賦能** 與 **Database-First 混合架構**，支援將企業之知識、規範、部門資產與自動化工作流模組化裝載。

---

## 📁 全域 Prefix 目錄結構與 L0-L4 座標標註地圖

```plaintext
virtual-enterprise-template/
├── README.md                                      # 📖 通用型虛擬企業模板總覽與說明
├── config.yaml                                    # ⚙️ 頂層通用系統與 Agent 運行配置
├── .agentignore                                   # 🚫 Agent 檢索忽略規則檔
├── 00_Enterprise_Core/                            # 🏢 [全域核心資產] 通用企業骨架 (Global Context)
│   ├── CORE_L3_BOOK_000_Virtual_Enterprise_Book.md# 📖 虛擬企業總體白皮書 (Master Context)
│   ├── CORE_L3_PROFILE_001_Enterprise_Profile.md  # 📄 通用型企業 Profile (Vision, Mission)
│   ├── CORE_L3_TRUTH_002_Master_Org_Chart.json    # 🗂️ 組織圖結構與主管 Agent ID (L3 真相層)
│   ├── CORE_L3_RACI_003_Functional_Matrix.md      # 📋 職能矩陣與 RACI 權責矩陣 (L3 真相層)
│   ├── CORE_L1_FACT_004_Enterprise_Glossary.md    # 📚 全域專業術語庫 / 名詞解釋字典 (L1 文明層)
│   ├── Brand_Identity/                            # 🎨 品牌識別與 Tone & Manner 規範
│   └── Shared_Templates/                          # 📑 全域共用表單與公文範本 (L0 型態層)
├── _Workflow/                                     # 🚀 [全域管線編排] 跨部門自動化 Workflow 劇本
│   ├── Workflows/ (wf_01_onboarding.yaml, wf_04_procurement_approval.yml)
│   ├── Rules/ (iso_27001_guardrails.md, apqc_global_taxonomy.json)
│   └── Triggers/ (event_triggers.json)
├── 01_HR_Human_Resources/                         # [人] 人力資源與組織發展 (APQC 7.0)
│   ├── _workflow/ (HR_L2_WORKFLOW_001_default.yaml)
│   ├── _SOP/ (HR_L2_SOP_001_recruitment_sop.md)
│   ├── Templates/ (HR_L0_TEMPLATE_001_job_description_template.md)
│   ├── Examples/ (HR_L4_FEWSHOT_001_interview_record_example.md)
│   └── Agents/ (HR_L4_EXPERT_001_hr_recruiter.agent.json, prompts/...)
├── 02_RD_Research_Development/                    # [發] 研發與產品創新 (APQC 2.0/3.0)
│   ├── _workflow/ | _SOP/ | Templates/ | Examples/ | Agents/
├── 03_FIN_Finance_Accounting/                     # [財] 財務、會計與資安法規 (APQC 9.0/11.0)
│   ├── _workflow/ | _SOP/ | Templates/ | Examples/ | Agents/
├── 04_PROC_Procurement/                           # [採] 採購與供應鏈管理 (APQC 4.0/5.0)
│   ├── _workflow/ | _SOP/ | Templates/ | Examples/ | Agents/
├── 05_OPS_Operations/                             # [產/運] 營運與服務交付 (APQC 4.0/10.0)
│   ├── _workflow/ | _SOP/ | Templates/ | Examples/ | Agents/
└── 06_MKT_Sales_Marketing/                        # [銷] 行銷與業務拓展 (APQC 3.0/1.0)
    ├── _workflow/ | _SOP/ | Templates/ | Examples/ | Agents/
```

---

## 🆔 L0-L4 語意與座標化 ID (Coordinate Semantic ID) 命名規範

格式為 `[DEPT]_[LAYER]_[TYPE]_[NUM]`：
- **L0 (型態與資料範本)：** `[DEPT]_L0_TEMPLATE_[NUM]` (例如: `HR_L0_TEMPLATE_001`)
- **L1 (產業與文明 Facts)：** `[DEPT]_L1_FACT_[NUM]` (例如: `CORE_L1_FACT_004`)
- **L2 (職能與習慣 SOP/Workflow)：** `[DEPT]_L2_SOP_[NUM]`, `[DEPT]_L2_WORKFLOW_[NUM]` (例如: `HR_L2_SOP_001`)
- **L3 (企業與真相實體)：** `[DEPT]_L3_TRUTH_[NUM]`, `[DEPT]_L3_RACI_[NUM]` (例如: `CORE_L3_TRUTH_002`)
- **L4 (個人與專家手感)：** `[DEPT]_L4_EXPERT_[NUM]`, `[DEPT]_L4_FEWSHOT_[NUM]` (例如: `HR_L4_EXPERT_001`)

> **脈絡堆疊優先級：L4 (個人專家) > L3 (企業真相) > L2 (職能習慣) > L1 (產業文明) > L0 (型態資料)**
