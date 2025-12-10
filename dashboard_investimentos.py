# dashboard_investimentos.py
import streamlit as st
import pandas as pd
import plotly.express as px

# Exemplo de dados fictícios
dados = {
    "Ativo": ["Ações", "Fundos Imobiliários", "Renda Fixa", "Criptomoedas"],
    "Valor Investido": [50000, 30000, 20000, 10000],
    "Rentabilidade (%)": [12, 8, 6, 25]
}

df = pd.DataFrame(dados)

# Título do dashboard
st.title("📊 Dashboard de Investimentos")

# Exibir tabela
st.subheader("Resumo dos Investimentos")
st.dataframe(df)

# Gráfico de barras - valor investido
fig_valor = px.bar(df, x="Ativo", y="Valor Investido", 
                   title="Distribuição do Capital",
                   color="Ativo", text="Valor Investido")
st.plotly_chart(fig_valor)

# Gráfico de pizza - proporção dos ativos
fig_pizza = px.pie(df, names="Ativo", values="Valor Investido", 
                   title="Proporção dos Investimentos")
st.plotly_chart(fig_pizza)

# Gráfico de rentabilidade
fig_rent = px.bar(df, x="Ativo", y="Rentabilidade (%)", 
                  title="Rentabilidade por Ativo",
                  color="Rentabilidade (%)", text="Rentabilidade (%)")
st.plotly_chart(fig_rent)