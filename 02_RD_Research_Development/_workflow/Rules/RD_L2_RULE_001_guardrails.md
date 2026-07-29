# RD 研發部門控制與架構治理 Guardrails

- **版本：** v0.1
- **適用範圍：** 02_RD 研發部全域 Workflow

1. 架構決策與 ADR：重大架構變更必須撰寫 ADR 並經由 `AGT-RD-001` 審查通過。
2. 靜態掃描門檻：Code Review 之單元測試覆蓋率必須大於 80%，且不得包含 Hardcoded Credentials。
