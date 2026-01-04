# 6º Mini-Projeto: A Calculadora de Frete Logístico
# Objetivo:
# - Criar uma ferramenta simples para calcular o valor total de uma compra com frete.
# Regra de Negócio:
# - Cada produto possui um valor base informado pelo usuário.
# - O frete é calculado a R$ 10,00 por quilo do produto.
# Funcionalidades:
# - Solicitar ao usuário o valor do produto e o peso em kg.
# - Calcular o total (valor do produto + frete).
# - Exibir o resultado formatado para o usuário.
# Conceitos aplicados:
# - Funções com parâmetros e retorno.
# - Operações matemáticas simples.
# - Entrada e saída de dados (input/print).
# - Formatação de strings com f-strings.
# Aprendizado:
# - Como encapsular lógica em funções reutilizáveis.
# - Como aplicar regras de negócio em código.
# - Como melhorar a experiência do usuário com mensagens claras.


print("\n" + "=" * 100)
print("      Bem-vindos(as) ao Mini-Projeto 6º: A Calculadora de Frete Logístico      ")
print("=" * 100)

def ler_float(msg):
    # Lê número decimal, aceita vírgula e garante não-negativo
    while True:
        valor = input(msg).strip().replace(",", ".")
        try:
            v = float(valor)
            if v < 0:
                print("O valor não pode ser negativo! Tente novamente.")
                continue
            return v
        except ValueError:
            print("Entrada inválida! Digite um número, por favor.")

def calcular_total(valor_produto, peso_kg, preco_por_kg):

    """
    Calcula o total com frete:
    - valor_produto: valor base do produto
    - peso_kg: peso do produto em kg
    - preco_por_kg: preço do frete por kg
    Retorna: (total, valor_frete)
    """

    valor_frete = peso_kg * preco_por_kg
    total = valor_produto + valor_frete
    return total, valor_frete

def formata_brl(valor):
    # Formata número como moeda BRL (pt-BR)
    return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

print("\n" + "=" * 60)
print("      Sistema de Logística:      ")
print("=" * 60)

# Entrada
v_prod = ler_float("Qual o valor do produto? R$: ")
peso = ler_float("Qual o peso (KG)? ")

preco_por_kg = 10.0

# Cálculo (ex.: frete mínimo R$ 20, sem frete grátis)
valor_final, frete = calcular_total(v_prod, peso, preco_por_kg)

# Saída
print("\n" + "-" * 60)
print(f"Valor do produto: {formata_brl(v_prod)}")
print(f"Frete ({peso} kg x {formata_brl(preco_por_kg)}): {formata_brl(frete)}")
print(f"Total a pagar: {formata_brl(valor_final)}")
print("-" * 60 + "\n")

print("=" * 60)
print("      Fim do Programa      ")
print("=" * 60)
print("\n")
