# programa que mostra a casa do harry potter
name = input("Qual o seu nome?")

#usar match e case por linha
#match name:
#    case "Harry":
#        print("Grifinória")
#    case "Hermione":
#       print("Grifinória")
#    case "Ron":
#        print("Grifinória")
#   case "Draco":
#        print("Sonserina")
#    case _:
#        print("Casa não encontrada")

# Mais eficiente
match name:
    # usar o | permite colocar vários no mesmo print
    case "Harry" | "Hermione" | "Ron":
        print("Grifinória")
    case "Draco":
        print("Sonserina")
    case _:
        print("Casa não encontrada")