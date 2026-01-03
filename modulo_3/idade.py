idade_retornada = input("Qual a sua idade? \n")

print(idade_retornada)

idade_convertida = int(idade_retornada)

print(idade_convertida)

if idade_convertida >= 18:
    print("Você é maior de idade!")
elif idade_convertida < 18:
    print("Você é menor de idade!")
else:
    print('Não foi possível identificar se a pessoa é maior ou menos de idade de acordo com a valor fornecido anteriormente!')