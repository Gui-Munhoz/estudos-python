# Função para chamar o nome

# Podemos colocar também na mesma linha da função inicial : nome função = input("Qual o seu nome?").strip().title()
# name = input("Qual o seu nome?").strip().title()

# Podemos colocar duas funcionalidades de uma vez: nome função = nome função.strip().title()
name = input("Qual o seu nome?")
name = name.strip().title()

#printa o nome que o usuário digitou
print(f"Hello, {name}!")