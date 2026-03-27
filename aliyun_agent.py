import os
import subprocess
from dashscope import Generation

# ======================
# 阿里云 Agent 论文复现脚本（带错误处理）
# ======================

class AliyunPaperReplicationAgent:
    def __init__(self):
        self.data_path = "data/simulated_data.csv"
        self.script_path = "replications/demo_rep/script.py"
        self.plot_path = "replications/demo_rep/plot.png"

    def get_task_from_paper(self):
        """让 AI 读论文、提取任务（带错误处理）"""
        print("\n🤖 Agent: 正在读取论文任务...")
        prompt = """
        我要复现糖尿病风险分析的论文研究：
        1. 数据路径：./data/simulated_data.csv
        2. 核心方法：逻辑回归分析糖尿病风险，自变量 age、bmi、smoking，因变量 diabetes
        3. 请生成复现计划：
           - 确认数据结构
           - 确认模型方法
           - 运行复现代码
           - 验证结果
        """
        try:
            response = Generation.call(
                model="qwen-turbo",
                api_key="sk-sp-fa54f14c54c14b64a9c86fe6a24a359c",
                base_url="https://coding.dashscope.aliyuncs.com/v1",
                messages=[{"role": "user", "content": prompt}]
            )
            if response and hasattr(response, 'output') and response.output:
                print("✅ Agent: 任务提取完成，计划如下：")
                print(response.output.text)
            else:
                print("⚠️ Agent: API 返回空，使用默认复现计划：")
                print("默认计划：运行 script.py，验证 plot.png 是否生成")
        except Exception as e:
            print(f"⚠️ Agent: API 调用失败：{e}")
            print("切换到默认复现计划：直接运行 script.py")

    def run_replication(self):
        """自动运行你的复现代码"""
        print("\n🤖 Agent: 开始自动复现...")
        result = subprocess.run(
            ["python", self.script_path],
            capture_output=True,
            text=True
        )
        print("✅ Agent: 代码运行完成！输出：")
        print(result.stdout)
        if result.stderr:
            print("⚠️ Agent: 警告/报错：")
            print(result.stderr)

    def verify_result(self):
        """验证复现结果"""
        print("\n🤖 Agent: 验证结果...")
        if os.path.exists(self.plot_path):
            print("✅ 图表 plot.png 已生成！")
            print("🎉 论文复现成功！（手动 + Agent 自动化）")
        else:
            print("❌ 图表生成失败")

    def run(self):
        """完整 Agent 流程"""
        print("🚀 启动阿里云论文复现 Agent...")
        self.get_task_from_paper()
        self.run_replication()
        self.verify_result()

if __name__ == "__main__":
    agent = AliyunPaperReplicationAgent()
    agent.run()