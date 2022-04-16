"""
Abduljabbar Said
Calculator
"""
def main():
    tt = input("type an expression ")
    zz = input(" +, -, *, or / the variables x,y, a, and q to the expression ")
    x = -5
    y = 17
    a = 44
    q = 69
    if(x == -5) and (y== 17) and (a == 44) and (q == 69):
        print(eval(tt), zz)
    elif(x != -5) and (y != 17) and (a != 44) and (q != 69):
        print(eval(tt), zz)

main()
