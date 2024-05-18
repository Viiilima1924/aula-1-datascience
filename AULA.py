# texto = "Ana"
# numero_inteiro = 10
# numero_real = 0.10
# dado_boleano = True

# # print() -> mostrar ou imprimir dados no console

# print(texto)
# print(numero_inteiro)
# print(numero_real)
# print(dado_boleano)




# #typr - verificar o tipo de dado

# print(type(texto))
# print(type(numero_inteiro))
# print(type(numero_real))
# print(type(dado_boleano))

# # cocatenação == juntar textos, variáveis, resultados

# text = (type(texto))
# inteiro = (type(numero_inteiro))
# real = (type(numero_real))
# boleano = (type(dado_boleano))

# print('Essa variável ->' , texto, 'é da', text)
# print('Essa variável ->' , numero_inteiro, 'é da', inteiro)
# print('Essa variável ->' , numero_real, 'é da', real)
# print('Essa variável ->' , dado_boleano, 'é da', boleano)


# print(f'Essa variável -> , {texto}, é da, {text} ' )
# print(f'Essa variável -> , {numero_inteiro} é da, {inteiro} ')
# print(f'Essa variável -> , {numero_real}, é da, {real} ' )
# print(f'Essa variável -> , {dado_boleano}, é da, {boleano} ' )



#------------------------------------------------------


# NOME = 'Fernando'
# nome = 'Jr'
# print(nome)


# NOME = 'Caio'
# NOME = 'Karol'
# print(NOME)


# def nome():
#     name = 'Maria'
#     return name

# NOME = nome()
# print(NOME)

# * / 
# print((1+3)+3 ** 2/5)
# nome = input ('digite o seu nome:')
# print(nome)

# numero1 = int(input('>>'))
# numero2 = int(input('>>'))

# calcular = numero1 * numero2
# print(calcular)

# x = '10'
# text = int(x)
# n = text + 1
# print(n)

# texto = "Caculadora Adição "
# print(texto)

# numero1 = int(input('>>'))
# numero2 = int(input('>>'))

# calcular = numero1 + numero2
# print(calcular)

# texto = "Caculadora Subtração "
# print(texto)

# numero1 = int(input('>>'))
# numero2 = int(input('>>'))

# calcular = numero1 - numero2
# print(calcular)

# texto = "Caculadora Multiplicação "
# print(texto)

# numero1 = int(input('>>'))
# numero2 = int(input('>>'))


# calcular = numero1 * numero2
# print(calcular)

# texto = "Caculadora Divisão "
# print(texto)

# numero1 = int(input('>>'))
# numero2 = int(input('>>'))

# calcular = numero1 / numero2
# print(calcular)

# n1 = float(input('Digite um número:'))
# n2 = float(input('Digite outro número:'))


# print(f'''
# Resultado da soma: {n1+n2}
# Resultado da divisão: {n1//n2}
# Resultado da Multiplicação: {n1*n2}
# Resultado da Subtração: {n1-n2}

# '''
# )

# numero = 10 
#           #0  1 2 3  4    5    6
# numeros = [10,2,3,5,'a', True, 8.0]
# print(numeros)
# print(numeros[-2])


# dado = numeros [-1] = 20
# print(numeros)

# lista = [10,15,3,1,5]

# indice = lista[0]
# indice2 = lista[1]

# print(indice + indice2)

# numeros1 = list(range(1,11,2))
# print(numeros1)

# comprimento/tamanho ==len

# lista = [10,15,3,1,5]

# print(len(lista))

#add == append()

# lista. append(10)
# print(lista)

# #transormar uma variável em uma lista do tipo str
# variavel = 'text'
# lista2 = list(variavel)
# print(lista2)

# #criar uma lista com list()
# cria_sequencia = list(range(1,101))
# soma = sum(cria_sequencia)
# print(soma)

#max e min
# menor = min(cria_sequencia)
# print(menor)

# maior = max(lista2)
# print(maior)

# lista3 = [6456,56,45,1,89,1100,1,9,7]
# organizar = sorted(lista3)
# print (organizar)

# pop() -> remover um indice
# lista3.pop(0)
# print(lista3)


# del lista3 [0]
# print(lista3)

# lista3 = [6456,56,45,1,89,1100,1,9,7]
# lista3.remove(89)

# del lista3[0]
# print(lista3)

#Tuplas
#Listas imutaveis
#usamos parenteses

# tupla = (1,2,150,6,9,9,9,9)
# print(tupla[2])

#conta a quantidade de valores 
#que foi declarado no parenteses

# contador = tupla.count(9)

# #verifica o indice do valor
# indice = tupla.index(9)
# print(contador, indice)

# #tamanaho len
# print(len(tupla))

#max e min

# maior = max(tupla)
# menor = min(tupla)
# print(menor, maior)

# ordenar = sorted(tupla)
# print(ordenar)

# tupla4 = (1,4546,1,89,3,4,656)
# sorted(tupla4)
# a,b,c,d,e,f,g, = tupla4
# numero = tupla4[1]
# print(numero)
# print(tupla4)

# conjuntos {}

# nome = {1,5,150,56,89,78}
# conjunto2 = { 1,6,6}

# diferenca = conjunto2 ^ nome
# nome.symmetric_difference(conjunto2)
# print(diferenca)
# print(nome.difference(conjunto2))

# conjunto4 = set([1,56,6])
# remove= conjunto4.remove(56)
# print(conjunto4)

#VAI VERIFICAR O QUE TEM NOS DOIS CONJUNTOS 
# nome.intersection(conjunto2)
# print(nome.intersection(conjunto2))




# print(nome.union,(conjunto2))



# dicionario ={
# 'nome' : 'Pedro',
# 'idade': 25,
# 'endereco' : 'Rua 100',
# 'curso': 'Python60h',

# }
# print(dicionario['curso'])

texto = "MÉDIA DAS NOTAS OBTIDAS PELO ALUNO FERNANDO:"
print(texto)

tupla = (10,9,8,6)
contador = tupla.count(tupla)




texto = "Maior nota:"
print(texto)


maior = max(tupla)
print(maior)


texto = "Menorr nota:"
print(texto)

menor = min(tupla)
print(menor)
