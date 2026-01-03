# 1º Mini-Projeto: Sistema de Cadastro Simples
# Objetivo: Criar um programa interativo que coleta informações e gera uma ficha de cadastro organizada!
# Regras - O que o seu programa deve fazer:
# Perguntar o nome do usuário.
# Perguntar a comida favorita do usuário.
# Perguntar a cidade onde o usuário mora.
# No final, imprimir uma ficha de cadastro completa com todos os dados coletados.
# Funcionalidades:
# Solicitar três informações: nome, comida favorita e cidade onde mora.
# Validar se os campos foram preenchidos (não permitir valores vazios).
# Exibir uma ficha formatada com os dados informados.

print("\n====== Bem-vindos(as) ao Mini-Projeto 1º: Sistema de Cadastro Simples ======\n")

# 1. Perguntar os dados do usuário
nome = input("Digite o seu nome: ").strip()
comida = input("Digite a sua comida favorita: ").strip()
local_moradia = input("Digite a cidade onde você mora: ").strip()

# Validação simples: se algum campo estiver vazio, alerta
if not nome or not comida or not local_moradia:
    print("\nAtenção: Todos os campos devem ser preenchidos!\n")
else:
    # 2. Mostrar os dados capturados
    print("\n====== Sua Ficha de Cadastro ======\n")
    print(f"Nome: {nome}")
    print(f"Comida favorita: {comida}")
    print(f"Cidade: {local_moradia}")
    print("\nInformações salvas com sucesso!\n")
