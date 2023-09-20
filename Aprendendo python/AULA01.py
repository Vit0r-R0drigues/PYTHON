import random
from random import randint
import math
#import pygame
#import time
from datetime import date

#import emoji

#import mysql

'''print(emoji.emojize("ola, mundo :earth_americas:", language='alias'))'''


# Exercicios
'''print("Qual o valor da base de um triangulo?")

base = input('valor da base? ')
altura = input('valor da altura? ')
area = float(base) * float(altura)

print(f'a base do triangulo medir exatamente {area} ')

# base de um quadrado
print('Qual a area de um quadrado? ')

lado1 = input('valor do lado 1: ')
lado2 = input('valor do lado 2: ')
area = float(lado1) * float(lado2)

print(f'A area do quadrado equivale a: {area}')'''

# valor do produto com desconto
'''x = 1000
print(f'o valor do produto é {x}')
z = 10/100
print(f'o valor que do desconto sera de {z}')
w = (z) * (x)
print(f'o valor do desconto sera de {w}')'''

'''a = int(input('Qual a sua idade?'))

if (a <= 16):
    print('Voce é jovem')
elif (a == 16 < 18):
    print('voce é Emancipado')
else:
    print('voce é Adulto')
print('fora do bloco')'''

'''nome = input('qual o seu nome ?')
sobrenome = input('Qual seu sobrenome ?')
print(f'Seja Bem vindo(a), {nome}{sobrenome}')

dia = input('Qual o dia do seu nascimento ?')
mês = input('Qual o mes do seu nascimento ?')
ano = input('Qual o ano do seu nascimento ?')
print(f'ola {nome}{sobrenome} voce nasceu no dia {dia} do mês {mês} de {ano} ')'''

'''a = input('Digite algo: ')
print('O tipo primitivo deste valor é', type(a))
print('Tem espaços ?', a.isspace())
print('É um numero ?', a.isnumeric())
print('É alfabetico ?', a.isalpha())
print('É alfanumerico', a.isalnum())
print('É maiucula ?', a.isupper())
print('É minuscula ?', a.islower())
print('Está capitalizada ?', a.istitle())'''

'''n = int(input('Digite um numero: '))
d = n * 2
t = n * 3
r = n ** (1/2)
print(f'O dobro de {n} é {d}\n o seu triplo é {t}\n e a sua raiz quadrada é {r} {:.2f}.')'''

'''n = float(input('Qual a sua nota na AV1: '))
n2 = float(input('Qual a sua nota na AV2: '))
a = (n + (n2 * 2))//3
print(f'A media do aluno é {a}')'''

'''n = int(input('Qual o valor desta parede em metros ?'))
c = n * 100
m = n * 1000
print(f'o valor em centimentros desta parede é {c}\ne em milimetros é {m}')'''

'''n = int(input('Digite um numero para a tabuada: '))
print(f'{n} x { 1} = {n*1}')
print(f'{n} x { 2} = {n*2}')
print(f'{n} x { 3} = {n*3}')
print(f'{n} x { 4} = {n*4}')
print(f'{n} x { 5} = {n*5}')
print(f'{n} x { 6} = {n*6}')
print(f'{n} x { 7} = {n*7}')
print(f'{n} x { 8} = {n*8}')
print(f'{n} x { 9} = {n*9}')
print(f'{n} x {10} = {n*10}')
n2 = int(input('Digite outro numero: '))
print('{} x {:2} = {}'.format(n2, 1, n2*1))
print('{} x {:2} = {}'.format(n2, 2, n2*2))
print('{} x {:2} = {}'.format(n2, 3, n2*3))
print('{} x {:2} = {}'.format(n2, 4, n2*4))
print('{} x {:2} = {}'.format(n2, 5, n2*5))
print('{} x {:2} = {}'.format(n2, 6, n2*6))
print('{} x {:2} = {}'.format(n2, 7, n2*7))
print('{} x {:2} = {}'.format(n2, 8, n2*8))
print('{} x {:2} = {}'.format(n2, 9, n2*9))
print('{} x {} = {}'.format(n2, 10, n2*10))'''

'''dinheiro_disponivel = float(input('Quanto de dinheiro você tem disponível para trocar no cambio ? R$'))
dollar = 3.27
print('Com esse valor em reis R${:.2f} disponível se convertemos em dollar que está custando RS${:.2f} você terá US${:.2f} dolares '
.format( dinheiro_disponivel, dollar, dinheiro_disponivel/dollar))'''

'''base = input('Qual o valor da base? m²: ')
altura = input('Qual a altura da parede ? m²: ')
area = float(base) * float(altura)
tinta = 2
print('O valor da da area entao sera de {} x {} = {}'.format(base, altura, area))
print('Se a cada litro de tinta pintamos {}M², a quantidade de tinta que precisaremos para pintar está parede será de: {:.0f}L '.format(tinta, tinta*area))'''

