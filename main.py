import readline
import shutil
import os
import subprocess
from .utils import parser, shell_completer 


def main():
    # Uncomment this block to pass the first stage
    built_ins = ['exit', 'type', 'echo', 'pwd', 'cd', 'history']
    home_dir = os.environ.get('HOME')
    readline.set_completer_delims(' \t\n;')
    readline.parse_and_bind('tab: complete')
    # fname_completer = rlcompleter.Completer({}).complete
    readline.set_completer(shell_completer)
    his = []

    while True:
        # Wait for user input
        inp = input("$ ")
        his.append(inp)
        command = inp.split(" ")
        tokens = parser(inp)
        if not tokens:
            continue
        cmd = tokens[0]
        exec_path = shutil.which(cmd)
        match command[0]:
            case "exit":
                break
            case 'echo':
                echo_list = parser(inp)
                print(" ".join(echo_list[1:]))
            case 'type':
                for prog in command[1:]:
                    if prog in built_ins:
                        print(f"{prog} is a shell builtin")
                    elif shutil.which(prog) is not None:
                        path = shutil.which(prog)
                        print(f"{prog} is {path}")
                    else:
                        print(f"{" ".join(command[1:])}: not found")
            case "pwd":
                print(os.getcwd())
            case 'cd':
                path = command[1]
                if os.path.isdir(path):
                    os.chdir(path)
                elif path == '~':
                    os.chdir(home_dir)
                else: print(f"cd: {path}: No such file or directory")
            case 'mkdir':
                name = tokens[1]
                try:
                    os.makedirs(name)
                except FileExistsError:
                    print(f"{name} already exists")
            case "rmdir":
                name = tokens[1]
                try:
                    os.removedirs(name)
                except FileNotFoundError:
                    print(f"{name} file dosen't exists")
                except OSError:
                    confirmation = input(f"{name} is not empty. Delete everything inside? (y/n)\n")
                    if confirmation.lower() == 'y':
                        try: 
                            shutil.rmtree(name)
                        except Exception as e:
                            print("Error: {e}")
                    else: continue
            case 'clear':
                os.system('cls' if os.name == 'nt' else 'clear') #Look for an alternative
            case 'history':
                if len(tokens) == 1:
                    for i in range(len(his)):
                        print(f"{i+1}  {his[i]}")
                else:
                    val = int(tokens[1])
                    for i in range(len(his)-val, len(his)):
                        print(f"{i+1}  {his[i]}")
            case _ if exec_path is not None:
                subprocess.run(tokens)
            case _:
                print(f"{" ".join(command)}: not found")

if __name__ == "__main__":
    main()