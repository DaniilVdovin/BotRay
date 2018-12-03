from subprocess import *
from goto import with_goto

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