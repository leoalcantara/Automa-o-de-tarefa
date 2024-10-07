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
# Passo 4: Cadastrar 1 produto
# Passo 5: Repetir o processo de cadastrar até cadastrar os produtos
