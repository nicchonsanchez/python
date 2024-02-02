
# Para usar o console você usará o print()

print("Meu nome é Nicchon")

# Chamar variável dentro do print
nome = "Nicchon"

print('Meu nome é '+nome) # O + vai juntar a variável com o texto
print('Meu nome é',nome) #  A vírgula vai juntar com o texto, porém vai dar um espaço antes
print('Meu nome é {}'.format(nome)) # Format é o melhor para casos de mais de uma repetição. Ele irá substituir as chaves pelas variáveis na ordem que colocar. Siga o exemplo mais abaixo

nome = "Nicchon"
nomemeio = "Sanchez"
sobrenome = "Pinto"
idade = 22
apelido = "Nick"

print("Seu nome é {} {} {}.\n Tem {} anos e seu apelido é {}".format(nome, nomemeio, sobrenome, idade, apelido))


# Limitação de espaço

x = input("Qual é seu nome? ")

print("Olá {:2}".format(x)) # Se colocar o :2 o mínimo de caracteres retornados será 2
print("Olá {:15}".format(x)) # :15 o mínimo de caracteres retornados será 15

print("Olá {:>15}".format(x)) # :>15 o mínimo de caracteres retornados será 15 e ele alinhará a resposta à direita
print("Olá {:<15}".format(x)) # :<15 o mínimo de caracteres retornados será 15 e ele alinhará a resposta à esquerda
print("Olá {:^15}".format(x)) # :^15 o mínimo de caracteres retornados será 15 e ele alinhará a resposta ao centro

print("Olá {:-^15}".format(x)) # :-^15 o mínimo de caracteres retornados será 15 e ele alinhará a resposta ao centro e os espaços serão preenchidos com o -
print("Olá {:=^15}".format(x)) # :=^15 o mínimo de caracteres retornados será 15 e ele alinhará a resposta ao centro e os espaços serão preenchidos com o =
print("Olá {:a^15}".format(x)) # :a^15 o mínimo de caracteres retornados será 15 e ele alinhará a resposta ao centroNi e os espaços serão preenchidos com o a

