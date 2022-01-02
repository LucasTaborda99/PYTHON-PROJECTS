import random

print("\n---------- Descobrindo o número inteiro ----------\n")

top_of_range = input("Digite um número maior que zero e inteiro: ")

# verifica se o número digitado pelo usuário é realmente um número
if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("\nPor favor digite um número maior que 0 e inteiro na próxima vez.\n")
        quit()
else:
    print("\nPor favor digite um número positivo e inteiro na próxima vez.\n")
    quit()

# gera números aleatórios from 0 to top_of_range
randon_number = random.randint(0, top_of_range)

# variável do número de tentativas do usuário
guesses = 0

while True:

    user_guess = input("\nDê o seu palpite de um número a partir de 0 até " + str(top_of_range) + ": ")

    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("\nPor favor digite um número positivo e inteiro na próxima vez.")
        continue

    if user_guess > top_of_range:
        print("\nSeu palpite está fora do range, por favor digite um número que esteja dentro do range informado acima.")
        continue

    # faz a contagem do número de tentativas
    guesses += 1

    if user_guess == randon_number:
        print("\nVocê acertou :)")
        break

    elif user_guess > randon_number:
            print("\nSeu palpite estava acima do número a ser descoberto, quase lá ! Continue ...")
    else:
            print("\nSeu palpite estava abaixo do número a ser descoberto, quase lá ! Continue ...")

if guesses == 1:
    print("\nVocê acertou em", guesses, "tentativa, parabéns ;)\n")
else:
    print("\nVocê acertou em", guesses, "tentativas, parabéns ;)\n")
