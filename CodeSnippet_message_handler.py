# -*- coding: utf-8 -*-
"""
这是一个简单的智能体消息处理工具
可以模拟简单的 ACPs 协议中的基础数据格式化
"""

def build_acp_request(user_id, content):

    packet = {
        "header": {                        
            "from": user_id,
            "protocol": "ACPs-Lite-v1.0"
        },
        "body": {
            "text": content,
            "length": len(content)
        }
    }
    return packet

def main():
    # 模拟发送指令
    message = "请帮我查询时间。"
    
    print(f">>>原始输入为: \n{message} ")

    acp_request = build_acp_request("User_01", message)
    
    print("\n >>>封装后的智能体消息为：")
    for key, value in acp_request.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()
