# 5º Mini-Projeto: O Cadastro Centralizado
# Objetivo:
# - Coletar informações do usuário em um dicionário único.
# - Exibir a ficha organizada com formatação amigável.
# Conceitos:
# - dicionários (dict), input/print, validação simples, f-strings, formatação de texto.

print("\n" + "=" * 100)
print("      Bem-vindos(as) ao Mini-Projeto 5º: O Cadastro Centralizado (V2)      ")
print("=" * 100)

# 1. Criamos um dicionario vazio inicialmente
cadastro = {}

# 2. Perguntar os dados do usuário e salvar nas respectivas chaves do dicionario 'cadastro'
cadastro["nome"] = input("Digite o seu nome: ").strip()
cadastro["comida"] = input("Digite a sua comida favorita: ").strip()
cadastro["local_moradia"] = input("Digite a cidade onde você mora: ").strip()

# 3. Validação simples: se algum campo estiver vazio, alerta
if not all(cadastro.values()):
    print("\nAtenção: Existem campos que não foram preenchidos corretamente!\n")

# 4. Gerar a ficha: Mostrar os dados capturados
print("\n" + "=" * 60)
print("      Sua Ficha de Cadastro:      ")
print("=" * 60)

# Usamos o loop for para formatar o dicionário sem vários prints manuais
for chave, valor in cadastro.items():
    # Rótulo bonito: troca '_' por espaço e capitaliza cada palavra
    chave_formatada = chave.replace("_", " ").title()
    valor_formatado = valor.title()
    print(f"{chave_formatada}: {valor_formatado}")

print("\nInformações salvas com sucesso!\n")
print("=" * 60)

print("      Fim do Programa      ")
print("=" * 60)
print("\n")