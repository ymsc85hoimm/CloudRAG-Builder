# CloudCode-Reviewer

基于云端大模型 API 的多 Agent 协作代码审查系统。

## 核心架构

- **DiffAgent**: PR 差异提取与影响面分析
- **StyleAgent**: 代码规范审查（长链推理，10k+ Tokens）
- **SecurityAgent**: 安全漏洞专项扫描
- **ReportAgent**: 结果聚合与结构化报告生成
- **ReviewOrchestrator**: 中央调度器，支持并行处理与失败回流

## 快速开始

```bash
pip install -r requirements.txt
python demo_local.py# CloudRAG-Builder
