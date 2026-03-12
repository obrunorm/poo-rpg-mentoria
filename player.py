import random

# Classe Player representa o jogador
class Player:

    # Construtor da classe
    # Ele é executado automaticamente quando criamos um objeto
    def __init__(self, nome, vida, mana, arma):

        # Atributos do objeto
        self.nome = nome
        self.vida = vida
        self.mana = mana
        self.arma = arma


    # Método de ataque
    # "self" representa o próprio objeto
    def atacar(self):

        # Dano base
        dano = random.randint(1,5)

        # Cada arma modifica o dano
        if self.arma == "espada":
            dano += 5

        elif self.arma == "machado":
            dano += 7

        elif self.arma == "cajado":
            dano += 3
            self.mana += 1   # cajado recupera mana

        # Mostra o ataque na tela
        print(self.nome, "atacou usando", self.arma, "e causou", dano, "de dano")

        # Retorna o dano causado
        return dano


    # Método para receber dano
    def tomar_dano(self, dano):

        # diminui a vida
        self.vida -= dano

        print(self.nome, "recebeu", dano, "de dano")
        print("Vida restante:", self.vida)