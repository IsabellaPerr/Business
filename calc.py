#The second one
import math

print('Welcome to Isabellas amasing calculator that will tell you the needed decreased debt')
per = float(input('What is the needed percent in percentage fourm, do not include a percentage symbol'))
per = per/100
user_answer = input('Type "d" for needed decreased debt or "i" for needed increased income')

def my_function(x,y):
    deb = float(input('What is the current debt?'))
    inc = float(input('What is the current income?'))
    rat_current = deb/inc
    if deb/inc <= x:
        print('You are already under ',x)
    elif y == 'd':
        needed_deb = x * inc
        print('You need to decrease the debt by $', math.ceil(deb - needed_deb))
    else:
        needed_inc = deb/x
        print('You need to increase the income by $', math.ceil(needed_inc - inc))

my_function(per, user_answer)
