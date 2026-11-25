# % reprenta aritimetimerica modular, mostrar o resto da divisão
# Exemplo 1 :Nesse exemplo vamos trazer se o x é par ou impar
#x = int(input("Qual é x?"))
#if x % 2 == 0:
#    print("x é par")
#else:
#    print("x é impar")

def main():
    x = int(input("Qual é x?"))
    if is_even(x):
        print ("x é par")
    else:
        print("x é impar")

#def is_even(n):
#    if n % 2 == 0:
#        return True
#    else:
#        return False

#melhorado
#def is_even(n):
#    return True if n % 2 == 0 else False

#ainda melhor
def is_even(n):
    return n % 2 == 0

main()