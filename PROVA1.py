quantidade = 0
totalcorazul = 0
totalcorverde = 0
totalcorrosa = 0

idadevelhaazul = 0
idadenovaazul = 0

idadevelhaverde = 0
idadenovaverde = 0

idadevelharosa = 0
idadenovarosa = 0

mascazul = 0
femazul = 0

mascverde = 0
femverde = 0

mascrosa = 0
femrosa = 0




while(True):
    corpreferida = int(input("Qual sua cor favorita? Azul, Verde ou Rosa? (1-Azul 2-Verde 3-Rosa)"))
    idade = int(input("Qual sua idade?"))
    sexo = int(input("Qual seu sexo? (1-M 2-F)"))

    quantidade += 1

    if corpreferida == 1:
        totalcorazul += 1

    if corpreferida == 2:
        totalcorverde += 1
    
    if corpreferida == 3:
        totalcorrosa += 1

    if corpreferida == 1 and (idade > idadevelhaazul):
        idadevelhaazul = idade

    if corpreferida == 2 and (idade > idadevelhaverde):
        idadevelhaverde = idade

    if corpreferida == 3 and (idade > idadevelharosa):
        idadevelharosa = idade

    if corpreferida == 1 and (idade < idadenovaazul) or (idadenovaazul == 0):
        idadenovaazul = idade

    if corpreferida == 2 and (idade < idadenovaverde) or (idadenovaverde == 0):
        idadenovaverde = idade

    if corpreferida == 3 and (idade < idadenovarosa) or (idadenovarosa == 0):
        idadenovarosa = idade

    if corpreferida == 1 and sexo == 1:
        mascazul += 1

    if corpreferida == 1 and sexo == 2:
        femazul += 1

    if corpreferida == 2 and sexo == 1:
        mascverde += 1

    if corpreferida == 2 and sexo == 2:
        femverde += 1

    if corpreferida == 3 and sexo == 1:
        mascrosa += 1

    if corpreferida == 3 and sexo == 2:
        femrosa += 1



    if (input ("Deseja continuar? (S, N)") != "S"):
        break


percentualAzul = (totalcorazul * 100) / quantidade
percentualVerde = (totalcorverde * 100) / quantidade
percentualRosa = (totalcorrosa * 100) / quantidade

print ("Total de respondentes: ", quantidade)
print ("Total de pessoas que preferem a cor Azul: ", percentualAzul)
print ("Total de pessoas que preferem a cor Verde: ", percentualVerde)
print ("Total de pessoas que preferem a cor Rosa: ", percentualRosa)

print ("A idade da pessoa mais velha que prefere a cor Azul: ", idadevelhaazul)
print ("A idade da pessoa mais velha que prefere a cor Verde: ", idadevelhaverde)
print ("A idade da pessoa mais velha que prefere a cor Rosa: ", idadevelharosa)

print ("A idade da pessoa mais nova que prefere a cor Azul: ", idadenovaazul)
print ("A idade da pessoa mais nova que prefere a cor Verde: ", idadenovaverde)
print ("A idade da pessoa mais nova que prefere a cor Rosa: ", idadenovarosa)

print ("Quantidade de pessoas do sexo masculino que preferem a cor Azul: ", mascazul)
print ("Quantidade de pessoas do sexo feminino que preferem a cor Azul: ", femazul)

print ("Quantidade de pessoas do sexo masculino que preferem a cor Verde: ", mascverde)
print ("Quantidade de pessoas do sexo feminino que preferem a cor Verde: ", femverde)

print ("Quantidade de pessoas do sexo masculino que preferem a cor Rosa: ", mascrosa)
print ("Quantidade de pessoas do sexo feminino que preferem a cor Rosa: ", femrosa)