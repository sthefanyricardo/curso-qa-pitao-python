# 3º Mini-Projeto: O Sorteador de Nomes + Lista de Convidados + Tabuada
# Objetivo: Exercitar listas e loops com um programa que:
# - Saúda cada convidado de uma lista;
# - Sorteia nome(s)
# - Gera a tabuada de um número escolhido pelo usuário (1 a 10).
# Conceitos usados:
# Listas (list), laço for, range, tratamento de erros com try/except, input(), print(), f-strings.

import random

# Gera a lista de convidados
print("\n====== Bem-vindos(as) ao Mini-Projeto 3º: Lista de Convidados ======\n")

print("Você quer criar uma lista de convidados ou usar uma lista aleatória?")
print("Digite 'Criar' para informar os nomes separados por vírgula.")
print("Digite 'Aleatorio' para usar uma lista gerada pelo programa.\n")

opcao_escolhida = input("Digite a sua escolha: ").strip().lower()

if opcao_escolhida == "criar":
    nomes_digitados = input("\nDigite os nomes separados por vírgula (ex.: Ana, Bruno, Carla):\n").strip()

    # Converte para lista, remove espaços extras e entradas vazias
    lista_de_convidados = [nome.strip().title() for nome in nomes_digitados.split(",") if nome.strip()]

    # Remove duplicados mantendo a ordem (se o usuário repetir nomes)
    vistos = set()
    lista_de_convidados = [n for n in lista_de_convidados if not (n in vistos or vistos.add(n))]

    if not lista_de_convidados:
        print("\nNenhum nome válido foi informado. Encerrando o programa.\n")
        exit()

elif opcao_escolhida == "aleatorio":
    lista_de_convidados = [
        "Ana", "Bruno", "Carla", "Daniel", "Eduarda", "Felipe",
        "Gabriela", "Hugo", "Isabela", "João", "Kátia", "Luís",
        "Mariana", "Nina", "Otávio", "Paula", "Rafael", "Sofia",
        "Tiago", "Vitória"
    ]
else:
    print("\nOpção inválida! Encerrando o programa.\n")
    exit()

print("\n====== Iniciando a Festa ======\n")

# Saudar cada convidado
# O laço 'for' vai passar por cada nome da variável de lista 'lista_de_convidados'
for nome in lista_de_convidados:
    print(f"Olá, {nome}! Seja bem-vindo(a)!")

print("\n====== Todos foram convidados! ======\n")



# Sorteio simples (com opção de vários sorteados, ainda simples)
print("\n====== Bem-vindos(as) ao Mini-Projeto 3º: O Sorteador de Nomes ======\n")

print("Ordem atual da lista:\n", ", ".join(lista_de_convidados))

random.shuffle(lista_de_convidados)
print("\nOrdem da lista embaralhada:\n", ", ".join(lista_de_convidados))

qtd_txt = input("\nQuantas pessoas você deseja sortear? (ex.: 1, 2, 3): ").strip()
try:
    qtd = int(qtd_txt)
except ValueError:
    print("Entrada inválida. Sorteando 1 pessoa.\n")
    qtd = 1

if qtd <= 0:
    print("Quantidade deve ser >= 1. Sorteando 1 pessoa.\n")
    qtd = 1

qtd = min(qtd, len(lista_de_convidados))  # não permitir pedir mais do que a lista tem
if qtd == 1:
    sorteado = random.choice(lista_de_convidados)
    print(f"A pessoa sorteada para ganhar um brinde é: {sorteado} 🎁\n")
else:
    sorteados = random.sample(lista_de_convidados, k=qtd)
    print(f"As pessoas sorteadas são: {', '.join(sorteados)} 🎁\n")


# Gera e imprimi tabuada(s)
print("\n====== Bem-vindos(as) ao Mini-Projeto 3º: A Tabuada ======\n")

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

print("====== Fim do Programa ======\n")