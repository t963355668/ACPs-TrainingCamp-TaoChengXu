# ACPs-TrainingCamp-TaoChengXu

## 项目简介
本项目用于存放 ACPs 智能体互联网实训营的入门作业及后续学习笔记。

本项目中CodeSnippet代码完整实现了协议生命周期的闭环：**请求封包 -> 接收解析 -> 响应封包 -> 回复解析**。

## 项目结构
项目由四个核心模块组成，模拟了完整的通信链路：

1. **`CodeSnippet_message_handler.py`**: [发送端] 将用户输入封装为 ACPs 规范的请求包。
2. **`CodeSnippet_message_parser.py`**: [接收端] 模拟智能体验证请求包的合法性与数据完整性。
3. **`CodeSnippet_agent_response_builder.py`**: [接收端] 模拟智能体处理任务后，生成带有状态码的响应包。
4. **`CodeSnippet_response_parser.py`**: [发送端] 将复杂的系统回包解析为用户直观可读的文字。
