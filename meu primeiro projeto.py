import datetime
import random
nome= 'Gustavo'
idade = 18
empresa = 'LCM'
print('\nOlá me chamo', nome,' tenho ',idade,'anos\nMuito feliz de estar na empresa ',empresa,' para aprender e melhorar minha habilidade!!\nFim do primeiro teste\n' )
#------------------------------------------------------------------------------------------------------------
dia=input('Qual dia que vc nasceu:')
mes= input('Qual mes vc nasceu:')
ano=  input ('Qual ano vc nasceu:')
print('Voce nasceu na data:',dia,'/',mes,'/',ano,'\nFim segundo teste\n')
#------------------------------------------------------------------------------------------------------------
print('oi\n'*5,'\nFim  terceiro teste\n')
#------------------------------------------------------------------------------------------------------------
n1= int( input('Escreva um numero:'))
n2= int(input('Escrva outro numero:'))
s= n1+ n2
m=n1* n2
d=n1/n2
di= n1//n2
pot= n1**n2
print('A soma deu:',s,'\n multiplicação deu:',m,'divisao deu:',d,'\ndivisão inteira deu:',di,'\n e para finalizar a potencia deu:',pot,'\n Fim quarto teste\n')
#------------------------------------------------------------------------------------------------------------

n1=  int(input('Escreva um numero:'))
ant = n1-1
suc= n1+1
print('Seu número escolhido foi{}.Seu antecessor é{}, e seu sucessor é{}'.format(n1,ant,suc),'\nFim do quinto teste\n')
#------------------------------------------------------------------------------------------------------------
idade=int(input('Digite a sua idade atual em anos, para que você possa comprar bebida:'))
if idade>=18:
    print('Você pode beber, so não enche a cara e vai dirigir em!')
else:
    dif= 18-idade
    print('Pelo que vi vc nao tem 18 anos e vai demorar{} para voce poder comprar bebidas alcolicas'.format(dif),'\nFim do sexto teste\n')
#------------------------------------------------------------------------------------------------------------
age=int(input('Digite a sua idade atual em anos, para que você ser classificado como criança,adolescente, adulto ou idoso:'))
if age<0:
    while(age<=0):
        age=int(input('Digite sua idade em anos de forma valida de 0 para cima:'))
elif age<=1 or age >=11:
    print('Pela sua idade vc é uma criança')
elif age<=12 or age >=19:
        print('Pela sua idade vc é um adolscente')
elif age<=20 or age>=59:
        print('Pela sua idade vc é  um adulto')
elif age in(25 ,35 ,50):
    print('Essas são as maiores medias de idades do Brasil')
else:
        print('Pela sua idade vc é idoso')         
print('Fim sétimo teste \n')
#------------------------------------------------------------------------------------------------------------
for c in range(10,0,-1):
    print(c)
for g in range(0,10):
    print(g)
for i in range(1,6):
    print('Cruzeiro maior de minas\n')
print('Fim do oitavo teste\n')
#------------------------------------------------------------------------------------------------------------
year=2011
user_year = year
print('O ano que foi escolhido foi o {}, digite um ano menor que ele, se vc digitar um maior vai entrar em um loop ate digitar corretamente(numero igual não vai funcionar somente maior)'.format(year))
print('Para testar o while seu primeiro número sera o proprio {}, agora é com vc\n'.format(user_year))
while(user_year<=year):
    user_year=int(input(' Digite um ano maior que {}:'.format(year))) 
print('Fim do nono teste\n')
#------------------------------------------TESTES ABAIXO UM POUCO MAIS COMPLEXOS ------------------------------------------------------------------
dia=int(input('Qual dia que vc nasceu:'))
mes=int(input('Qual mes vc nasceu:'))
ano=int(input ('Qual ano vc nasceu:'))
data_user=datetime.datetime(ano,mes,dia) #Nao sabia e data estilo eua#
data= datetime.datetime.now()
difernca=  data- data_user
print('Você viveu aproximadamente {} dias'.format(difernca.days))
print('\nFim do décimo teste\n')
#--------------------------------------------------------------------------------------------------
numero=random.randint(0,10)
number= int(input('Escolha um número aleatorio entre 0 e 10:'))
if number<=-1 or number>=11:
    while number<=-1 or number>=11:
        number= int(input('Errado, escolha um número aleatorio ENTRE 0 e 10:'))

if number== numero:
    print('Que azar, seu numero {} foi o mesmo que o computdor escolheu')
else:
    print('Parabéns vc escolheu um número diferente do computador, seu numero {}, numero do computador {}'.format(number,numero))
print('\nFim do dédimo primeiro teste\n')
#--------------------------------------------------------------------------------------------------
num= int(input('Escreva um numero para fazermos seu fatorial:'))
numero=num
fat=1
while num>1:
    fat= fat*num
    num= num-1
    print('Fatorial:',fat)
print('O fatorial de {} é {}'.format(numero,fat))  
print('\nFim do décimo segundo teste\n') 
#--------------------------------------------------------------------------------------------------
numero=random.randint(0,10)
number= int(input('Escolha um número aleatorio entre 0 e 10:'))
if number<=-1 or number>=11:
    while number<=-1 or number>=11:
        number= int(input('Errado, escolha um número aleatorio ENTRE 0 e 10:'))
if number==numero:
    print('Que azar, o computador conseguiu de primeira acerta seu numero')
cont =0
while numero!=number:
         cont+=1
         numero=random.randint(0,10)
         print('Tentativa:{} Palpite:{}'.format(cont,numero))
print('Foram precisas {} tentativas para acertar seu numero'.format(cont))
print('\nFim do décimo terceiro teste \n')
#---------------------------------------Ultimo desafio inicial-----------------------------------------------------------
escolha=int(input('Bem vindo ao Menu\nSe deseja somar digite 1\nmultiplicar digite 2\nmaior numero digite 3\nnovos numeros digite 4\nsair do programa digite 5\n'))
if escolha<1 or escolha >5:
    while escolha<1 or escolha >5:
            escolha=int(input('Digite um número valido entre 1 e 5:'))
num1=int(input('Escolha um numero:'))
num2=int(input('Escolha outro numero:'))
            
while escolha!= 5:
    if escolha==1:
        print(num1+num2)
    elif escolha==2:
        print(num1*num2)
    elif escolha==3:
        if num1>num2:
            print(num1)
        else:
            print(num2)
    elif escolha==4:
        num1=int(input('Escolha outro valor para o numero 1:'))
        num2=int(input('Escolha outro numero para numero 2:'))
    else:
        print('numero invalido')
    escolha=int(input('Bem vindo ao Menu\nSe deseja somar digite 1\nmultiplicar digite 2\nmaior numero digite 3\nnovos numeros digite 4\nsair do programa digite 5\n'))
    if escolha<1 or escolha >5:
        while escolha<1 or escolha >5:
            escolha=int(input('Digite um número valido entre 1 e 5:'))
print('Fim do ultimo problema do programa')