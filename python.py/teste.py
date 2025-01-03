somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = 0
mulhermenos20 = 0
for c in range(1, 5):
    nome = str(input(f'Qual o nome da {c} pessoa? '))
    idade = int(input(f'Qual a idade da {c} pessoa? '))
    sexo = str(input(f'Qual o sexo da {c} pessoa? [M/F]?')).upper()
    somaidade += idade
    if sexo in 'M' and maioridadehomem < idade:
        maioridadehomem = idade
        nomevelho = nome
    elif sexo in 'F' and idade < 20:
        mulhermenos20 += 1
