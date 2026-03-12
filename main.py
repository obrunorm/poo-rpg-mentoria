from player import Player
from enemy import Enemy
from chest import Chest


print("Bem vindo ao meu RPG!!!")


# jogador digita o nome
nome = input("Digite seu nome: ")


# jogador escolhe arma
print("\nEscolha sua arma:")
print("1 - Espada")
print("2 - Machado")
print("3 - Cajado")

opcao = input("Digite o número da arma: ")


# define qual arma foi escolhida
if opcao == "1":
    arma = "espada"

elif opcao == "2":
    arma = "machado"

else:
    arma = "cajado"


# cria objeto jogador
player1 = Player(nome, 20, 10, arma)

print("\nOlá", player1.nome)
print("Você escolheu:", player1.arma)


# cria inimigo
enemy1 = Enemy("Goblin", 15)

print("\nUm inimigo apareceu:", enemy1.nome)


# sistema simples de batalha
while enemy1.vida > 0 and player1.vida > 0:

    input("\nPressione ENTER para atacar")

    # jogador ataca
    dano = player1.atacar()

    # inimigo recebe dano
    enemy1.tomar_dano(dano)


    # verifica se inimigo morreu
    if enemy1.vida <= 0:

        print("\nO inimigo foi derrotado!")

        # cria o baú
        bau = Chest()

        # abre o baú
        bau.abrir()

        break


    # inimigo ataca
    dano_enemy = enemy1.atacar()

    # jogador recebe dano
    player1.tomar_dano(dano_enemy)


# verifica se jogador morreu
if player1.vida <= 0:
    print("\nVocê foi derrotado...")