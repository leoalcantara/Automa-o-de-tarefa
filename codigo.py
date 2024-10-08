# Passo 1: Entrar no sistema da empresa https://dlp.hashtagtreinamentos.com/python/intensivao/login
# pit install pyautogui
import pyautogui
import time

#pyaurogui.write -> escreve um texto
#pyaurogui.click -> clica com o mouse
#pyaurogui.press -> aperta uma tecla
#pyaurogui.hotkey -> aperta um atalho de teclado (ctrl, c)

pyautogui.PAUSE = 0.3

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


linha = 0
for linha in tabela.index:
    # selecionar o primeiro campo
    pyautogui.click(x=530, y=259)        
    
    # codigo
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")

    # marca    
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")
    
    # tipo
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")

    # categoria
    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")
    # preco_unitario
    preco_unitario = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")

    #custo
    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")

    #obs
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(str(obs))
    pyautogui.press("tab")

    #clicar em enviar
    pyautogui.press("enter")
    pyautogui.scroll(5000)

# Passo 5: Repetir o processo de cadastrar até cadastrar os produtos
