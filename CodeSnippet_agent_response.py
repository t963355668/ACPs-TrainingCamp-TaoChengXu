# -*- coding: utf-8 -*-
"""
这是一个接收端回应 ACPs 消息的工具
可以模拟智能体处理任务后的回包封装
"""

def build_acp_response(agent_id, status_code, content):
    """
    status_code: 用 200 表示成功, 500 表示服务器出错
    """
    response = {
        "header": {
            "from": agent_id,
            "protocol": "ACPs-Lite-v1.0",
            "type": "response"
        },
        "status": {
            "status_code": status_code,
            "description": "Success" if status_code == 200 else "Error"
        },
        "body": {
            "reply": content
        }
    }
    return response

if __name__ == "__main__":
    # 模拟智能体查询时间后的返回
    reply_packet = build_acp_response("Time_Agent_01", 200, "当前时间是：20xx年xx月xx日 xx：xx")
    
    print(f">>> 回包内容为：\n{reply_packet}")
