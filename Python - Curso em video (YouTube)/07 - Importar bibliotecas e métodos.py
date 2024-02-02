
# 07 - Importar bibliotecas e métodos

# Para importar algo usamos o import

import math

# Porém nesse caso ele importaria tudo que está dentro de math.
# ceil(), floor(), trunc(), pow(), sqrt(), factorial() e etc...

# Se quisermos importar somente pow() de dentro de math podemos usar

from math import pow

print(math.pow(2,4)) # Vai calcular 2 elevado à 4 que é 16


# Agora vamos importar a biblioteca random. Ela gera números aleatórios

import random
print(random.random()) # random.random() gera qualquer número aleatório
print(random.randint(1, 100)) # aqui vai gerar um número inteiro de 1 à 100



# Importando emojis

import emooji
print(emooji.emojize("Olá :smile:"))



import random

print("<h2>Número aleatório: {}</h2>", format(random.randint(1-100)))
    