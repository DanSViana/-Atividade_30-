'''
Crie um programa para automatizar o envio de um programa qualquer para o repositório remoto do GitHub. Ao terminar, gere o executável e envie o código-fonte e a pasta do executável.
'''
import pyautogui as auto
import time

# tempo que cada comando demora para executar
auto.PAUSE = 1

# instruções
auto.press('win')
auto.write('vscode')
auto.press('enter')

# espera  para abrir o vscode e continuar com os comandos
time.sleep(10)

# continua as instruções
auto.hotkey('ctrl', 'shift', "'")
auto.write('git add .')
auto.press('enter')
auto.write('git commit -m "atividade_30."')

# espera 5 segundos para dar tempo de fazer o commit
time.sleep(5)

# continua as instruções
auto.press('enter')
auto.write('git push')

import pyautogui as auto

# define o tempo de espera para cada comando do pyautogui, para
auto.PAUSE = 0.5

auto.press('win') # abre o menu iniciar
auto.write('chrome')# digita na barra de pesquisa do menu iniciar o nome do progra
auto.press('enter')

# entrar na página de login do GitHub
for i in range(13):
    auto.press('tab')
    
# acessa o site do "GitHub"
auto.write('github.com')
auto.press('enter')

auto.press('enter')

# para entrar com senha e login 
auto.write('DanSViana')
auto.press('tab')
auto.write('Der!m123')
auto.press('enter')