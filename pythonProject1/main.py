espaco=" "
folha= "\033[92m\u22EF\033[0m"
estrela="\033[93m\u2605\033[0m"
enfeiteRosa="\033[95m\u23FA\033[0m"
br="\n"
presente="\u2AF6"

# print(espaco*15,
#       br,
#       espaco*13+folha*5,
#       br,
#       espaco*12+folha*7,
#       br,
#       espaco*11+folha*9,
#       br,
#       espaco*10+folha*11,
#       br,
#       espaco*9+folha*13,
#       br,
#       espaco*8+folha*15,
#       br,
#       espaco*7+folha*5,"Feliz",folha*5,
#       br,
#       espaco*6+folha*6,"Natal",folha*6,
#       br,
#       espaco*5+folha*21,
# )


# print("Sofia")

# a=3
# b=5
# print(2*a*3*b)

# a=5
# b=11
# c=37
# print(a+b+c)

# print("""\nNúmero Tipo númerico
# inteiro
# ponto flutuante
# ponto flutuante
# inteiro
# inteiro
# ponto flutuante""")

# salario = float(input("\nDigite o seu salário: "))
# imposto = salario * 0.2
#
# if(salario > 1200.0):
#     novoSalario = salario - imposto
#     print("Seu salário com imposto é:",novoSalario)
# else:
#     print("Seu salário sem imposto é:",salario)


# materia01=float(input("\nDigite a primeira nota:"))
# materia02=float(input("Digite a segunda nota:"))
# materia03=float(input("Digite a terceira nota:"))
#
# calculoNota= (materia01+materia02+materia03) / 3
#
# if(calculoNota > 7):
#     print("Parabéns, você foi aprovado!!!")
# else:
#     print("Infelizmente você foi reprovado :(")

# num01= int(input("Digite um número inteiro:"))
# num02= int(input("Digite outro número inteiro:"))
# soma= num01+num02
#
# if(soma % 2 == 0):
#     print("O número",soma,"é par!")
# else:
#     print("O número",soma,"é impar!")

# def maiorEntreDoisNumeros(num01, num02):
#     if(num01 > num02):
#         frase = f"O maior número entre {num01} e {num02} é: {num01}"
#         return frase
#     elif(num02 > num01):
#         return f"O maior número entre {num01} e {num02} é: {num02}"
#     else:
#         return "Não existe maior pois os números são iguais"
#
#
# numero01 = int(input("Digite um numero inteiro: "))
# numero02 = int(input("Digite outro numero inteiro: "))
#
# resultado = maiorEntreDoisNumeros(numero01, numero02)
#
# print(resultado)

# ----------------------------------------
# 1)
# Exercicio função python
# num = int(input("Digite um numero:"));
#
# def multImpunt(num):
#     for i in range(num+1):
#         texto = ""
#         texto += str(i)
#         print(texto * i)
#
# multImpunt(num)

# ------------------------------
# 2)
# num = int(input("Digite um numero:"))
#
# def imprimir(num):
#     texto = ""
#     for i in range(1 ,num + 1):
#         texto += str(i)
#         print(texto)
#
# imprimir(num)

# ------------------------------------
# 3)
# num01 = int(input("Digite o primeiro numero: "))
# num02 = int(input("Digite o segundo numero: "))
# num03 = int(input("Digite o terceiro numero: "))
#
# def soma(num1, num2, num3):
#     total = num1+ num2 + num3
#     print("o total da soma é %d" %(total))
#
# soma(num01, num02, num03)

# -----------------------------------------
# 4)
# num = int(input("Digite um numero:"))
#
# def positiveOrNegative(num):
#     if(num > 0):
#         print("P")
#     else:
#         print("N")
#
# positiveOrNegative(num)

# ---------------------------------------
# 5)
# valor = float(input("Digite seu custo: "))
# taxa = float(input("Digite a porcentagem do imposto: "))
#
# def somaImposto(taxaImposto, custo):
#     valorComImposto = custo * (taxaImposto / 100)
#     custo += valorComImposto
#     print("Novo valor : %.2f" %(custo))
#
# somaImposto(taxa, valor)

# -------------------------------------
# 6)
# def formartarSaidaAM(hora, minuto):
#     if(hora < 10 and minuto >= 10):
#         print(f"0{hora}:{minuto} AM")
#     elif(hora < 10 and minuto < 10):
#         print(f"0{hora}:0{minuto} AM")
#     elif(hora >= 10 and minuto < 10):
#         print(f"{hora}:0{minuto} AM")
#     elif(hora >= 10 and minuto >= 10):
#         print(f"{hora}:{minuto} AM")
#
# def formartarSaidaPm(hora, minuto):
#     if (hora < 10 and minuto >= 10):
#         print(f"0{hora}:{minuto} PM")
#     elif (hora < 10 and minuto < 10):
#         print(f"0{hora}:0{minuto} PM")
#     elif (hora >= 10 and minuto < 10):
#         print(f"{hora}:0{minuto} PM")
#     elif (hora >= 10 and minuto >= 10):
#         print(f"{hora}:{minuto} PM")
# def converterHora(hora,minuto):
#     if(hora < 12 and hora > 0 and minuto < 60 and minuto >= 0):
#         formartarSaidaAM(hora,minuto)
#     elif(hora == 0 and minuto < 60 and minuto >= 0):
#         hora = 12
#         formartarSaidaAM(hora,minuto)
#     elif(hora == 12 and minuto < 60 and minuto >= 0):
#         formartarSaidaPm(hora, minuto)
#     elif(hora >= 13 and hora <= 23 and minuto < 60 and minuto >= 0):
#         hora -= 12
#         formartarSaidaPm(hora,minuto)
#     else:
#         print("Digite um valor valido'")
#
# while True:
#     horas = int(input("Digite uma hora: "))
#     minutos = int(input("Digite um minuto: "))
#
#     converterHora(horas,minutos)
#
#     repetir = input("Deseja converter novamente? (Sim/Não)")
#     if repetir != "Sim":
#         break

# ----------------------------------
# 8)
# def valorPagamento(v, d):
#     if(d == 0):
#         return v
#     else:
#         valorMulta = v * 0.03
#         valorJuros = v * (0.001 * d)
#         totalPagar = v + valorJuros + valorMulta
#         return totalPagar
#
#
# def relatorio(totalPrest, totalDia):
#     print(f"""Relatório do dia:
#     Quantidade de prestações pagas: {totalPrest}
#     Valor total: {totalDia:.2f}""")
#
#
# totalDia = 0.0
# totalPrest = 0
#
# while True:
#     valorPrest = float(input("Digite o valor da prestação: "))
#     if(valorPrest == 0):
#         break
#
#     diasAtraso = int(input("Quantos dias está atrasada? "))
#
#     totalPagar = valorPagamento(valorPrest,diasAtraso)
#
#     print(f"Valor a ser pago hoje: R${totalPagar:.2f} \n")
#
#     totalDia += totalPagar
#     totalPrest += 1
#
# relatorio(totalPrest,totalDia)


#-----------------------------
# 8)
# num = int(input("Digite um numero inteiro: "))
# qtdCaracter = len(str(num))
# print(qtdCaracter)

# ----------------------------------
# 9)
