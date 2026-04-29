# -*- coding: utf-8 -*-
"""
这是一个接收端处理 ACPs 消息的工具
可以模拟 ACPs 协议的接收端解析逻辑
"""

def parse_acp_packet(packet):
    # 检查格式是否合格
    if "header" not in packet:
        return False,"错误：数据包缺失 Header "
    if "body" not in packet:
        return False,"错误：数据包缺失 body "
    
    # 检查版本号
    protocol_version = packet["header"].get("protocol")
    if protocol_version != "ACPs-Lite-v1.0":
        return False,f"错误：协议版本不匹配 ({protocol_version})"
      
    # 提取内容
    content = packet["body"].get("text", "")
    user_id = packet["header"].get("from", "Unknown")
    
    # 检查长度
    claimed_length = packet["body"].get("length", 0)
    actual_length = len(content)
    if claimed_length != actual_length:
        print(f">>>注意：长度校验异常 (声明:{claimed_length}, 实际:{actual_length})")

    return True,f"成功解析来自 {user_id} 的消息: {content}"

if __name__ == "__main__":
    # 模拟接收到 ACPs 数据包
    sample_packet = {
        "header": {"from": "User_01", "protocol": "ACPs-Lite-v1.0"},
        "body": {"text": "请帮我查询时间", "length": 7}
    }
    
    success, result = parse_acp_packet(sample_packet)
    print(f">>>解析结果为: {result}")
