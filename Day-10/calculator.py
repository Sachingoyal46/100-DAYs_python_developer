#calculator


def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
def mul(n1,n2):
    return n1*n2
def div(n1,n2):
    return n1/n2

# create dictornary

operations ={
    "+":add,
    "-":sub,
    "*":mul,
    "/":div
}

num1=int(input("enter the first number"))



for i in operations:
    print(i)


should_conti=True

while should_conti:

    operation_pick= input("pick out the operation symbol respectiviley")
    num2=int(input("enter the second number"))

    operation_symbol = operations[operation_pick]

    answer=operation_symbol(num1,num2)
    print(f"{num1} {operation_pick} {num2} ={answer}")

    if input("y for yes and n for no")=="y":
        num1=answer
    else:
        should_conti= False    





