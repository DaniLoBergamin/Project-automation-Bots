# Passo a passo do projeto

# 1º - Entrar no sistema da empresa
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login   

# Bibliotecas Python
    # PYAUTOGUI - Permite que seus scripts Python controlem o mouse e o teclado para automatizar as interações com outros aplicativos
    #  pip install pyautogui
    
import pyautogui
import time

# Clicar -> pyautogui.click
# Escrever -> pyautogui.write
# Apertar -> pyautogui.press
# Utilizar um atalho -> pyautogui.hotkey        (ctrl + c)
# Scroll (rolar) -> pyautogui.scroll            (-100) pra baixo / (100) pra cima

# Comando para inserir tempo (segundos) entre cada comando
pyautogui.PAUSE = 1

# Apertar a tecla windows
pyautogui.press("win")
# Digitar o programa (CHROME)
pyautogui.write("chrome")
# Entrar no google chrome
pyautogui.press("enter")
# Digitar o link
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
# Apertar enter
pyautogui.press("enter")

# Esperar 5 segundos apenas nessa parte
time.sleep(5)



# 2º - Fazer login

# X,Y - Local da tela em que o mouse vai clicar (email)
pyautogui.click(x=1153, y=445)
# Digitar o email
pyautogui.write("test@test.com.br")
#Passar para a senha
pyautogui.press("tab")
# Digitar a senha
pyautogui.write("123456")
# Clicar em logar
pyautogui.click(x=1346, y=617)

time.sleep(3)



# 3º - Importar base de dados (produtos.csv)

# pip install pandas numpy openpyxl

import pandas                                       # import pandas as pd

tabela = pandas.read_csv("produtos.csv")            # tabela = pd.read_csv("produtos.csv")
print(tabela)

# Quando utilizar for, você precisa utilizar o TAB, pois ele utiliza apenas o comando que está com TAB na próxima linha.
# O que não estiver dentro do TAB, ele não irá repetir.

# 4º - Cadastrar um produto
for linha in tabela.index:



# 5º - Repetir o cadastro com toda a base de dados

    # Click do mouse
    pyautogui.click(x=1246, y=303)
    
    # Código
    codigo = tabela.loc[linha, "codigo"]    # Pegar da tabela o valor do campo que a gente quer preencher
    pyautogui.write(str(codigo))
    pyautogui.press("tab")
    # Marca
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    # Tipo do produto
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    # Categoria do produto
    pyautogui.write(str(tabela.loc[linha, "categoria"]))     # str - Transforma o número em texto / "1"
    pyautogui.press("tab")
    # Preço unitário
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    # Custo do produto
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    # Obs
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):        # Se obs estiver vazio, pular e seguir para a proxima.
                                    # Se tiver observacao, escrever.
        pyautogui.write(str(tabela.loc[linha, "obs"]))
        
    pyautogui.press("tab")
    
    # Enviar o produto
    pyautogui.press("enter")

    pyautogui.scroll(5000)



