from subprocess import *
import os,sys
from goto import with_goto


def remu():
   os.remove("Main.py")
   os.rename('Main_temp.py','Main.py')
   call(['python','Main.py'])
   
@with_goto
def CrateLogic(name):
    print('Что я должен ответить ?')
    answer = input()
    temp = '   print(\''+answer+'\')'
    print('После этого мы продолжим это обсуждать ?')
    answer = input()
    label .chat
    if answer == "да":
       print('Что скажешь дальше ?')
       answerQ = input()
       print('Что я должен ответить ?')
       answer = input()
       temp += '\n   answer = input()\n   if answer ==\''+answerQ+'\': \n      print(\''+answer+'\')'
       print('После этого мы продолжим это обсуждать ?')
       answer = input()
       goto .chat
    File = open('Memo.py','a',encoding='utf-8')
    File.write('\ndef '+name+'():\n' + temp)
    File.close()

def addDef(name,nameR):
    File = open('Main.py','r',encoding='utf-8')
    Temp = File.read()
    File.close()
    File = open('Main_temp.py','tw',encoding='utf-8') 
    CrateLogic(name)
    File.write(Temp + '\n   elif ans == \''+nameR+'\':\n'+ 
               '        ' + name+'()\n        call([\'python\',\'Main.py\'])')
    File.close()
    remu()

    




