from subprocess import *
from goto import with_goto
from time import gmtime, strftime   
@with_goto
def hi():
    print('Привет друг.\nКак дела?')
    label .start
    answer = input()
    if answer == 'хорошо'   or  answer == 'нормально'   or  answer == 'сойдет'  or   answer =='я впорядке':
       print('я рад')
       call(['python','Main.py'])
    else:
       print('Что?  еще раз')
       goto .start     
def Poka():
   print('Пока бро')
   answer = input()
   if answer ==')': 
      print('<3')
def Info():
   File = open('HEALP.txt','r')
   print('''\
BotRay - псевдо интелект способный вести осмысленные диалог с пользователем
Список команд: 
''' + File.read())
   File.close()
def Rasskazhiosebe():
   print('Меня зовут Рей, меня можно дополнять разными фенкциями как через код так и через терминал. Если знаешь Python пиши в кодЕсли иначе вызывай команду "Д К" и начинай создавать !')