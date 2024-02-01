# Reverse Shell Shop | REVSHELLSHOP.py
#   Made by @truerubn on github
# 
# UNDER THE GNU GPL 2.0 LICENSE  
import subprocess, socket, yaml, platform
from ruamel.yaml import YAML

# -----------FUNCTS-----------
def clear():
    subprocess.run(DEFAULT_CLEAR_COMMAND, shell=True)
def getClearCommand():
    return 'cls' if 'Windows' in OPERATING_SYSTEM else 'clear'
# -----------FUNCTS-----------

# ----------DEFAULTS----------
OPERATING_SYSTEM = platform.system()
DEFAULT_PORT = 9000
DEFAULT_IP = socket.gethostbyname(socket.gethostname())
DEFAULT_CLEAR_COMMAND = getClearCommand()
# ----------DEFAULTS----------

with open("payloads.yml", 'r') as payload_file:
    yml = YAML()
    SCRIPTS = yml.load(payload_file)

DESIRED_PAYLOAD = None

clear()

print("""
Welcome to the reverse shell shop!

What OS is the user using?

    [1] Windows
    [2] Linux
    [3] MacOS
""")
# ask for the targets Operating system
OPERATING_SYSTEM_INPUT = input("OS?> ")

# This if statment is the basis of the script.
if OPERATING_SYSTEM_INPUT == "1":
    clear()
    print("""
OS: WIN
IP: ??

What IP would you like the target to connect to?
If no input, we will use you IP.
""")
    IP = input("IP?> ")
    if not IP:
        IP = DEFAULT_IP

    clear()
    print(f"""
OS: WIN
IP: {IP}
PORT: ??

What port?
If no input, we will use {DEFAULT_PORT}.
""")
    PORT = input("PORT?> ")
    if not PORT:
        PORT = DEFAULT_PORT

    clear()
    print(f"""
OS: WIN
IP: {IP}
PORT: {PORT}
METHOD: ??

Here is the fun part, method!

Which method would you like to use? 
    [1] Powershell  [7] Javascript
    [2] Python      [8] Groovy
    [3] C/C#        [9] Lua
    [4] PHP         [10] Go
    [5] Java        [11] Dart
    [6] node.js     [12] Crystal (System)
""")
    METHOD = input("METHOD?> ")
    if METHOD == "1":
        clear()
        print(f"""
OS: WIN
IP: {IP}
PORT: {PORT}
METHOD: POWERSHELL1
SCRIPT: ??

Which ps1?""")
        ps1_scripts = SCRIPTS.get("scripts", {}).get("ps1", {})
        for index, script_name in enumerate(ps1_scripts, start=1):
           print(f"    [{index}] {script_name}")

        SCRIPT_INDEX = int(input("PS1?> "))
        selected_script = list(ps1_scripts.keys())[SCRIPT_INDEX - 1]

        clear()
        DESIRED_PAYLOAD = SCRIPTS.get("scripts", {}).get("ps1", {}).get(selected_script, {}).replace("{YOURIP}", f"{IP}").replace("{YOURPORT}", f"{PORT}")
        print(f"""
OS: WIN
IP: {IP}
PORT: {PORT}
METHOD: POWERSHELL1
SCRIPT: {script_name}

Thank you for shopping with us!

Here is your script:
    {DESIRED_PAYLOAD}
""") 
    elif METHOD == "2":
        clear()
        print(f"""
OS: WIN
IP: {IP}
PORT: {PORT}
METHOD: PYTHON3
SCRIPT: ??

Which py?""")
        py_scripts = SCRIPTS.get("scripts", {}).get("python3", {})
        for index, script_name in enumerate(py_scripts, start=1):
           print(f"    [{index}] {script_name}")

        SCRIPT_INDEX = int(input("PYTHON3?> "))
        selected_script = list(py_scripts.keys())[SCRIPT_INDEX - 1]

        clear()
        DESIRED_PAYLOAD = SCRIPTS.get("scripts", {}).get("python3", {}).get(selected_script, {}).replace("{YOURIP}", f"{IP}").replace("{YOURPORT}", f"{PORT}")
        print(f"""
OS: WIN
IP: {IP}
PORT: {PORT}
METHOD: PYTHON3
SCRIPT: {script_name}

Thank you for shopping with us!

Here is your script:
    {DESIRED_PAYLOAD}
""")
    if METHOD == "3":
        clear()
        print(f"""
OS: WIN
IP: {IP}
PORT: {PORT}
METHOD: C/CS
SCRIPT: ??

Which C or C#?""")
        ccs_scripts = SCRIPTS.get("scripts", {}).get("c_cs", {})
        for index, script_name in enumerate(ccs_scripts, start=1):
           print(f"    [{index}] {script_name}")

        SCRIPT_INDEX = int(input("C/C#?> "))
        selected_script = list(ccs_scripts.keys())[SCRIPT_INDEX - 1]

        clear()
        DESIRED_PAYLOAD = SCRIPTS.get("scripts", {}).get("c_cs", {}).get(selected_script, {}).replace("{YOURIP}", f"{IP}").replace("{YOURPORT}", f"{PORT}")
        print(f"""
OS: WIN
IP: {IP}
PORT: {PORT}
METHOD: C/CS
SCRIPT: {script_name}

Thank you for shopping with us!

Here is your script:
    {DESIRED_PAYLOAD}
""")
elif OPERATING_SYSTEM_INPUT == "2":
    clear()
    print("""
OS: LINUX
IP: ??

What IP would you like the target to connect to?
If no input, we will use your IP.
""")
    IP = input("IP?> ")
    if not IP:
        IP = DEFAULT_IP

    clear()
    print(f"""
OS: LINUX
IP: {IP}
PORT: ??

What port?
If no input, we will use 9000.
""")
    PORT = input("PORT?> ")

    clear()
    print(f"""
OS: LINUX
IP: {IP}
PORT: {PORT}
METHOD: ??

Here is the fun part, method!

Which method would you like to use? 
    [1] Bash  [7] Python
    [2] Perl  [8] Ruby
    [3] C     [9] PHP
    [4] Java  [10] Netcat
    [5] Go    [11] Socat
    [6] Node.js
""")
    METHOD = input("METHOD?> ")
    if METHOD == "1":  # Bash
        bash_scripts = SCRIPTS.get("scripts", {}).get("bash", {})
        for index, script_name in enumerate(bash_scripts, start=1):
            print(f"    [{index}] {script_name}")

        SCRIPT_INDEX = int(input("BASH?> "))
        selected_script = list(bash_scripts.keys())[SCRIPT_INDEX - 1]

        clear()
        DESIRED_PAYLOAD = SCRIPTS.get("scripts", {}).get("bash", {}).get(selected_script, {})
        print(f"""
OS: LINUX
IP: {IP}
PORT: {PORT}.
METHOD: BASH
SCRIPT: {DESIRED_PAYLOAD}

Thank you for shopping with us!

Here is your script:
    {DESIRED_PAYLOAD}
""")
    

