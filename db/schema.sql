-- Control Plane Meta DB Schema (v0.1)

DROP TABLE IF EXISTS execution_audit_logs;
DROP TABLE IF EXISTS agent_permissions;
DROP TABLE IF EXISTS apqc_data_mappings;
DROP TABLE IF EXISTS external_connectors;

-- 1. 外部系統介面閘道表
CREATE TABLE external_connectors (
    connector_id VARCHAR(64) PRIMARY KEY,
    system_name VARCHAR(100) NOT NULL,
    api_endpoint TEXT NOT NULL,
    auth_type VARCHAR(32) NOT NULL,
    status VARCHAR(20) DEFAULT 'ACTIVE'
);

-- 2. APQC / ISO 流程與實體 DB 表映射 (含 L0-L4 座標標籤)
CREATE TABLE apqc_data_mappings (
    mapping_id VARCHAR(64) PRIMARY KEY,
    apqc_code VARCHAR(32) NOT NULL,
    layer_level VARCHAR(10) DEFAULT 'L2',
    sop_id VARCHAR(64) NOT NULL,
    target_table VARCHAR(100) NOT NULL,
    target_api_action VARCHAR(100) NOT NULL
);

-- 3. Agent 權限與 RACI 控制表
CREATE TABLE agent_permissions (
    permission_id VARCHAR(64) PRIMARY KEY,
    agent_id VARCHAR(64) NOT NULL,
    apqc_code VARCHAR(32) NOT NULL,
    raci_role CHAR(1) NOT NULL,
    max_approval_amount DECIMAL(12,2) DEFAULT 0.00
);

-- 4. 執行與稽核軌跡日誌
CREATE TABLE execution_audit_logs (
    log_id VARCHAR(64) PRIMARY KEY,
    workflow_id VARCHAR(64) NOT NULL,
    agent_id VARCHAR(64) NOT NULL,
    action_performed TEXT NOT NULL,
    human_approved BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