'''preço = float(input('Qual o preço deste determinado produto ? R$: '))
a_prazo = preço
a_vista = preço * 0.05
print('O preço da mercadoria a vista será de {}R$ com 5% de desconto que da {}R$.\nE o preço da mercadoria a prazo será de {}R$'.format(preço, preço - a_vista, a_prazo))'''

'''salario = float(input('Qual o valor do do salario minimo 2022: R$ '))
aumento = salario * 7.425743/100
aliquota = aumento / salario * 100
print('O salario minimo de 2022 é de {}R$, já o salario minimo de 2023 é de {}R$, tendo assim  um reajuste de {:.2f}%'.format(salario, salario + aumento, aliquota ))'''

'''c = float(input('Digite a temperatura em: ºC'))
f = ((9 * c) / 5) + 32
k = c + 213
print('A temperatura em graus Celsius é de {}ºC, convetendoem Fahrenheit é de {}ºF, e covertendo em Kelvin é de {} '.format(c, f, k))'''

'''dias = int(input('Qual a quantidades de dias que você alugou o carro ? '))
km = float(input('Qual a quantidade de Quilometros que o carro rodou ?'))
por_dia = 60
por_km = 0.15
aluguel = (dias * por_dia) + (km * por_km)
print('O preço pelo aluguem do carro sera a quantidade de dias mutiplicado pelo valod da diaria  que custa {}R$ \ne a quantidade de quilometros rodados que foi de {}km, onde cada km custa {}R$\no preço total do aluguel é de {}R$'.format(por_dia, km, por_km, aluguel ))'''

'''num = float(input('Digite um numero quebrado na tela: '))
trans = math.trunc(num)
print('O numero real é {} e sua parte inteiro é {} '.format(num, trans))'''

'''cao = float(input('Digite o valor do cateto oposto: '))
caa = float(input('Digite o valor do cateto adjecente: '))
h = (cao**2) + (caa**2)
hipotenusa = math.sqrt(h)
teste = math.hypot(cao, cao)
print('O valor da hipotenusa é igual a soma do cateto oposto² que é {} mais o adjecente² {} que da igual {}, \nelevado a sua raiz quadrada no qual o valor da hipotenusa fica {}'.format(cao, caa, h, hipotenusa))
print('O valor da hipotenusa é {}'.format(teste))'''


'''an = float(input('Digito o valor do angulo: '))
di = float(input('Digite o valor da distancia: '))
tangente = math.tan(math.radians(an))
seno = math.sin(math.radians(an))
cosseno = math.cos(math.radians(an))
print('O valos da tangente de um angulo de {}º graus é de {:.2f}'.format(an, tangente))
print('O valor de um seno de um angulo de {}º graus  é  de {:.2f}'.format(an, seno))
print('O valor de um cosseno de um angulo de {}º graus é de {:.2f}'.format(an, cosseno))
print('Para quem está a uma distancia de {}km em um angulo de {}º graus estaria enxergando o balao a distancia de {:.3f}'.format(di, an, tangente * di))'''

'''a1 = input('nome do aluno: ')
a2 = input('nome do aluno: ')
a3 = input('nome do aluno: ')
a4 = input('nome do aluno: ')
a5 = input('nome do aluno: ')
lista = [ a1, a2, a3, a4, a5 ]
premiado = random.choice(lista)
print('O aluno premiado é {}'.format(premiado))'''

'''a1 = input('aluno 1: ')
a2 = input('aluno 2: ')
a3 = input('aluno 3: ')
a4 = input('aluno 4: ')
lista = [a1, a2, a3, a4]
random.shuffle(lista)
print('a ordem de apresentaçao do trabalho é {}'.format([lista]))'''

'''nome  = input('Digite seu nome completo: ').strip()
print('Analisando seu nome...')
print('Seu nome em letras maiusculas é {}'.format(nome.upper()))
print('Seu nome em letras minusculas é {}'.format(nome.lower()))
print('Seu nome tem {} letras '.format(len(nome) - nome.count(' ') ))
#print('Seu primeiro nome tem {} letras'.format(nome.find('')))
separado = nome.split()
print('Seu primeiro nome tem {} e tem {} letras'.format(separado[0], len(separado[0])))'''


'''num = int(input('Digite um numero: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisandow seu {}'.format(num))
print('Unidades: {}'.format(u))
print('Dezena {}'.format(d))
print('Centena {} '.format(c))
print('Milhar {} '.format(m))'''

'''cid = str(input('Em qual cidade você nasceu ? ')).strip()
print(cid[:5].upper() == 'SANTO')'''

'''nome = str(input('Qual seu nome ? ')).strip()
print('seu nome tem silva ? {} '.format('silva' in nome.lower()))'''


