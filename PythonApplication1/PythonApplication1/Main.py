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
   elif ans == 'Д К':
       print('Укажи команду')
       ans = input()
       addDef(Repairdef(ans),ans)
   elif ans == 'Пока':
        Poka()
        call(['python','Main.py'])
   elif ans == 'Сашаа':
        Sashaa()
        call(['python','Main.py'])
   elif ans == 'Гарик':
        Garik()
        call(['python','Main.py'])
   elif ans == 'Время':
        Vremja()
        call(['python','Main.py'])