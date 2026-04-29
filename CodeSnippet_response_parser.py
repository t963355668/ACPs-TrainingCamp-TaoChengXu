# -*- coding: utf-8 -*-
"""
这是一个发送端解析回复的工具
可以模拟用户收到智能体的回包后，提取出最终的答案
"""

def parse_agent_response(reply_packet):
    # 检查状态码
    status_code = reply_packet.get("status", {}).get("status_code","")
    
    if status_code == 200:
        # 成功，提取回复内容
        reply_text = reply_packet.get("body", {}).get("reply", "无回复内容")
        return True, f"服务器回复：{reply_text}"
    elif status_code == 500:
        # 失败，提示错误
        return False, "服务器发生错误，请稍后再试。"
    else:
        return False, f"未知状态码: {status_code}"

if __name__ == "__main__":
    # 模拟从网络收到的回复包
    sample_response = {
                  "header":{
                      "from":"agent_01",
                      "protocol":"ACPs-Lite-v1.0",
                      "type":"response"},
      
                  "status": {
                      "status_code": 200,
                      "description": "Success"},
                  "body": {"reply": "当前时间是：20xx年xx月xx日 xx:xx"}
    }


    success, result = parse_agent_response(sample_response)
    print(f">>>解析结果为：{result}")