elif OPERATING_SYSTEM_INPUT == "3":
    clear()
    print("""
OS: MACOS
IP: ??

What IP would you like the target to connect to?
If no input, we will use your IP.
""")
    IP = input("IP?> ")
    if not IP:
        IP = DEFAULT_IP

    clear()
    print(f"""
OS: MACOS
IP: {IP}
PORT: ??

What port?
If no input, we will use 9000.
""")
    PORT = input("PORT?> ")

    clear()
    print(f"""
OS: MACOS
IP: {IP}
PORT: {PORT}
METHOD: ??

Here is the fun part, method!

Which method would you like to use? 
    [1] Bash  [7] Python
    [2] Perl  [8] Ruby
    [3] C     [9] PHP
    [4] Java  [10] Netcat
    [5] Go    [11] Socat
    [6] Node.js
""")
    METHOD = input("METHOD?> ")
    if METHOD == "1":  # Bash
        clear()
        bash_scripts = SCRIPTS.get("scripts", {}).get("bash", {})
        for index, script_name in enumerate(bash_scripts, start=1):
            print(f"    [{index}] {script_name}")

        SCRIPT_INDEX = int(input("BASH?> "))
        selected_script = list(bash_scripts.keys())[SCRIPT_INDEX - 1]

        clear()
        DESIRED_PAYLOAD = SCRIPTS.get("scripts", {}).get("bash", {}).get(selected_script, {})
        print(f"""
OS: MACOS
IP: {IP}
PORT: {PORT}.
METHOD: BASH
SCRIPT: {DESIRED_PAYLOAD}

Thank you for shopping with us!

Here is your script:
    {DESIRED_PAYLOAD}
""")

else:
    print("Invalid selection. Please choose 1, 2, or 3.")
