
#kwargs são similares ao args porem, são nomeados.
#Exemplo 1:

def func(*args, **kwargs):
    print(args)
    print(kwargs['nome'], kwargs['sobrenome']) #Aqui são chamados os indices que deseja acessar.

lista1 = [10,11,12,13]
lista2 = [21,22,23]
func(*lista1, *lista2, nome='Paloma', sobrenome='Silva')


#Exemplo 2:

def func(*args, **kwargs):
    print(args)
    print(kwargs)

    idade = kwargs.get('idade') #procurando se idade esta definida na tupla kwargs (rertornou NONE).
    print(idade)


lista1 = [10,11,12,13]
lista2 = [21,22,23]
func(*lista1, *lista2, nome='Paloma', sobrenome='Silva')


#Exemplo 3:

def func(*args, **kwargs):
    print(args)
    print(kwargs)

    idade = kwargs.get('idade') #procurando se idade esta definida no kwargs (retornou com a idade, 35).
    print(idade)


lista1 = [10,11,12,13]
lista2 = [21,22,23]
func(*lista1, *lista2, nome='Paloma', sobrenome='Silva', idade=35)