
#!/bin/python

import os
import sys

class Preparer:

    # Init and config
    def __init__(self):
        print("ENV-preparer CLI started please wait for input requests")
        self.username = input("Type your gitHub username: ")
        self.email = input("Type your gitHub email: ")
   
    def conf(self):
        commandConfig = [   
                            'mkdir ~/Studies', 
                            'mkdir ~/Work',
                            'sudo apt-get update',
                            'sudo apt install snapd',
                            'sudo apt-get install git-all',
                            'sudo apt install gdebi',
                            'wget - O hyper_3.0.2 https://releases.hyper.is/download/deb',
                            'sudo gdebi deb',
                            'sudo snap install --classic code',
                            'sudo snap install discord',
                            'sudo snap install telegram-desktop',
                            'sudo snap install spotify',
                            'sudo apt install nodejs'
        ]
        gitConfig = [ 
                        f'git config --global user.name "{self.username}"',
                        f'git config --global user.email"{self.email}"'
                    ]

        configList = [commandConfig, gitConfig]
        return(configList)
 
    def main(self):
        configList = self.conf()

        for config in configList:
            for command in config:
                os.system(command)
            
        return(True)
        # commandLineArray = self.commandLine()

instancedClass = Preparer()
instancedClass.main()
