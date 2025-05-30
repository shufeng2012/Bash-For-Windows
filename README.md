# Bash For Windows
语言：[简体中文](https://github.com/shufeng2012/Bash-For-Windows/blob/main/README.md) [English](https://github.com/shufeng2012/Bash-For-Windows/blob/main/README-english.md)
## 前言
不知大家有没有这样的烦恼：自己习惯Windows的界面，或者是因为Windows的生态强于Linux，从而才选择Windows。但是却不习惯`dir` `del`等指令，想要用Linux那种简洁明了的指令——反正我是有这种烦恼。

因此，我便开发了这样的一个程序：**在Windows下可以使用bash！**
> 说明：本人是一个小学生，技术有限，有部分代码参考AI，敬请谅解。

希望大家能够支持，给出更改建议，或者直接提供代码，谢谢！
## 一些因为技术原因无法修正的bug
以下是一些已知bug
* 无法显示`Bad command`类似的提示
    * 具体问题代码
    ```python
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
        (len(first_arg) > 1 and first_arg[1] == ":")
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
    ```

***持续开发中……***