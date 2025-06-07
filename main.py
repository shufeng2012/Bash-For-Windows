import functions

print("Bash For Windows")
functions.start()
command = input()
while command != "exit":
    command_list = None
    command_out = None
    functions.start()
    command = input()
    command_list = functions.command_operate(command)
    command_out = functions.run(command_list)
    print(command_out)
else:
    print("Bye!")
    input("Press enter to continue:")