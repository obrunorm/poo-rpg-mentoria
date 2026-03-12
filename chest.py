import random

# Classe do Baú
class Chest:

    # Método que abre o baú
    def abrir(self):

        # Lista de itens possíveis
        itens = ["moeda", "poção de vida", "espada lendária"]

        # Escolhe um item aleatório
        item = random.choice(itens)

        print("\nVocê abriu um baú!")
        print("Você encontrou:", item)