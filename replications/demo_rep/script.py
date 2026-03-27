import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns

# 读取模拟数据
df = pd.read_csv("../../data/simulated_data.csv")

# 数据预览
print("=== 数据预览 ===")
print(df.head())
print("\n=== 描述性统计 ===")
print(df.describe())

# 构建逻辑回归模型
X = df[["age", "bmi", "smoking"]]
y = df["diabetes"]
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
model = LogisticRegression()
model.fit(X_scaled, y)

# 输出模型结果
print("\n=== 逻辑回归模型系数 ===")
print(f"截距: {model.intercept_[0]:.4f}")
for name, coef in zip(X.columns, model.coef_[0]):
    print(f"{name}: {coef:.4f}")

# 生成可视化图表
plt.figure(figsize=(8, 5))
sns.scatterplot(x="bmi", y="diabetes", hue="diabetes", data=df, palette="coolwarm")
plt.title("BMI vs Diabetes Status")
plt.xlabel("BMI")
plt.ylabel("Diabetes (1=Yes, 0=No)")
plt.savefig("plot.png")
plt.close()
print("\n✅ 图表已保存为 plot.png")
