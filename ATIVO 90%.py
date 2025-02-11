import pyautogui
import pandas as pd
import time

caminho_arquivo = r"//depo0903/gpa$/PAC/Daniel Menezes/Python/ATIVO/macro.xlsx"
ler = pd.read_excel(caminho_arquivo)
tabela = pd.DataFrame(ler)
print(tabela)

x = 0
y = 1

rua = tabela.iloc[x, y]
modulo = tabela.iloc [x, y + 1]
altura = tabela.iloc [x , y + 2]
pick = tabela. iloc [x , y + 3]


print (rua)

pyautogui.hotkey("win")
time.sleep(1)
pyautogui.write("OPERA")
time.sleep(1)
pyautogui.press("enter")
time.sleep(1)
pyautogui.write("manhattan")
time.sleep(1)
pyautogui.hotkey("down")
pyautogui.hotkey("down")
pyautogui.hotkey("down")
pyautogui.hotkey("down")
pyautogui.hotkey("down")
pyautogui.hotkey("down")
pyautogui.hotkey("down")
pyautogui.hotkey("down")
pyautogui.hotkey("down")
time.sleep(1)
pyautogui.press("enter")
time.sleep(2)
pyautogui.leftClick(58, 83)
time.sleep(2)
pyautogui.write("reconstruir assistente")
time.sleep(2)
pyautogui.press("enter")
time.sleep(1)
pyautogui.leftClick(186, 223)
time.sleep(1)
pyautogui.leftClick(212, 255)
time.sleep(1)
pyautogui.leftClick(255, 246)
time.sleep(1)
pyautogui.leftClick(236, 277)
time.sleep(1)
pyautogui.leftClick(894, 268)

while True and x < len (tabela):
    rua = tabela.iloc[x, y]
    modulo = tabela.iloc [x, y + 1]
    altura = tabela.iloc [x , y + 2]
    pick = tabela. iloc [x , y + 3]
    
    
    
    
    time.sleep(1)
    pyautogui.leftClick(253, 311)
    pyautogui.write("1")
    pyautogui.hotkey("tab")
    pyautogui.write(rua)
    pyautogui.hotkey("tab")
    pyautogui.write(modulo)
    pyautogui.hotkey("tab")
    pyautogui.write(altura)
    pyautogui.hotkey("tab")
    pyautogui.write(pick)
    pyautogui.leftClick(254, 380)
    pyautogui.write("1")
    pyautogui.hotkey("tab")
    pyautogui.write(rua)
    pyautogui.hotkey("tab")
    pyautogui.write(modulo)
    pyautogui.hotkey("tab")
    pyautogui.write(altura)
    pyautogui.hotkey("tab")
    pyautogui.write(pick)
    pyautogui.leftClick(885, 491)
    time.sleep(3)
    pyautogui.leftClick(892, 274)
    x = x + 1
    time.sleep(2)
    print("DEV: DANIEL MENEZES")
    print(x)
    