from subprocess import *
from Replase import *
from Memo import *
import transliterate

def Repairdef(name):
    name.replace(" ", "")
    name = transliterate.translit(name, reversed=True)
    return name
if __name__ == '__main__':
   ans = input()
   if ans == 'Привет':
        hi()
   elif ans == "Info" or ans == "Healp" or ans == "Помашь":
       Info()
   elif ans == 'Д К':
       print('Укажи команду')
       ans = input()
       addDef(Repairdef(ans),ans)
   elif ans == 'Пока':
        Poka()
        call(['python','Main.py'])
   
   elif ans == 'Расскажи о себе':
        Rasskazhiosebe()
        call(['python','Main.py'])