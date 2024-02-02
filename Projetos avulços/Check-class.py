# Evia mensagens
import pyautogui as pg
import time
from datetime import datetime



for x in range(3):
    # Tempo de espera para começar
    time.sleep(15)


    # Clicar em shift+tab 9x e enter
    for i in range(4):
        time.sleep(0.1)
        pg.hotkey('shift', 'tab')

    pg.press('enter')