
# 4º Mini-Projeto: O Validador de Senha
# Objetivo: Permitir acesso somente quando a senha correta for digitada.
# - Loop while que solicita a senha até estar correta.
# Conceitos: while, comparação de strings, input, limpeza com strip()

# Valida a diferença da senha incorreta e correta
print("\n====== Bem-vindos(as) ao Mini-Projeto 4º: O Validador de Senha ======\n")

senha_secreta = "python1234"

print("====== Sistema de Segurança ======\n")

senha_digitada = input("Digite uma senha incorreta, inicialmente: \n").strip()

while senha_digitada != senha_secreta:
    print("\nSenha incorreta! Acesso negado, tente novamente. \n")

    senha_digitada = input("Por favor, digite novamente a senha: \n")

print("\nA senha correta foi informada. Acesso concedido!\n")

print("====== Fim do Programa ======\n")
