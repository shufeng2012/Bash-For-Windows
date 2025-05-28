Documentation:
# Bash For Windows
Language: [简体中文](https://github.com/shufeng2012/Bash-For-Windows/README.md) [English](https://github.com/shufeng2012/Bash-For-Windows/README-english.md)

## Preface
Do you ever feel frustrated when using Windows? Perhaps you're accustomed to the Windows interface, or maybe you choose Windows because its ecosystem is stronger than Linux's. However, you might find yourself uncomfortable with commands like `dir` and `del`, longing for the concise Linux-style commands—this is exactly the frustration I've experienced.

That's why I developed this program: **to enable the use of bash commands on Windows!**
> Note: I am an elementary school student with limited technical skills. Some code references AI-generated content, and I appreciate your understanding.

We welcome your support, suggestions for improvements, or direct code contributions. Thank you!

## Known Bugs Due to Technical Limitations
The following issues are currently unresolved:
* Unable to display `Bad command` type error prompts
    * Relevant code snippet:
    ```python
    def run(command: list) -> str:
    '''
    Command execution function
    '''
    PATH = ".\\bin\\bin"
    if not command:
        return ""  # Handle empty commands

    first_arg = command[0]
    # Determine if path-style command
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
            # Search for executable in PATH
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

***Development Ongoing...***