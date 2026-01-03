# 3º Mini-Projeto: O Sorteados de Nomes + Lista de Convidados + Tabuada
# Objetivo: Exercitar listas e loops com um programa que:
# Saúda cada convidado de uma lista;
# Gera a tabuada de um número escolhido pelo usuário (1 a 10).
# Conceitos usados:
# Listas (list), laço for, range, tratamento de erros com try/except, input(), print(), f-strings.

print("\n====== Bem-vindos(as) ao Mini-Projeto 3º:  O Sorteador de Nomes ======\n")

lista_de_convidados = ["Ana", "Bruno", "Carla", "Daniel"]

print("====== Iniciando a Festa ======\n")

# O laço de repetição 'for loop' vai passar por casa nome da variavel de lista 'lista_de_convidados'
for nome in lista_de_convidados:
    print(f"Olá, {nome}! Seja bem-vindo(a)!")

print("\n====== Todos foram convidados! ======\n")

print("\n====== Tabuada ======\n")
numero_retornado = input("Digite um número para a tabuada: ").strip()
print(f"\nNumero informado (texto): {numero_retornado}")

try:
    numero_convertido = int(numero_retornado)
    print(f"\nImprimindo a tabuada do {numero_convertido}: \n")

    for index in range(1, 11):
        conta = numero_convertido * index
        print(f"{numero_convertido} x {index} = {conta}")

    print("\n")
except ValueError:
    print("A entrada digitada é inválida! Digite um número inteiro (ex.: 1, 7, 5). \n")
