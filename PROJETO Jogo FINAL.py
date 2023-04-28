import time
respostas = []
gabarito = ["C", "B", "A", "B", "D", "B", "D", "D", "C", "A"]
global pontos
pontos = 0
print("BEM VINDO, ESSE É O NOSSO JOGO SOBRE PANDEMIA CRIADO NA LINGUAGEM PYTHON")

def pergunta1():
    print("1) Qual destes NÃO é sintoma de Covid-19?")
    print(" a) Febre\n b) Tosse Seca\n c) Visão Embaçada\n d) Cansaço")
    resposta1 = str(input("Qual é a opção correta? ")).upper()
    while resposta1 != "A" and resposta1 != "B" and resposta1 != "C" and resposta1 != "D":
        resposta1 = str(input("Qual é a opção correta? ")).upper()
    respostas.append(resposta1)
    print("")

def correcao1():
    global pontos
    time.sleep(2)
    if respostas[0] == gabarito[0]:
        pontos += 5
        print("VOCÊ ACERTOU, PARÁBENS!")
        print("A razão é: Os sintomas de COVID-19 variam de paciente para paciente, pois cada organismo reage de uma forma diferente à infecção.\n" 
              "Podem apresentar sintomas leves como tosse, cansaço, dores musculares ou corporais, dor de garganta, congestão nasal, febre alta, "
              "perda do olfato e paladar.")
    else:
        pontos += 0
        print("Você errou, na próxima você consegue")
        print("A razão é: Os sintomas de COVID-19 variam de paciente para paciente, pois cada organismo reage de uma forma diferente à infecção."
            "Podem apresentar sintomas leves como tosse, cansaço, dores musculares ou corporais, dor de garganta, congestão nasal, febre alta, "
            "perda do olfato e paladar.")
    time.sleep(4)
    print("")

def pergunta2():
    print("2)  O que é mais eficiente para remover o coronavírus das mãos?")
    print(" a) Álcool em Gel\n b) Água e Sabão\n c) Lenço Umedecido\n d) Detergente")
    resposta1 = str(input("Qual é a opção correta? ")).upper()
    while resposta1 != "A" and resposta1 != "B" and resposta1 != "C" and resposta1 != "D":
        resposta1 = str(input("Qual é a opção correta?")).upper()
    respostas.append(resposta1)
    print("")

def correcao2():
    global pontos
    time.sleep(2)
    if respostas[1] == gabarito[1]:
        pontos += 10
        print("VOCÊ ACERTOU, PARÁBENS!")
        print("A razão é: Água e sabão é a combinação mais eficiente porque conseguem deixar o vírus inativo. Na falta de água e sabão deve-se usar o álcool em gel.")
    else:
        pontos += 0
        print("Você errou, na próxima você consegue")
        print("A razão é: Água e sabão é a combinação mais eficiente porque conseguem deixar o vírus inativo. Na falta de água e sabão deve-se usar o álcool em gel.")
    time.sleep(4)
    print("")

def pergunta3():
    print("3) Qual é o órgão do corpo que o coronavírus mais ataca?")
    print(" a) Pulmão\n b) Coração\n c) Fígado\n d) Estômago")
    resposta1 = str(input("Qual é a opção correta? ")).upper()
    while resposta1 != "A" and resposta1 != "B" and resposta1 != "C" and resposta1 != "D":
        resposta1 = str(input("Qual é a opção correta? ")).upper()
    respostas.append(resposta1)
    print("")


def correcao3():
    global pontos
    time.sleep(2)
    if respostas[2] == gabarito[2]:
        pontos += 5
        print("VOCÊ ACERTOU, PARÁBENS!")
        print("A razão é: Por começar nas vias aéreas, quem mais sofre é o pulmão (há evidência que outros órgãos, como o coração, também sofrem com o patógeno).")
    else:
        pontos += 0
        print("Você errou, na próxima você consegue")
        print("A razão é: Por começar nas vias aéreas, quem mais sofre é o pulmão (há evidência que outros órgãos, como o coração, também sofrem com o patógeno). ")
    time.sleep(4)
    print("")

def pergunta4():
    print("4) Como a COVID-19 é transmitida?")
    print(" a) Picada de mosquito\n b) Inalação de gotículas de saliva contaminda\n c) Comida estragada\n d) Mordida de morcedo contaminado")
    resposta1 = str(input("Qual é a opção correta? ")).upper()
    while resposta1 != "A" and resposta1 != "B" and resposta1 != "C" and resposta1 != "D":
        resposta1 = str(input("Qual é a opção correta?")).upper()
    respostas.append(resposta1)
    print("")

def correcao4():
    global pontos
    time.sleep(2)
    if respostas[3] == gabarito[3]:
        pontos += 5
        print("VOCÊ ACERTOU, PARÁBENS!")
        print("A razão é: A transmissão da COVID-19 se dá por secreções contaminadas, como gotículas de saliva, espirro, tosse e catarro.\n"
              " Deve-se evitar o contato pessoal próximo, como toque ou aperto de mão, e o toque em objetos ou superfícies contaminados,\n"
              " seguido de contato com a boca, o nariz ou os olhos")
    else:
        pontos += 0
        print("Você errou, na próxima você consegue")
        print("A razão é: A transmissão da COVID-19 se dá por secreções contaminadas, como gotículas de saliva, espirro, tosse e catarro.\n"
              " Deve-se evitar o contato pessoal próximo, como toque ou aperto de mão, e o toque em objetos ou superfícies contaminados, \n"
              "seguido de contato com a boca, o nariz ou os olhos")
    time.sleep(4)
    print("")

