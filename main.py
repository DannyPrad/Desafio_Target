numero = int(input("Digite um número: "))

# Verifica se o número é 0 diretamente, pois pertence à sequência
if numero == 0:
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    a, b = 0, 1  # Inicializa os dois primeiros números da sequência

    # Gera a sequência até que 'b' seja maior ou igual ao número informado
    while b < numero:
        a, b = b, a + b

    # Verifica se o número pertence à sequência
    if b == numero:
        print(f"O número {numero} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {numero} NÃO pertence à sequência de Fibonacci.")
