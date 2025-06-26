import sys                      # 提供exit函数原型
import functions
from colorama import Fore, Back          # 高亮

print(f"{functions.color("Bash For Windows ", Fore.LIGHTWHITE_EX, Back.RED)}{functions.color("v1.0.1", Fore.LIGHTWHITE_EX, Back.BLUE)}")
print(f"Github address:{functions.color("https://github.com/shufeng2012/Bash-For-Windows",Fore.LIGHTCYAN_EX)}")
print(f"{functions.color("Thank you for use this ", Fore.YELLOW)}{functions.color("procedure", Fore.LIGHTBLACK_EX, Back.YELLOW)}{functions.color("!!!", Fore.YELLOW)}")
command_list: list = None
command_out: str = None
functions.start()
command: str = input()               # 获取命令
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