def pergunta5():
    print("5) No Brasil, qual é o período de segurança de quarentena para que pessoas expostas não transmitam a COVID-19?")
    print(" a) 5 dias\n b) 10 dias\n c) 7 dias\n d) 14 dias")
    resposta1 = str(input("Qual é a opção correta? ")).upper()
    while resposta1 != "A" and resposta1 != "B" and resposta1 != "C" and resposta1 != "D":
        resposta1 = str(input("Qual é a opção correta?")).upper()
    respostas.append(resposta1)
    print("")

def correcao5():
    global pontos
    time.sleep(2)
    if respostas[4] == gabarito[4]:
        pontos += 10
        print("VOCÊ ACERTOU, PARÁBENS!")
        print("A razão: No Brasil, a regra ainda é a quarentena de 14 dias, embora alguns municípios estejam cogitando reduzir para dez dias.\n"
              " Em países como a Suíça, infectados com sintomas leves são liberados do isolamento após sete dias apenas")
    else:
        pontos += 0
        print("Você errou, na próxima você consegue")
        print("A razão é: No Brasil, a regra ainda é a quarentena de 14 dias, embora alguns municípios estejam cogitando reduzir para dez dias.\n"
              " Em países como a Suíça, infectados com sintomas leves são liberados do isolamento após sete dias apenas")
    time.sleep(4)
    print("")


def pergunta6():
    print("6) Os trabalhadores e/ou familiares com suspeita de infecção devem adotar qual procedimento?")
    print(" a) Procurar Pronto Socorro ou laboratórios para realização de exames.\n b) Fazer uso da máscara, manter distanciamento social e entrar em contato com os serviços de saúde referenciados pelos órgãos oficiais.\n c) Tomar medicação por conta própria.\n d) Não comunicar para ninguém.")
    resposta1 = str(input("Qual é a opção correta? ")).upper()
    while resposta1 != "A" and resposta1 != "B" and resposta1 != "C" and resposta1 != "D":
        resposta1 = str(input("Qual é a opção correta?")).upper()
    respostas.append(resposta1)
    print("")

def correcao6():
    global pontos
    time.sleep(2)
    if respostas[5] == gabarito[5]:
        pontos += 10
        print("VOCÊ ACERTOU, PARÁBENS!")
        print("A razão: O primeiro passo é procurar imediatamente por atendimento médico e fazer o teste no período certo.\n"
              " Negligenciar esses cuidados podem prejudicar a sua própria saúde e colocar em risco a saúde das pessoas que estão à sua volta.")
    else:
        pontos += 0
        print("Você errou, na próxima você consegue")
        print("A razão é: O primeiro passo é procurar imediatamente por atendimento médico e fazer o teste no período certo.\n"
              " Negligenciar esses cuidados podem prejudicar a sua própria saúde e colocar em risco a saúde das pessoas que estão à sua volta.")
    time.sleep(4)
    print("")

def pergunta7():
    print("7) Quais são as Condições Individuais de saúde consideradas situações de alto risco para a transmissão do coronavírus?")
    print(" a) Anemia, disfagia, doença celíaca, intolerância a lactose.\n b) Obesidade, gastroenterite, alcoolismo, apneia do sono.\n c) Doenças psiquiátricas, doença de Parkinson, síndrome de Down\n d) Diabetes, hipertensão, problemas respiratórios, doenças cardiovasculares, pacientes imunossuprimidos")
    resposta1 = str(input("Qual é a opção correta? ")).upper()
    while resposta1 != "A" and resposta1 != "B" and resposta1 != "C" and resposta1 != "D":
        resposta1 = str(input("Qual é a opção correta?")).upper()
    respostas.append(resposta1)
    print("")

def correcao7():
    global pontos
    time.sleep(2)
    if respostas[6] == gabarito[6]:
        pontos += 10
        print("VOCÊ ACERTOU, PARÁBENS!")
        print("A razão e: O fato é que as pessoas portadoras de doenças crônicas têm uma probabilidade muito maior de apresentar sintomas graves da Covid-19, que podem evoluir para internação ou óbito.\n"
              " Na prática isso significa que a Covid-19 é mais perigosa para portadores de doenças crônicas como hipertensão, cardiopatias, doenças renais e respiratórias.")
    else:
        pontos += 0
        print("Você errou, na próxima você consegue")
        print("A razão é: o fato é que as pessoas portadoras de doenças crônicas têm uma probabilidade muito maior de apresentar sintomas graves da Covid-19, que podem evoluir para internação ou óbito.\n"
              " Na prática isso significa que a Covid-19 é mais perigosa para portadores de doenças crônicas como hipertensão, cardiopatias, doenças renais e respiratórias.")
    time.sleep(4)
    print("")

