import time

import pyautogui

pyautogui.alert("O código está sendo executado!!")
pyautogui.PAUSE = 1
# abir o google driver no navegador
pyautogui.press('winleft')
pyautogui.write('brave web browser')
pyautogui.press('enter')
pyautogui.write('https://drive.google.com/drive/my-drive')
pyautogui.press('enter')
# entrar na área de trabalho
pyautogui.hotkey('winleft', 'd')

# clicar no arquivo
pyautogui.moveTo(1317, 46)
pyautogui.mouseDown()
pyautogui.moveTo(805, 462)
pyautogui.hotkey('alt', 'tab')
time.sleep(1.2)
pyautogui.mouseUp()
# enquanto eu estiver arrastando o arquivo, eu vou mudar para o google driver
pyautogui.hotkey('alt', 'tab')
time.sleep(1.3)
# mandar  o arquivo para o google driver
pyautogui.mouseUp()
time.sleep(1.3)
# espearar alguns segundos (5 seg max)
time.sleep(5)

pyautogui.alert("O código acabou de rodar!!")
