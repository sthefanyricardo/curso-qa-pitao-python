# 2º Mini-Projeto: Porteiro Eletrônico
# Objetivo: Criar um programa que simula a lógica de acesso a um evento com base na idade informada pelo usuário.

# Regras:
# Se a idade for maior que 65, a entrada é gratuita.
# Se a idade estiver entre 18 e 65, a entrada custa R$ 20,00.
# Se a idade for menor que 18, o acesso não é permitido.

# Para implementar isso, usamos estruturas condicionais if, elif e else, que permitem múltiplos caminhos no código.
# A comparação encadeada (18 <= idade <= 65) deixa a lógica mais legível e evita dependência da ordem das condições.

IDADE_MIN_PAGANTE = 18
IDADE_MAX_PAGANTE = 65
PRECO_ENTRADA = 20.00

print("\n====== Bem-vindos(as) ao Mini-Projeto 2º: Porteiro Eletrônico ======\n")

idade_retornada = input("Digite a sua idade: \n").strip()
print(f"\nIdade informada (texto): {idade_retornada}")

try:
    idade_convertida = int(idade_retornada)

    print(f"Idade convertida (int): {idade_convertida}\n")

    # Podemos utilizar a comparação encadeada (18 <= idade <= 65), recurso do Python que
    # torna a regra de intervalo mais legível do que 'idade >= 18 and idade <= 65'.
    # As faixas ficam explícitas e o fluxo não depende da ordem dos elif.
    
    # Validação adicional: impedir idades negativas e 0
    if idade_convertida <= 0:
        print("\nIdade inválida. A idade não pode ser negativa e nem igual a 0.")
    elif IDADE_MIN_PAGANTE <= idade_convertida <= IDADE_MAX_PAGANTE:        
        # Formatação BR simples sem locale: 20.00 -> "20,00"
        PRECO_FORMATADO = f"{PRECO_ENTRADA:.2f}".replace(".", ",")
        print(f"Sua entrada no evento custa: R$: {PRECO_FORMATADO}. Seja bem-vindo(a)! \n")
    elif idade_convertida > IDADE_MAX_PAGANTE:
        print("Aproveite! Sua entrada no evento é gratuita. \n")
    else: # menores de 18 anos
        print("O acesso ao evento só é permitido a maiores de 18 anos. \n")

except ValueError:
    print("A entrada digitada é inválida! Digite um número inteiro, ex.: 18, 25, 70.")
