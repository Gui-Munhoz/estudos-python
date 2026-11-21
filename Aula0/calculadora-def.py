def main():
    x = int(input("Digite um número: "))
    print(" O quadrado do numero é", square(x))

def square(x):
    return pow(x, 2)

main()