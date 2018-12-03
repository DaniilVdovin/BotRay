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
def Sashaa():
   print('Где ?')
   answer = input()
   if answer =='Тут': 
      print('не вижу')
def Garik():
   print('Оооооу')
   answer = input()
   if answer =='Кто это': 
      print('Чуувак')
def Vremja():
