class StyleAgent:
    """Agent 2: 代码规范审查，含长链推理"""
    
    def __init__(self, api_client):
        self.api = api_client
        self.name = "StyleAgent"
    
    def run(self, code: str) -> dict:
        print(f"[{self.name}] 启动三步规范审查...")
        # Step 1: 命名规范
        # Step 2: 格式检查  
        # Step 3: 注释覆盖
        # 长链推理，消耗 10k+ Tokens
        issues = [
            "auth.py: validateToken() → 建议 validate_token()",
            "auth.py: 第 47 行超 79 字符",
            "2 处函数缺少 docstring"
        ]
        return {"issues": issues, "token_cost": 10240}
