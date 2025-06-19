# 简单问候程序
def greet_user():
    """问候用户并显示当前时间"""
    import datetime
    
    # 获取当前时间
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # 获取用户输入
    name = input("你好！请问你叫什么名字？ ")
    
    # 检查输入是否为空
    if not name.strip():
        name = "朋友"
    
    # 生成个性化问候
    greeting = f"\n{current_time}\n你好，{name}！欢迎使用Python。\n"
    
    # 打印问候语
    print(greeting)
    print("=" * 40)
    print("这是一个简单的Python程序演示：")
    print("- 用户输入处理")
    print("- 字符串格式化")
    print("- 日期时间操作")
    print("- 函数定义与调用")
    print("=" * 40)

# 调用函数
if __name__ == "__main__":
    greet_user()
    
    # 额外功能：计算两个数字的和
    print("\n让我们做个小计算：")
    try:
        num1 = float(input("请输入第一个数字: "))
        num2 = float(input("请输入第二个数字: "))
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")
    except ValueError:
        print("哦！你输入的不是有效数字。")
    
    print("\n程序结束，感谢使用！")