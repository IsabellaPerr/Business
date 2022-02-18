# loan to value calculator
# 1 milli house to 800k loan = 80 loan to value
# house 937 k figure out what 80% is, need to lower the loan ammount

ans = input('Welcome to the loan to value calculator, type "loan" to calculate the loan to value percent, type lower to find the ammount you need \
to lower loan to make it less than 80%')

if ans == 'loan':
    house = float(input('What is the value of the house?'))
    loan = float(input('What is the value of the loan?'))
    loan_to_value = (loan/house) * 100
    print('The loan to value is ', loan_to_value,'%')
else:
    house = int(input('What is the value of the house?'))
    val = 0.8
    loan = house * val
    print('The needed loan value is $', loan)
