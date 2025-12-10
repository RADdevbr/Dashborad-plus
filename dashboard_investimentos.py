{\rtf1\ansi\ansicpg1252\cocoartf2822
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 # dashboard_investimentos.py\
import streamlit as st\
import pandas as pd\
import plotly.express as px\
\
# Exemplo de dados fict\'edcios\
dados = \{\
    "Ativo": ["A\'e7\'f5es", "Fundos Imobili\'e1rios", "Renda Fixa", "Criptomoedas"],\
    "Valor Investido": [50000, 30000, 20000, 10000],\
    "Rentabilidade (%)": [12, 8, 6, 25]\
\}\
\
df = pd.DataFrame(dados)\
\
# T\'edtulo do dashboard\
st.title("\uc0\u55357 \u56522  Dashboard de Investimentos")\
\
# Exibir tabela\
st.subheader("Resumo dos Investimentos")\
st.dataframe(df)\
\
# Gr\'e1fico de barras - valor investido\
fig_valor = px.bar(df, x="Ativo", y="Valor Investido", \
                   title="Distribui\'e7\'e3o do Capital",\
                   color="Ativo", text="Valor Investido")\
st.plotly_chart(fig_valor)\
\
# Gr\'e1fico de pizza - propor\'e7\'e3o dos ativos\
fig_pizza = px.pie(df, names="Ativo", values="Valor Investido", \
                   title="Propor\'e7\'e3o dos Investimentos")\
st.plotly_chart(fig_pizza)\
\
# Gr\'e1fico de rentabilidade\
fig_rent = px.bar(df, x="Ativo", y="Rentabilidade (%)", \
                  title="Rentabilidade por Ativo",\
                  color="Rentabilidade (%)", text="Rentabilidade (%)")\
st.plotly_chart(fig_rent)}