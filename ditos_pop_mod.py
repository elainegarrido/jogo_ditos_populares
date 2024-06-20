def main():
    frases = {
        1: "Medir duas vezes, cortar uma",
        2: "Devagar se vai ao longe",
        3: "Cada macaco no seu galho",
        4: "Não se deve colocar todos os ovos na mesma cesta",
        5: "Casa de ferreiro, espeto de pau",
        6: "Água mole em pedra dura, tanto bate até que fura",
        7: "Mais vale um pássaro na mão do que dois voando",
        8: "Quem não arrisca, não petisca",
        9: "De grão em grão, a galinha enche o papo",
        10: "Quem tem pressa come cru"
    }

    significados = {
        1: "Esse dito enfatiza a importância de verificar e validar dados e modelos antes de tomar decisões baseadas neles, evitando erros e desperdícios.",
        2: "Reflete a ideia de que processos de modelagem e planejamento cuidadosos, ainda que lentos, tendem a resultar em sucesso a longo prazo.",
        3: "Destaca a importância de cada variável e parâmetro estar em seu devido lugar em um modelo, para garantir a precisão e relevância dos resultados.",
        4: "Relaciona-se à diversificação de modelos e estratégias para reduzir riscos e incertezas.",
        5: "Lembra que mesmo os especialistas em modelagem podem cometer erros ou negligenciar práticas básicas.",
        6: "Enfatiza a importância da persistência na validação e refinamento de modelos até que se tornem robustos e precisos.",
        7: "Sublinha a importância de trabalhar com dados e modelos que são concretos e verificáveis, em vez de confiar em previsões incertas.",
        8: "Incentiva a inovação e a experimentação na modelagem, mesmo sabendo que podem haver falhas ou incertezas no processo.",
        9: "Representa a construção gradual de um modelo detalhado e preciso a partir da coleta de dados e pequenos insights.",
        10: "Adverte contra a pressa na criação de modelos, destacando a necessidade de um desenvolvimento e validação meticulosos."
    }

    print("Escolha uma das frases abaixo digitando o número correspondente:")
    for key, value in frases.items():
        print(f"{key}. {value}")

    escolha = int(input("\nDigite o número da frase escolhida: "))

    if escolha in significados:
        print(f"\nSignificado: {significados[escolha]}")
    else:
        print("Escolha inválida. Tente novamente.")

if __name__ == "__main__":
    main()
