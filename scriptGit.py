#!/bin/python

import os
import sys

# echo "# flaskSecondApp" >> README.md
# git init
# git add README.md
# git commit -m "first commit"
# git branch -M main
# git remote add origin https://github.com/yabouseada/flaskSecondApp.git
# git push -u origin main
# sudo apt-get install xsel
 

class ScriptGit:
    def __init__(self):
        print('Github lazy repository initializing')
        self.pathName=os.popen('pwd').read()
        self.repositoryName=input("Type the repository name")

    def gitConfig(self):
        
        commandConfig= [
                    f'cd {self.pathName}',
                    f'echo " # {self.repositoryName} " >> README.md',
                    'git init',
                    'git add README.md',
                    'git commit -m "first commit"',
                    'git branch -M main',
                    f'git remote add origin https://github.com/yabouseada/{self.repositoryName}.git',
                    f'git remote add origin https://github.com/yabouseada/{self.repositoryName}.git',
                    'git branch -M main',
                    'git push -u origin main'
                     
        ]
        return(commandConfig)
    
    def main(self):
        commandConfig = self.gitConfig()
        for config in commandConfig:
                os.system(config)
            
        return(True)
        

instancedClass = ScriptGit()
instancedClass.main()


    

    