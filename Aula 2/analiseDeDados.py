# Importação necessária para o funcionamento do Passo 1
import pandas as pd

# Rosulução do Passo 1
tabela = pd.read_csv(r"C:\Projetos\Python\Aula 2\telecom_users.csv")

# Teste realizado, resultado: APROVADO

# Resolução do Passo 2
print(tabela)
tabela = tabela.drop("Unnamed: 0", axis=1)
print(tabela)

# Teste realizado, resultado: APROVADO

# Resolução do Passo 3
print(tabela.info())
tabela["TotalGasto"] = pd.to_numeric(tabela["TotalGasto"], errors="coerce")
tabela = tabela.dropna(how="all", axis=1)
tabela = tabela.dropna(how="any", axis=0)
print(tabela.info())

# Teste realizado, resultado: APROVAOD

# Resolução do Passo 4
print(tabela["Churn"].value_counts())
print(tabela["Churn"].value_counts(normalize=True).map("{:.1%}".format))

#Teste realizado, resultado: APROVADO

# Importação necessária para o funcionamento do Passo 5
import plotly.express as px

# Resolução do Passo 5
for coluna in tabela.columns:
    if coluna != "IDCliente":
        # Cria gráfico
        grafico = px.histogram(tabela, x=coluna, color="Churn", text_auto=True)
        # Exibe gráfico
        grafico.show()
    
# Teste realizado, resultado: 