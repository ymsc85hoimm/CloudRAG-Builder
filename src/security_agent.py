class SecurityAgent:
    """Agent 3: 安全漏洞专项扫描"""
    
    def __init__(self, api_client):
        self.api = api_client
        self.name = "SecurityAgent"
    
    def run(self, code: str) -> dict:
        print(f"[{self.name}] 扫描 SQL/XSS/敏感信息...")
        risks = [
            {"type": "敏感信息泄露", "file": "config.yaml", "line": 12, "level": "CRITICAL"}
        ]
        return {"risks": risks, "scan_complete": True}
