quantidade = 0
quantidadeOtimo = 0
quantidadeBom = 0
quantidadeRegular = 0
quantidadePessimo = 0
idadevelha = 0
avaliacaovelha = 0
idadenova = 0
avaliacaonova = 0

while (True):
    avaliacao = int(input("informe sua avaliacao (1-otimo 2-bom 3-regular 4-pessimo):"))
    idade = int(input ("informe sua idade:"))

    quantidade += 1

    if avaliacao == 1:
        quantidadeOtimo += 1

    if avaliacao == 2:
        quantidadeBom += 1

    if avaliacao == 3:
        quantidadeRegular += 1

    if avaliacao == 4:
        quantidadePessimo += 1      

    if (idade > idadevelha):
        idadevelha = idade
        avaliacaovelha = avaliacao

    if (idade < idadenova) or (idadenova == 0)
        idadenova = idade
        avaliacaonova = avaliacao      

    continua = int(input ("deseja continuar? (1-sim 2-nao):"))
    if continua == 2:
        break

print ("total de respondentes: ", quantidade)
print ("total de respostas otimo", quantidadeOtimo)
print ("total de respostas bom", quantidadeBom)
print ("total de respostas regular", quantidadeRegular)
print ("total de respostas pessimo", quantidadePessimo)
print ("o respondente mais velho tem:", idadevelha)
print ("a resposta do respondente mais velho foi:", avaliacaovelha)
print ("o respondente mais novo tem:", idadenova)
print ("a resposta do respondente mais novo foi:", avaliacaonova)