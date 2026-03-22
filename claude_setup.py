#!/usr/bin/env python3
"""
Claude SDK 安装和使用说明

安装步骤：
1. 确保网络连接正常
2. 安装 Python 3.8 或更高版本
3. 安装 Claude SDK：pip3 install anthropic
4. 设置 ANTHROPIC_API_KEY 环境变量

使用示例：
1. 替换 API_KEY 为你的实际 API 密钥
2. 运行脚本：python3 claude_setup.py
"""

import os
from anthropic import Anthropic

# 替换为你的 API 密钥
API_KEY = "your_anthropic_api_key_here"

def install_claude():
    """安装 Claude SDK"""
    print("安装 Claude SDK...")
    os.system("pip3 install anthropic")
    print("安装完成！")

def set_api_key():
    """设置 API 密钥"""
    print("设置 API 密钥...")
    # 在 macOS/Linux 上设置环境变量
    os.system(f"export ANTHROPIC_API_KEY={API_KEY}")
    # 永久设置（可选）
    print("\n要永久设置 API 密钥，请将以下行添加到 ~/.bashrc 或 ~/.zshrc 文件中：")
    print(f"export ANTHROPIC_API_KEY={API_KEY}")

def test_claude():
    """测试 Claude SDK"""
    print("\n测试 Claude SDK...")
    try:
        client = Anthropic(api_key=API_KEY)
        message = client.messages.create(
            model="claude-3-opus-20240229",
            max_tokens=100,
            messages=[{"role": "user", "content": "你好，Claude！"}]
        )
        print("响应：", message.content[0].text)
        print("测试成功！")
    except Exception as e:
        print(f"测试失败：{e}")
        print("请检查 API 密钥是否正确，以及网络连接是否正常。")

if __name__ == "__main__":
    print("Claude SDK 安装和测试脚本")
    print("=" * 50)
    
    # 检查是否已安装 anthropic
    try:
        import anthropic
        print("Anthropic SDK 已安装，版本：", anthropic.__version__)
    except ImportError:
        install_claude()
    
    # 设置 API 密钥
    set_api_key()
    
    # 测试 Claude
    test_claude()
    
    print("\n使用说明：")
    print("1. 确保已设置正确的 API 密钥")
    print("2. 运行脚本：python3 claude_setup.py")
    print("3. 查看测试结果")
