#compound intrest calculator
# = is A = P(1+r/n)^n*t
i = 1

def calc():
    P = float(input('What is P'))
    r = float(input('What is r'))
    n = float(input('What is n'))
    t = float(input('What is t'))

    r = r/100
    x = n * t

    A = P * (1 + r/n) ** x
    A = round(A, 2)
    print('Your answer is', A)

calc()

while i == 1:
    ans = str(input('Would you like to go again, type "y" or "n"'))
    if ans == 'y':
        calc()
    else:
        print('done')
