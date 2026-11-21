# podemos colocar o input dentro do float, assim não precisamos colocar a variável como float depois
x = float(input("Digite um número: "))
y = float(input("Digite outro número: "))
#precisa colocar se a variável é int ou float, caso contrário o python vai concatenar os números e não somar
#quando tiver [] na formula do python, significa que é opcional, ou seja, não precisa colocar, mas se colocar, 
#o python vai entender que é para arredondar o número, no caso do float, o python vai arredondar o número para 2 casas decimais,
# caso não coloque, o python vai arredondar para 15 casas decimais
# exemplo print(round(x + y, 2))
 #z = round(x / y, 2)

z = x/y
#outro caso mais eficiente para colocar os pontos e virgular em numeros maiores que 999,99, é colocar o locale, assim o python vai entender que é para colocar os pontos e virgulas nos números maiores que 999,99
print(f"{z:,.2f}")
