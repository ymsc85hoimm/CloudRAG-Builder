class ReportAgent:
    """Agent 4: 聚合结果生成结构化报告"""
    
    def __init__(self, api_client):
        self.api = api_client
        self.name = "ReportAgent"
    
    def run(self, style_result: dict, security_result: dict) -> dict:
        print(f"[{self.name}] 合并 Style + Security 输出...")
        critical = len([r for r in security_result.get("risks", []) if r.get("level") == "CRITICAL"])
        warnings = len(style_result.get("issues", []))
        return {
            "critical": critical,
            "warnings": warnings,
            "suggestions": 2,
            "report_generated": True
        }
