Sempre que for começar um projeto em python primeiro escreva o passo a passo do que for fazer em português.
# Passo 1: Entrar no sistema da empresa (No caso é uma pasta do Drive)
-Abri nova aba (Ctrl+T)
-Escrever link
-Dar Enter
-Esperar o site carregar

# Passo 2: Navegar no sistema e encontrar a base de dados
-Clicar o mouse duas vezes na pasta Exportar

# Passo 3: Download da base de dados
-Clicar no arquivo (Vendas)
-Clicar nos 3 pontos (Mais opções)
-Clicar para fazer o download (Fazer download)
-Esperar abrir a aba de seleção de caminho
-Dar Enter
-Esperar finalizar o download (Deve haver uma alternativa melhor)

# Passo 4: Calcular os indicadores (Faturamento, quantidade de produtos)
-Utilizar comando do pandas para ler o arquivo e salvar em uma variável
-Imprimir essa variável afim de verificação
-Fazer a soma das quantidades e faturamentos (Quantidade, Valor Final) e salvar em variáveis
-Imprimir essas variáveis afim de verificação

# Passo 5: Entrar no email
-Abrir nova aba (Ctrl + T)
-Escrever link
-Dar Enter
-Esperar o site carregar

# Passo 6: Mandar um email para a diretoria com os indicadores
-Clicar no botão +
-Preencher o destinatário
-Dar Tab para selecionar o email referente ao preenchido
-Trocar para o Assunto (Tab)
-Preencher o Assunto
-Trocar para o Corpo (Tab)
-Preencher o Corpo
-Enviar email (Ctrl + Enter)

<-- Passo 1 -->
!pip install pyautogui
import pyautogui
import pyperclip
import time

pyautogui.PAUSE = 1	(segundos)

pyautogui.click -> clicar com o mouse
pyautogui.write -> escrever texto	CUIDADO: Não usa caracteres especiais (por exempo: ?)
pyautogui.press -> pressionar um botão
pyautogui.hotkey -> atalho do teclado
pyperclip.copy -> copia um texto	(com caracteres especiais)

time.sleep -> espera um tempo	(segundos)
<-- Fim Passo 1 -->

<-- Passo 2 -->
É necessário passar as coordenadas de onde o programa precisa clicar
DevTools?

Utilizar um código para descobrir as coordenadas
pyautogui.position -> Devolve a posição do mouse na hora que rodar o código
Utilizar um sleep para ter tempo para colocar o mouse onde se deseja

pyautogui.click(x= , y= , clicks= )
<-- Fim Passo 2 -->

<-- Passo 3 -->
Pegar a coordenada dos 3 cliques

(x3)pyautogui.click	CUIDADO: No meu navegador ele espera eu escolher onde será salvo o arquivo

Adicionais para funcionar no meu caso (vide CUIDADO)
time.sleep
pyautogui.press
<-- Fim Passo 3 -->

<-- Passo 4 -->
import pandas

Armazenar base de dados em uma variável
pandas.read_excel -> lê um arquivo .xlsx (possível trocar excel por html, csv, json, etc)
Importante: necessário colocar o caminho completo para o arquivo
Dica: colocar "r" logo antes das aspas do caminho para ignorar comandos especiais de string como \n

display -> imprime a tabela de maneira organizada

Salvar em uma váriavel a quantidade e em outra o faturamento
Usar colchetes([]) para acessar a coluna de uma tabela
Funções .sum, .count, .average, etc

Imprimir quantidade e faturamento afim de verificação
<-- Fim Passo 4 -->

<-- Passo 5 -->
Repetir o Passo 1 mas com o link do email
<-- Fim Passo 5 -->

<-- Passo 6 -->
pyautogui.click -> abrir novo email
pyautogui.write -> preenche o campo de destinatário
pyperclip.copy -> para os campos assunto e corpo pois possuem caracteres especiais
pyautogui.press -> usa o "Tab" para trocar entre os campos
pyautogui.hotkey -> usa um atalho para colar o assunto e o corpo e um para enviar o email
<-- Fim Passo 6 -->

Esse teoricamente é o fim desse programa, adicionarei também um passo para fechar as abas abertas 
após já terem sido utilizadas e pesquisarei também alternativas para a utilização da biblioteca 
'time', de maneira a garantir que o tempo de espera nunca seja de mais ou de menos.
