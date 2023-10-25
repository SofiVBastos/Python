# print(6789+123)
# print("ola"+"mundo")
# print(200-58)
# print(2*245)
# print(6789/3)


# x=2
# y=3
# print(x+y)


# x=9
# y="gatos"
# print(x,y)

# x="3"
# y="tigres tristes"
# print(x,y)

# x=5
# y="rosas"
# # print(x+y)
# print(x,y)

# x=10
# y=9
# print(x+y)
# print(x*y)
# print(x-y)


# def imprimirCumprimento(parametro):
#     print("olá,", parametro, "!!!")
#
# imprimirCumprimento("Ninja")


# nome=input("Digite seu nome: ")
# TI= float(input(("Digite sua carteira de identidade")))
#
# print("Seu nome é", nome, "e sua carteira de identidade é", TI)

# km= float(input(("Digite um numero: ")))
# m=km*1000
# cm=km*1000000
#
# def TransformarKm (Km):
#     print(Km, "em kilometros ", m, "metros e ", cm, "centimetros")
#
# TransformarKm(km)


nota1 = float(input("digite a primeira nota: "))
nota2 = float(input("digite a segunda nota: "))
nota3 = float(input("digite a terceira nota: "))

lista = [nota1, nota2, nota3]

def calcularMédia():
    i = 0
    while i <= len(lista):
        soma = soma + lista[i]
        i = i + 1

    media = soma / len(lista)

    if(media >= 7):
        print("Aprovado!")
    else:
        print("Reprovado")
        print(soma)


calcularMédia()