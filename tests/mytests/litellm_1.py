from litellm import completion

# 创建 LLM 实例
response = completion(
    model="mistral/mistral-tiny",
    messages=[{"role": "user", "content": "hello"}],
)
# llm = LLM(model="mistral/mistral-tiny")

# 如果有 --drop_params 或者类似的选项，查阅文档看看如何在代码中设置
# llm.some_method_to_drop_params() # 假设的方法名，具体要看实际 API 文档

# 使用 LLM 模型
# response = llm("你的输入文本")
print(response)
