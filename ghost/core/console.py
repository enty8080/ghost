#!/usr/bin/env python3

#
# MIT License
#
# Copyright (c) 2020 EntySec
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#

import os
import readline

from ghost.core.badges import Badges
from ghost.core.server import Server
from ghost.core.helper import Helper
from ghost.core.ghost import Ghost


class Console:
    def __init__(self):
        self.badges = Badges()
        self.server = Server()
        self.helper = Helper()
        self.ghost = Ghost()

    def banner(self):
        print("""
  ________.__                    __        ,
 /  _____/|  |__   ____  _______/  |_       \\`-,      ,     =-
/   \\  ___|  |  \\ /  _ \\/  ___/\\   __\\  .-._/   \\_____)\\
\\    \\_\\  \\   Y  (  <_> )___ \\  |  |   ("              / =-
 \\______  /___|  /\\____/____  > |__|    '-;   ,_____.-'       =-
        \\/     \\/           \\/            /__.'
""")

        print("Ghost Framework " + self.helper.version)
        print("--------------------")

        print("""
[*] Also explore our last projects:
    * HatSploit (https://github.com/EntySec/HatSploit) - Modular exploitation
    * HatVenom  (https://github.com/EntySec/HatVenom)  - Binary exploitation
    * Shreder   (https://github.com/EntySec/Shreder)   - SSH bruteforce
    * RomBuster (https://github.com/EntySec/RomBuster) - Router hacking
    * CamOver   (https://github.com/EntySec/CamOver)   - Camera hacking
    * CamRaptor (https://github.com/EntySec/CamRaptor) - Camera hacking
[i] Please rate my work by star :)

    Our Twitter: @entysec
    CEO Twitter: @enty8080
""")

    def shell(self):
         readline.parse_and_bind('tab: complete')
         while True:
             try:
                 ui = input('\033[4mghost\033[0m> ').strip(" ")
                 ui = ui.split()

                 if not ui:
                     continue
                 elif ui[0] == "exit":
                     break
                 elif ui[0] == "clear":
                     os.system("clear")
                 elif ui[0] == "help":
                     print("")
                     print("Core Commands")
                     print("=============")
                     print("")
                     print("    Command        Description")
                     print("    -------        -----------")
                     print("    clear          Clear terminal window.")
                     print("    connect        Connect to the specified device.")
                     print("    disconnect     Disconnect specified device.")
                     print("    exit           Exit Ghost Framework.")
                     print("    help           Show available commands.")
                     print("")
                 elif ui[0] == "connect":
                     if len(ui) < 2:
                         print("Usage: connect <address>")
                     else:
                         try:
                             if len(ui[1].split(':')) < 2:
                                 self.server.connect(ui[1], 5555)
                             else:
                                 self.server.connect(ui[1].split(':')[0],  ui[1].split(':')[1])
                         except SystemExit:
                             pass
                 elif ui[0] == "disconnect":
                     if len(ui) < 2:
                         print("Usage: disconnect <address>")
                     else:
                         try:
                             self.ghost.disconnect(ui[1].split(':')[0])
                         except SystemExit:
                             pass
                 else:
                     print(self.badges.E + "Unrecognized command!")
             except (EOFError, KeyboardInterrupt):
                 pass
             except Exception as e:
                 print("An error occurred: " + str(e) + "!")
