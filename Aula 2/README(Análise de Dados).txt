O objetivo desta aula é aprender a fazer análises de dados completas 
em Python, está aula é referente à Aula 2 do Intensivão de Python da 
HashTag.
Projetos de análise de dados normalmente vem em formato de um problema 
do qual você deve descobrir a solução utilizando de bases de dados.

    Passo-a-Passo:
# Passo 1:
- Importar a base de dados

# Passo 2:
- Visualizar a base de dados
- Entender as informações que você têm disponível
- Procurar por problemas na base de dados

# Passo 3:
- Corrigir eventuais problemas na base de dados

# Passo 4:
- Análise inicial dos dados

# Passo 5:
- Criar gráfico
- Mostrar gráfico
- Descobrir os motivos dos cancelamentos

<-- Passo 1 -->
import pandas as pd 

pd.read_csv -> ler base de dados e salvar numa variável     OBS: Como o arquivo está na mesma pasta do programa só é necessário passar o nome do arquivo.
<-- Fim Passo 1 -->

<-- Passo 2 -->
display -> mostra os dados na tela de maneira organizada

IMPORTANTE: Informação que não te ajuda, te atrapalha
.drop -> remove uma linha ou coluna da base de dados (axis = 0 para linha ou 1 para coluna)
<-- Fim Passo 2 -->

<-- Passo 3 -->
IMPORTANTE: Verificar se colunas estão com tipo correto (int64, float64 ou object)
print(tabela.info()) -> retorna resumo da base de dados
tabela[""] -> seleciona uma coluna da tabela
pd.to_numeric(tabela[], erros= ) -> altera o tipo de dado de uma coluna selecionada para to_numeric
erros -> 3 opções: coerce (deixa vazio o valor), raise (desiste da alteração), ignore (ignora o erro)
.dropna -> para remover colunas vazias e linhas com alguma informação vazia (how = all ou any, axis = )
<-- Fim Passo 3 -->

<-- Passo 4 -->
tabela[].value_counts() -> conta quantos tem de cada valor  (normalize -> percentual)
"Churn" -> coluna de cancelamentos
.map("{:.1%}".format) -> formata para percentual
<-- Fim Passo 4 -->

<-- Passo 5 -->
!pip install plotly     (fazer uma vez em uma célula separada)

import plotly.express as px 

px.bar ou .line ou .histogram -> cria um gráfico para salvar em uma variável
.histogram(tabela, x="" ,color="" ) -> parâmetros do gráfico, x é a coluna, color é diferenciação de cor referente a qual dado
.show -> mostra o gráfico na tela   (interativo)
DICA: salvar o nome da coluna em uma variável dentro de um looping para criar vários gráficos
tabela.columns -> retorna uma lista com o nome de todas as colunas
DICA 2: o looping indenrifica o que está no looping através da identação
<-- Fim Passo 5 -->