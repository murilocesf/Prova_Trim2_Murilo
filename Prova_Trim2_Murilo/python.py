nome = input("Digite o seu nome")
mes = int(input("Digite o mês que você quer consultar"))
dia = int(input("Digite o dia que você quer consultar"))

if mes == 1 or mes == 2 or (mes == 3 and dia < 21) or (mes == 12 and dia >= 21):
    print("Verão")
elif (mes == 3 and dia >= 21) or mes == 4 or mes == 5 or (mes == 6 and dia < 21):
    print("Outono")
elif (mes == 6 and dia >= 21) or mes == 7 or mes == 8 or (mes == 9 and dia < 23):
    print("Inverno")
elif (mes == 9 and dia >= 23) or mes == 10 or mes == 11 or (mes == 12 and dia < 21):
    print("Primavera")