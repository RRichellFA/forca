import getpass
print("Jogo da forca")
print('1- O desafiante digita o segredo da forca, ele ficará escondido, portanto certifique-se de digitar corretamente.')
print('2- O jogador terá 5 chances de adivinhar o segredo, letra por letra. Se ele errar perde, se completar o '
      'segredo, ganha.')

forca = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

print("Vamos começar!")
segredo = getpass.getpass("Digite o segredo da forca: ").strip().upper()
print(forca[0])
erros = 0
acertos = 0
letras = []
letrascertas = []
print(f"O segredo escolhido tem {len(segredo)} letras.")
while erros < 5 or acertos == len(segredo):
  jogador = input("Digite uma letra.")[0].upper()
  if jogador not in letras:
    letras.append(jogador)
    letras.sort()
  else:
    print("Essa letra ja foi escolhida.")
    continue
  if jogador in segredo:
    print("ACERTOU")
    acertos +=1
    print(forca[erros])
    letrascertas.append(jogador)
    print(f"As letras corretas escolhidas foram {letrascertas}.")
    if acertos == len(segredo):
      print("Parabéns, você venceu!")
      break
  else:
    print("ERROU")
    erros +=1
    print(forca[erros])
    print(f"Você tem mais {5-erros} tentativas.")
    if erros == 5:
      print(forca[6])
      print(f'O segredo era "{segredo}"')
      print("Você perdeu!")
  print(f"As letras escolhidas foram {letras}.")
print("FIM DO JOGO")