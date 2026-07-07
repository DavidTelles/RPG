def atacar(jogadores, jogador_atual, qtd_jogadores) :
    if qtd_jogadores > 2 : 
        while True :
            for i in range (qtd_jogadores) :
                if i != jogador_atual:
                    print(f"- [{i + 1}] {jogadores[i].nome}")
            alvo = int (input("Quem deseja atacar? : ")) - 1
            if alvo == jogador_atual :
                print("Você não pode se atacar.")
            else :
                break
    else :
        for i in range (qtd_jogadores) : 
            if i != jogador_atual :
                alvo = i
    print(f"{jogadores[jogador_atual].nome} atacou {jogadores[alvo].nome}")