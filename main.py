import os
import pyautogui
import time
import pandas as pd

diretorio_atual = os.path.dirname(os.path.abspath(__file__))
caminho_csv = os.path.join(diretorio_atual, "products.csv")

tabela = pd.read_csv(caminho_csv)

pyautogui.PAUSE = 0.5

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(10)

pyautogui.write("https://rafael211808.github.io/Register-Products-Project/")
pyautogui.press("enter")
time.sleep(3)

for linha in tabela.index:
  pyautogui.press("tab")
  pyautogui.write(str(tabela.loc[linha, "code"]))
  pyautogui.press("tab")
  pyautogui.write(str(tabela.loc[linha, "brand"]))
  pyautogui.press("tab")
  pyautogui.write(str(tabela.loc[linha, "type"]))
  pyautogui.press("tab")
  pyautogui.write(str(tabela.loc[linha, "category"]))
  pyautogui.press("tab")
  pyautogui.write(str(tabela.loc[linha, "unit_price"]))
  pyautogui.press("tab")
  pyautogui.write(str(tabela.loc[linha, "cost"]))
  pyautogui.press("tab")
  note = tabela.loc[linha, "note"]
  if not pd.isna(note):
    pyautogui.write(str(note))
  pyautogui.press("tab")
  pyautogui.press("enter")
  time.sleep(1)
  pyautogui.press("enter")
  time.sleep(3)
  
  pyautogui.scroll(5000)
