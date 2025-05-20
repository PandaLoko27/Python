import time
import random

class Sim:
    def __init__(self, nome):
        self.nome = nome
        self.fome = 100
        self.energia = 100
        self.diversao = 100
        self.higiene = 100
        self.dinheiro = 50
        self.vivo = True
        self.dias_sobrevividos = 0
        self.motivo_morte = None

    def status(self):
        return {
            "Fome": self.fome,
            "Energia": self.energia,
            "Diversão": self.diversao,
            "Higiene": self.higiene,
            "Dinheiro": self.dinheiro,
        }

    def mostrar_status(self):
        print(f"\nStatus de {self.nome}:")
        for k, v in self.status().items():
            print(f"{k}: {v}")

    def checar_estado(self):
        causas = {
            "fome": self.fome,
            "exaustão": self.energia,
            "tédio extremo": self.diversao,
            "falta de higiene": self.higiene
        }
        for motivo, valor in causas.items():
            if valor <= 0:
                self.vivo = False
                self.motivo_morte = motivo
                print(f"\n :( {self.nome} morreu de {motivo}. Fim de jogo.")
                break

    def comer(self):
        print(f"\n{self.nome} está comendo.")
        self.fome = min(100, self.fome + 30)
        self.energia -= 10

    def dormir(self):
        print(f"\n{self.nome} está dormindo.")
        self.energia = min(100, self.energia + 50)
        self.higiene -= 10

    def tomar_banho(self):
        print(f"\n{self.nome} está tomando banho.")
        self.higiene = min(100, self.higiene + 40)
        self.energia -= 5

    def trabalhar(self):
        print(f"\n{self.nome} está trabalhando.")
        self.energia -= 30
        self.fome -= 20
        self.diversao -= 20
        self.higiene -= 10
        self.dinheiro += 50
        print(f"{self.nome} ganhou R$50!")

    def assistir_tv(self):
        print(f"\n{self.nome} está assistindo TV.")
        self.diversao = min(100, self.diversao + 25)
        self.energia -= 10
        self.fome -= 5

    def comprar_item(self):
        while True:
            print("\n🛒 Itens disponíveis para compra:")
            print("1. Comida Rápida (+20 Fome) - R$20")
            print("2. Café Energético (+30 Energia) - R$30")
            print("3. Jogo Novo (+40 Diversão) - R$40")
            print("0. Sair da loja")

            escolha = input("Escolha o item (0-3): ").strip()
            if escolha == "0":
                print("Saindo da loja...")
                break
            elif escolha == "1" and self.dinheiro >= 20:
                self.fome = min(100, self.fome + 20)
                self.dinheiro -= 20
                print(f"{self.nome} comprou comida rápida.")
                break
            elif escolha == "2" and self.dinheiro >= 30:
                self.energia = min(100, self.energia + 30)
                self.dinheiro -= 30
                print(f"{self.nome} comprou um café energético.")
                break
            elif escolha == "3" and self.dinheiro >= 40:
                self.diversao = min(100, self.diversao + 40)
                self.dinheiro -= 40
                print(f"{self.nome} comprou um jogo novo.")
                break
            else:
                print("Dinheiro insuficiente ou escolha inválida. Tente novamente.")

    def passar_tempo(self):
        self.fome -= random.randint(5, 10)
        self.energia -= random.randint(3, 8)
        self.diversao -= random.randint(5, 10)
        self.higiene -= random.randint(2, 5)
        self.checar_estado()

def simular_jogo():
    nome = input("Digite o nome do seu personagem: ")
    sim = Sim(nome)

    while sim.vivo:
        sim.dias_sobrevividos += 1
        print(f"\n=== Dia {sim.dias_sobrevividos} ===")
        sim.mostrar_status()
        input("Pressione ENTER para continuar para a próxima ação...")

        print("\nEscolha uma ação:")
        print("1. Comer")
        print("2. Dormir")
        print("3. Tomar banho")
        print("4. Trabalhar")
        print("5. Assistir TV")
        print("6. Comprar item")
        print("0. Sair do jogo")

        escolha = input("Ação (0-6): ").strip()

        if escolha == "1":
            sim.comer()
        elif escolha == "2":
            sim.dormir()
        elif escolha == "3":
            sim.tomar_banho()
        elif escolha == "4":
            sim.trabalhar()
        elif escolha == "5":
            sim.assistir_tv()
        elif escolha == "6":
            sim.comprar_item()
        elif escolha == "0":
            print(f"\n👋 Até logo, {sim.nome}!")
            break
        else:
            print("Escolha inválida. Nada aconteceu.")

        sim.passar_tempo()
        time.sleep(1)

    # Exibir resumo de vida ao final
    print("\n📜 Resumo da vida de", sim.nome)
    print(f"- Dias vividos: {sim.dias_sobrevividos}")
    print(f"- Dinheiro final: R${sim.dinheiro}")
    if sim.motivo_morte:
        print(f"- Causa da morte: {sim.motivo_morte}")
    else:
        print("- Saiu do jogo antes de morrer.")
    input("\nPressione ENTER para sair...")

simular_jogo()
