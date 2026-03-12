import random

# Classe Enemy representa o inimigo
class Enemy:

    # Construtor da classe
    def __init__(self, nome, vida):

        self.nome = nome
        self.vida = vida


    # Método de ataque do inimigo
    def atacar(self):

        # inimigo causa dano aleatório
        dano = random.randint(1,4)

        print(self.nome, "atacou e causou", dano, "de dano")

        return dano


    # Método para receber dano
    def tomar_dano(self, dano):

        self.vida -= dano

        print(self.nome, "recebeu", dano, "de dano")

        if self.vida > 0:
            print("Vida restante do inimigo:", self.vida)