def pergunta8():
    print("8) Qual o tempo de vida do vírus fora do corpo humano (no ar)?")
    print(" a) Cerca de 24 horas\n b) Mais 96 horas \n c) 10 horas \n d) Cerca de 1 ou 2 horas")
    resposta1 = str(input("Qual é a opção correta? ")).upper()
    while resposta1 != "A" and resposta1 != "B" and resposta1 != "C" and resposta1 != "D":
        resposta1 = str(input("Qual é a opção correta?")).upper()
    respostas.append(resposta1)
    print("")

def correcao8():
    global pontos
    time.sleep(2)
    if respostas[7] == gabarito[7]:
        pontos += 10
        print("VOCÊ ACERTOU, PARÁBENS!")
        print("A razão é: Os pesquisadores constataram que o coronavírus pode sobreviver até 72 horas (ou 3 dias) em superfícies como o plástico ou o aço inoxidável.\n"
              " Em contrapartida, quando dispersos no ar ou na poeira, o tempo de existência varia entre 40 minutos e 2h e 30 minutos.")
    else:
        pontos += 0
        print("Você errou, na próxima você consegue")
        print("A razão é: Os pesquisadores constataram que o coronavírus pode sobreviver até 72 horas (ou 3 dias) em superfícies como o plástico ou o aço inoxidável.\n"
              " Em contrapartida, quando dispersos no ar ou na poeira, o tempo de existência varia entre 40 minutos e 2h e 30 minutos.")
    time.sleep(4)
    print("")

def pergunta9():
    print("9) Quais agentes químicos NÃO podem ser usados para o processo de desinfecção do coronavírus?")
    print(" a) Hipoclorito de sódio\n b) Álcoois etlíco e isopropílico\n c) Água Oxigenada\n d) Sabão")
    resposta1 = str(input("Qual é a opção correta? ")).upper()
    while resposta1 != "A" and resposta1 != "B" and resposta1 != "C" and resposta1 != "D":
        resposta1 = str(input("Qual é a opção correta?")).upper()
    respostas.append(resposta1)
    print("")

def correcao9():
    global pontos
    time.sleep(2)
    if respostas[8] == gabarito[8]:
        pontos += 20
        print("VOCÊ ACERTOU, PARÁBENS!")
        print("A razão é: Especialistas, no entanto, afirmam não haver recomendação oficial, por enquanto,\n"
              " para uso de água oxigenada nem evidências suficientes de que ele proteja contra o vírus.\n"
              " O uso de água oxigenada para higiene pessoal é contraindicado.")
    else:
        pontos += 0
        print("Você errou, na próxima você consegue")
        print("A razão é: Especialistas, no entanto, afirmam não haver recomendação oficial, por enquanto,\n"
              " para uso de água oxigenada nem evidências suficientes de que ele proteja contra o vírus.\n"
              " O uso de água oxigenada para higiene pessoal é contraindicado.")
    time.sleep(4)
    print("")

def pergunta10():
    print("10) Quando falamos em transmissão de COVID-19 por assintomáticos,\n qual é o percentual de contaminações pelo novo coronavírus que acontece a partir de pessoas sem sintomas?")
    print(" a) 59%\n b) 45%\n c) 20%\n d) 73%")
    resposta1 = str(input("Qual é a opção correta? ")).upper()
    while resposta1 != "A" and resposta1 != "B" and resposta1 != "C" and resposta1 != "D":
        resposta1 = str(input("Qual é a opção correta?")).upper()
    respostas.append(resposta1)
    print("")

def correcao10():
    global pontos
    time.sleep(2)
    if respostas[9] == gabarito[9]:
        pontos += 20
        print("VOCÊ ACERTOU, PARÁBENS!")
        print("A razão é: Os resultados de estudos estimam que aproximadamente 59% das infecções são transmitidas por indivíduos assintomáticos,\n"
              " sendo 35% oriundos de casos que ainda desenvolverão quadro clínico e 24% provenientes de pessoas que nunca desenvolvem sintomas ")
    else:
        pontos += 0
        print("Você errou, na próxima você consegue")
        print("A razão é: Os resultados de estudos estimam que aproximadamente 59% das infecções são transmitidas por indivíduos assintomáticos,\n"
              " sendo 35% oriundos de casos que ainda desenvolverão quadro clínico e 24% provenientes de pessoas que nunca desenvolvem sintomas ")
    time.sleep(10)
    print("")

def main():
    pergunta1()
    correcao1()
    pergunta2()
    correcao2()
    pergunta3()
    correcao3()
    pergunta4()
    correcao4()
    pergunta5()
    correcao5()
    pergunta6()
    correcao6()
    pergunta7()
    correcao7()
    pergunta8()
    correcao8()
    pergunta9()
    correcao9()
    pergunta10()
    correcao10()

    print("A sua pontuação foi: ", pontos,"/100")
    print("")
    print("As suas respotas foram:")
    for x in respostas:
        print(x)
    print("")
    print("O gabarito é:")
    for i in gabarito:
        print(i)

main()