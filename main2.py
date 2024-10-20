# entrada do usuário
texto = input("Digite uma string: ")
# Contagem de letras 'a' ou 'A'
quantidade_a = texto.lower().count('a')
# aparece resultado
print(f"A letra 'a' aparece {quantidade_a} vezes na string.")