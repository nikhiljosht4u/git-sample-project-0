#
# calculator.py 
#

# Asks user for 2 operands and 1 operator
# Returns output of this operation

a=float(input("Enter number 1 : "))
o=input("Enter operator : ")
b=float(input("Enter number 2 : "))
if b !=0:
    if o[0] in [ '+','-','*','/','%']:
        if o[0] == '+':
            out = a + b
        elif o[0] == '-':
            out = a - b
        elif o[0] == '*':
            out = a * b
        elif o[0] == '/':
            out = a/b
        elif o[0] =='%':
            out = a//b
        print("Output : ",out)
    else:
        print("Error : Invalid Operator")
else:
    print("Cannot divide by 0")


