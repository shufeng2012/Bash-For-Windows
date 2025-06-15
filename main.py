import sys                      # 提供exit函数原型
import functions

print("Bash For Windows Review v0.0.1")
print("Github address:https://github.com/shufeng2012/Bash-For-Windows")
command_list = None
command_out = None
functions.start()
command = input()               # 获取命令
if command == "exit":           # 判断是否退出
    print("Bye!")
    input("Press enter to continue:")
    sys.exit(0)
command_list = functions.command_operate(command)       # 对命令进行处理
command_out = functions.run(command_list)               # 运行命令
print(command_out)

while command != "exit":
    command_list = None
    command_out = None
    functions.start()
    command = input()
    if command == "exit":           # 判断是否退出
        continue
    command_list = functions.command_operate(command)
    command_out = functions.run(command_list)
    print(command_out)

else:           # 判断是否退出
    print("Bye!")
    input("Press enter to continue:")
    sys.exit(0)