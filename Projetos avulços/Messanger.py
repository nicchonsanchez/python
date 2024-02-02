# Evia mensagens
import random
import pyautogui as pg
import time
from datetime import datetime

# Frases a enviar
words = ('Va à merda')
time.sleep(10) # Tempo de espera até iniciar o código

# Enviar o horário de início
horario = datetime.now()
pg.write(horario)
pg.press('enter')

# Enviar as mensagens
for i in range(100): # Quantidade de repetições/mensagens
    a = random.choice(words)
    pg.write(a)
    pg.press('enter')
    
# Enviar o horário de término
horario = datetime.now()
pg.write(horario)
pg.press('enter')