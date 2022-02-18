print('Welcome to Isabellas amasing debt, income, and ratio to income calculator')
user_answer = input('Type "d" for debt "i" for income and "r" for the debt income ratio')

def debt():
    rat = float(input('What is the ratio?'))
    inc = float(input('What is the income?'))
    deb = rat * inc
    print('The debt is equal to',deb)

def income():
    rat = float(input('What is the ratio?'))
    deb = float(input('What is the debt'))
    inc = deb/rat
    print('The income is equal to',inc)

def ratio():
    deb = float(input('What is the debt?'))
    inc = float(input('What is the income?'))
    rat = deb/inc
    print('The debt to income ratio is equal to',rat)

if user_answer == 'd':
    debt()
elif user_anser == 'i':
    income()
else:
    ratio()
