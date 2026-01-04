pessoa = {
    'nome': 'Sthefany A. Ricardo',
    'idade': 26,
    'cidade': 'São Paulo - SP',
    'ativo': True
}

print("\nDicionario pessoa: ", pessoa)

print("\nValor da chave 'cidade' no dicionario 'pessoa': ", pessoa['cidade'])

chave = 'nome'
print(f"\nPosição: {chave} | Valor: {pessoa[chave]}, no dicionário 'pessoa'\n")

pessoa['idade'] = 23

pessoa['profissao'] = 'QE/QA'

print("Dicionario pessoa: ", pessoa)

print("\n")

for chave in pessoa:
    print(f"Chaves: {chave}, no dicionário 'pessoa'")

print("\n")

for chave in pessoa:
    print(f"Chave: {chave} | Valor: {pessoa[chave]}")
    
print("\n")

for chave in pessoa:
    print("Valores no dicionario 'pessoa'", pessoa[chave])
    
print("\n")

for chave, valor in pessoa.items():
    print(f"Chave: {chave} e Valor: {valor}, no dicionário 'pessoa'")

print("\n")