import os                       # 基本系统操作
import socket                   # 提供gethostname函数原型
import subprocess               # 提供run函数原型

def start() -> None:
    '''
    每次执行命令后的操作
    '''
    cwd = os.getcwd()           # 当前用户所在目录
    user = os.getlogin()        # 当前用户名
    name = socket.gethostname() # 当前计算机名
    print("\n%s@%s\n%s $ "%(user, name, cwd), end='')            # 输出提示

def command_operate(command: str) -> list:
    '''
    对命令进行分割
    '''
    return command.strip().split()

def run(command: list) -> str:
    '''
    执行命令的函数
    '''
    PATH = ".\\bin\\bin"
    if not command:
        return ""  # 处理空命令

    first_arg = command[0]
    # 判断是否为路径形式
    is_path_cmd = (
        first_arg.startswith(".\\") or
        first_arg.startswith("..") or
        (len(first_arg)>1 and first_arg[1]==":")
    )

    try:
        if is_path_cmd:
            ran = subprocess.run(
                command,
                shell=True,
                text=True,
                capture_output=True
            )
        else:
            # 在 PATH 中查找可执行文件
            cmd_path = os.path.join(PATH, first_arg)
            full_cmd = [cmd_path] + command[1:]
            ran = subprocess.run(
                full_cmd,
                shell=True,
                text=True,
                capture_output=True
            )

        return ran.stdout if ran.returncode == 0 else ran.stderr
    except Exception as e:
        return str(e)