'''num = int(input('Digite um numero: '))
print('processando....')
sleep(3)
pc = random.randint(0,5)
if (num < pc):
    print('Parabens você ganhou {}'.format(emoji.emojize(":1st_place_medal:")))
    print('-=-' * 25)
elif (num == pc):
    print('Foi empate vamos novamente {} que vença o melhor {}'.format(emoji.emojize(':grin:'), emoji.emojize(':smirk:')))
    print('-=-' * 25)
else:
    print('A maquina ganhou,{} mas sorte na proxima {}'.format(emoji.emojize(':1st_place_medal:'), emoji.emojize(':wink:')))
    print('-=-' * 25)'''


'''velocidade =  int(input('qual a velocidade de seu carro ao utrapassar a br 116: '))
if (velocidade <= 80):
    print('Parabens você está dirigindo a {}km/h a uma velocidade abaixo ou igual ao permitido 80km/h  bem, continue com cuidade '.format(velocidade))
elif (velocidade > 80):
    multa = (velocidade - 80) * 7
    print('Pela sua impudência no volante viajando a uma velocidade de {}km/h levou uma multa de {} para que da proxima vez nao utrapasse o limite permitido.'.format(velocidade, multa,))'''


'''for Regressiva in range(10, -1, -1):
    print(Regressiva)
    time.sleep(1)
print('BUM BUM ACABOU!!!!')'''


'''for par in range(0, 51,):
    if par % 2 == 0:
        print(par, end=' ')
        time.sleep(0.5)'''


'''soma = 0
cont = 0
for impar in range(1, 1001, 2):
    if impar % 3 == 0:
        cont = cont + 1
        soma = soma + impar
print('A soma de todos os {} valores impares de 1 ate 500 é {}'.format(cont, soma))'''


'''n = int(input('Digite um numero para a tabuada: '))
for tabu in range(1, 11):
    print(f'{n} x {tabu} = {n * tabu}')'''


'''cont = 0
soma = 0
for num in range(1, 7):
    n = int(input('Digite u numero: '))
    if n % 2 == 0:
        soma += n
        cont += 1
print('A soma de todos os {} numeros pares é: {}'.format(cont, soma))'''

'''num = int(input('Digite um numero: '))
tot = 0
for prim in range(1, num +1):
    if num % prim == 0:
        tot += 1
        print('\033[32m', end=' ')
    else:
        print('\033[31m', end=' ')
    print('{}'.format(prim), end=' ')
print('\n\033[mO numero {}  foi divisivel {} vezes'.format(num, tot))
if tot == 2:
    print('\033[36mO numero {} é PRIMO'.format(num))
else:
    print('\033[31mO numero {} não é PRIMO'.format(num))'''


'''frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for poli in range(len(junto) -1, -1, -1):
    inverso += junto[poli]
print(junto, inverso)
if inverso == frase:
    print('\033[36mA frase é um palindro')
else:
    print('\033[31mA frase não é um palindro')'''

#IMC
'''atual = date.today().year
idade = 0
idadeatual = 0
maioridade = 0
menoridade = 0
idosidade = 0
maiorpeso = 0
menorpeso = 0
IMC = 0
IGC = 0
for id in range(1, 2):
    print('---- {}º Pessoal ----'.format(id))
    nome = str(input('Qual seu nome ? ')).strip().upper()
    sexo = str(input('Qual seu sexo: ')).strip()
    nasc = int(input('Em que ano você nasceu ? '))
    peso = float(input('Qual seu peso: '))
    altura = float(input('Qual sua altura: '))
    if 'M' or 'm':
        sexo = 1
    elif 'F' or 'f':
        sexo = 0
    idade += nasc
    idadeatual = atual - nasc
    IMC = peso / altura * altura
    IGC = (1.20 * IMC) + (0.23 * idadeatual) - (10.8 * sexo) - 5.4
    if idade <=18:
        menoridade += 1
    elif idade <= 60:
        maioridade +=1
    else:
        idosidade += 1
    if id == 1:
        maiorpeso = peso
        menorpeso = peso
    else:
        if peso > maiorpeso:
            maiorpeso = peso
        if peso < menorpeso:
            maiorpeso = peso

print('Olá {} prazer em te conhecer\n você tem {} ano(s) de idade\n sua altura é de {}\n e seu peso é de {}Kg\n Você é {}.'.format(nome, idadeatual, altura, peso, idade))
print('{}\n seu indice de gordura corporal é {}\n seu indice de massa corporal é {}'.format(nome, IGC, IMC)'''



