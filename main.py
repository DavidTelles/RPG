from combate import atacar

class Jogador :
    def __init__(self, nome, hp):
        self.nome = nome
        self.hp = hp
        self.power = 0
        self.danobase = 0 + self.power

while True:
    qtd_jogadores = int (input ( "Quantos Players irão jogar? (2 - 4) : " ))
    if qtd_jogadores == 2 or qtd_jogadores == 3 or qtd_jogadores == 4 :
        break
    else : 
        print(f"Valor {qtd_jogadores} invalido!")

jogadores : list[Jogador] = []
hp = 100

for i in range (qtd_jogadores) :
    nome = str (input ( f"Nome do jogador {i+1} : " ))
    jogadores.append(Jogador(nome, hp))

jogador_atual = 0
while True:
    print(
        f"""
    vez de {jogadores[jogador_atual].nome}

    [1] Atacar
    [2] Inventario
    [3] Loja

    [0] Passar a vez
    """
    )

    opc = int (input("Sua opção : "))

    if opc == 1 :
        atacar(jogadores, jogador_atual, qtd_jogadores)
        jogador_atual = (jogador_atual + 1) % qtd_jogadores

    if opc == 2 :
        pass

    if opc == 3 :
        pass

    if opc == 0 :
        break