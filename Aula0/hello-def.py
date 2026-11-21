# Função para chamar o nome com def
# Vamos criar uma função para chamar o nome do usuário, assim podemos chamar a função quantas vezes quisermos, sem precisar digitar o código novamente
# Def é uma palavra reservada do python, que significa definição, ou seja, estamos definindo uma função
# exemplo de um def que foi definido antes de chamar a função hello, assim o python vai entender que é para chamar a função hello, e não o nome do usuário

#def hello(to = "World"): # definido que o to é uma variável que vai receber o nome do usuário, caso o usuário não digite nenhum nome, o python vai entender que é para chamar o nome padrão, que é "World"
#    print("Hello,", to)

#hello() # chamando a função sem passar nenhum parâmetro, assim o python vai entender que é para chamar o nome padrão, que é "World"
#name = input("Qual o seu nome?")

#hello(name) # chamando a função passando o parâmetro name, assim o python vai entender que é para chamar o nome que o usuário digitou


def main ():
    name = input("Qual o seu nome?").strip().title()
    hello()

 
def hello(): # definido que o to é uma variável que vai receber o nome do usuário, caso o usuário não digite nenhum nome, o python vai entender que é para chamar o nome padrão, que é "World"
   print("Hello,", name)

main ()
  