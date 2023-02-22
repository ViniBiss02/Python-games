import forca
import adivinhacao

print("*******************")
print("Escolha o seu jogo!")
print("*******************")

print("(1) Forca \n(2) Adivinhação")

jogo = int(input("Qual jogo ?\n"))

if jogo == 1:
    print("Jogando Forca de Frutas")
    forca.jogar()
elif jogo == 2:
    print("Jogando Adivinhação")
    adivinhacao.jogar()