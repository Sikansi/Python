# Variáveis
link = "https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga"       # Link do drive onde se encontra o arquivo
caminho = r"C:\Users\User\Downloads\Vendas - Dez.xlsx"      # Caminho para o arquivo baixado
email = "email@gmail.com"      # Email para quem será enviado
caixa = "https://mail.google.com/mail/u/1/#inbox"        # Link para caixa de entrada do seu email

# Importação das bibliotecas necessárias para o funcionamento do Passo 1
import pyautogui
import pyperclip
import time

# Define um tempo de pausa entre cada comando afim de evitar erros de atropelamento de comandos
pyautogui.PAUSE = 1

# Resolução do Passo 1
pyautogui.press("win")
pyautogui.write("brave")
pyautogui.press("enter")
pyperclip.copy(link)
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")

# Espera para a página carregar
time.sleep(5)

# Teste realizado, resultado: APROVADO

# Resolução do Passo 2
pyautogui.click(x=404 ,y=263 , clicks=2)

# Espera para a página carregar
time.sleep(5)

# Teste realizado, resultado: APROVADO

# Resolução do Passo 3
pyautogui.click(x=437, y=366)
pyautogui.click(x=1726, y=166)
pyautogui.click(x=1459, y=596)
time.sleep(5)
pyautogui.press("enter")

# Espera para o download finalizar
time.sleep(5)

# Teste realizado, resultado: APROVADO

# Importação da biblioteca necessárias para o funcionamento do Passo 4
from IPython.display import display
import pandas

# Resolução do Passo 4
tabela = pandas.read_excel(caminho)
display(tabela)
quantidade = tabela["Quantidade"].sum()
faturamento = tabela["Valor Final"].sum()
print(quantidade)
print(faturamento)

# Teste realizado, resultado: APROVADO

# Resolução do Passo 5
pyautogui.hotkey("ctrl", "t")
pyperclip.copy(caixa)
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")

# Espera para a página carregar
time.sleep(5)

# Teste realizado, resultado: APROVADO

# Resolução do Passo 6
pyautogui.click(x=107, y=170)
pyautogui.write(email)
pyautogui.press("tab")
pyautogui.press("tab")

pyperclip.copy("Relatório de Vendas")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("tab")

texto = f"""Prezados, bom dia

O faturamento de ontem foi de: R$ {faturamento:,.2f}
Referente a uma quantidade de produtos de: {quantidade:,}

Abraços,
Sikansi"""
pyperclip.copy(texto)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("ctrl", "enter")

# Teste realizado, resultado: APROVADO

# Extras

# Fecha as duas abas abertas pelo programa
pyautogui.hotkey("ctrl", "w")
pyautogui.hotkey("ctrl", "w")

# Teste realizado, resultado: APROVADO