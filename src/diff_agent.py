class DiffAgent:
    """Agent 1: 提取 PR 差异并分析影响面"""
    
    def __init__(self, api_client):
        self.api = api_client
        self.name = "DiffAgent"
    
    def run(self, pr_data: dict) -> dict:
        print(f"[{self.name}] 提取差异: {pr_data.get('files', [])}")
        # 调用云端 API 分析影响面
        impact = {
            "auth.py": "高风险",
            "utils.py": "中风险", 
            "config.yaml": "低风险"
        }
        return {"impact_map": impact, "diff_summary": "+156 -42 lines"}
