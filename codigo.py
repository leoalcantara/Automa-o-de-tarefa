# Passo 1: Entrar no sistema da empresa https://dlp.hashtagtreinamentos.com/python/intensivao/login
# pit install pyautogui
import pyautogui
import time

#pyaurogui.write -> escreve um texto
#pyaurogui.click -> clica com o mouse
#pyaurogui.press -> aperta uma tecla
#pyaurogui.hotkey -> aperta um atalho de teclado (ctrl, c)

pyautogui.PAUSE = 0.5

# abrir navegador
#apertar a tecla win
pyautogui.press("win")
pyautogui.write("Chrome")
pyautogui.press("enter")

# entrar no link: pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")



# Passo 2:  Fazer login
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

# Pausa de 3 segundos
time.sleep(3)
pyautogui.click(x=518, y=375)
pyautogui.write("teste@mail.com")

# Passar para proximo campo
pyautogui.press("tab")
pyautogui.write("teste@mail.com")

# Apertar o botão de logar
pyautogui.click(x=779, y=534)

time.sleep(2)

# Passo 3:  Importar a base de dados
import pandas

tabela = pandas.read_csv("produtos.csv")
print(tabela)

# Passo 4: Cadastrar 1 produto
pyautogui.click(x=530, y=259)
#codigo
pyautogui.write("codigo")
pyautogui.press("tab")
#marca
pyautogui.write("marca")
pyautogui.press("tab")
#tipo
pyautogui.write("tipo")
pyautogui.press("tab")
#categoria
pyautogui.write("categoria")
pyautogui.press("tab")
#preço unitário
pyautogui.write("codigo")
pyautogui.press("tab")
#custo
pyautogui.write("custo")
pyautogui.press("tab")
#obs
pyautogui.write("obs")
pyautogui.press("tab")

#clicar em enviar
pyautogui.press("enter")

# Passo 5: Repetir o processo de cadastrar até cadastrar os produtos