'''Nome = str(input('Digite seu nome: ')).strip().upper()
Idade = str(input('Digite sua idade: ')).strip().upper()
Sexo = str(input('Digite seu Sexo [M/F]: ')).strip().upper()
while Sexo not in 'MmFf':
    Sexo = str(input('Desculpe dados invalidos tente novamente seu Sexo [M/F]: ')).strip().upper()
if Sexo == 'M' or 'm':
    Sexo = 'Masculino'
elif Sexo == 'F' or 'f':
    Sexo = 'Feminino'
print('-=-' * 25)
print(f'Seu nome é {Nome}, Voce tem {Idade} anos e seu Sexo é {Sexo}')
print('-=-' * 25)'''


#Jogo
'''computador = randint (0,10)
emoj = emoji.emojize(':rosto_sorridente_com_olhos_sorridentes:',language = 'pt')
Ganhador = emoji.emojize(':medalha_de_ouro:',language = 'pt')
Legal = emoji.emojize(':rosto_abraçando:',language = 'pt')
Jogo = emoji.emojize(':caça-níquel:',language = 'pt')
Quase = emoji.emojize(':rosto_fazendo_sinal_de_silêncio:',language = 'pt')
PC = emoji.emojize(':computador_de_mesa:',language = 'pt')
print(f'Sou seu Computador{PC}, e voce esta no jogo{Jogo} da advinhação, vamos jogar {emoj}')
print(f'Será que você me ganha ?{emoj}')
Acertou = False
Palpite = 0
while not Acertou:
    Jogador = int(input('Qual seu palpite: '))
    Palpite += 1
    if Jogador == computador:
        Acertou = True
    else:
        if Jogador < computador:
            print(f'Mais.. tente novamente {Quase}')
        elif Jogador > computador:
            print(f'Menos.. tente novamente {Quase}')
print(f'Parabens {Ganhador} voce acertou com {Palpite} Palpites{emoj}')'''


''''num = tentativas = soma = 0
num = int(input('Digite o codigo [999 para parar]: '))
while num != 999:
    tentativas += 1
    soma += num
    num = int(input('Digite o codigo [999 para parar]: '))
print(f"O numero de tentaivas foi de {tentativas} para encerrar o programa, e a soma deste numeros foi de {soma} ")'''



'''n = total = cont = 0
while n != 999:
    n = int(input('Digite um número inteiro ou 999 para parar: '))
    if n != 999:
        total += n
        cont += 1
print('Foram digitados {} números e a soma entre eles foi {}'.format(cont, total))'''


'''txtInicio = '\033[35;41;1m'
txtFim = '\033[35;47m'
txtSem = '\033[0m'
txtNegSub = '\033[4;1m'

print( txtNegSub,' Vamos ao Valores', txtNegSub)

Quantidade = 0
opção = 'S'
total = 0
media = 0
soma = menor = maior = 0
while opção not in 'N':
    if opção == 'S':
        num = int(input('Tecle um numero: '))
        soma += num
        Quantidade += 1
        if Quantidade == 1:
            maior = menor = num
        else:
            if num > maior:
                maior = num
            if num < menor:
                menor = num
    opção = str(input('Dseja continuar [S/N] ')).strip().upper()
media += soma / Quantidade
print(f'Voce digitou {Quantidade}, que somados dao um total de {soma}, com media total de {media}\n onde o maior valor é {maior} e o menor valor é {menor} ')'''


'''num = tentativas = soma = 0
while True:
    num = int(input('Digite o codigo [999 para parar]: '))
    if num == 999:
        break
    tentativas += 1
    soma += num
print(f'O numero de tentaivas foi de {tentativas} para encerrar o programa, e a soma deste numeros foi de {soma}')'''


'''print('=' * 25)
print('Vamos a tabuada.....')
print('=' * 25)
time.sleep(3)
print('=' * 25)
print('Qual tabuada voce vai escolher ?...')
print('=' * 25)
time.sleep(3)
while True:
    tabu = int(input('Digite um numero para calcularmos a sua tabuada: '))
    if tabu < 0:
        break
    print(f'A sua tabuada escolhida foi de numero {tabu} que fica igual a:')
    print('===' * 25)
    print('Calculando......')
    time.sleep(2)
    for c in range(1, 11):
        print('===' * 25)
        print(f'{c} X {tabu} = {c * tabu}')
        print('===' * 25)
print('Tabuada encerrada.')'''


'''while True:
    jogador =  int(input('Pense em um numero: '))
    print('***'* 30)
    print('Computador pensando..... hum.. já sei ...')
    print('***' * 30)
    computador = random.randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PpIi':
        tipo = str(input('Impar ou Par escolha sua Opção: P/I -->  '))
    print(f'Você jogou {jogador} e o computador {computador} o total foi de {total}')
    print('DEU PAR' if total % 2 == 0 else 'DEU IMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Parabens voce ganhou deu PAR')
        else:
            print('Você perdeu, mais sorte na proxima!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Parabens voce ganhou deu PAR')
        else:
            print('Você perdeu, mais sortes na proxima!')
            break
        print('Vamos jogar nvamente.....')'''


while True:
    nome = str(input)