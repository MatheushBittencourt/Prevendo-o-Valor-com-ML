import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.exceptions import NotFittedError
import matplotlib.pyplot as plt

# Carregando o arquivo de dados
try:
    df = pd.read_csv("pizzas.csv")
except FileNotFoundError:
    st.error(
        "Erro: O arquivo 'pizzas.csv' não foi encontrado. Por favor, verifique o caminho e tente novamente."
    )
    st.stop()

# Verificando se o DataFrame tem dados
if df.empty:
    st.error(
        "Erro: O arquivo 'pizzas.csv' está vazio. Por favor, adicione os dados e tente novamente."
    )
    st.stop()

# Treinando o modelo
modelo = LinearRegression()
x = df[["diametro"]]
y = df[["preco"]]
modelo.fit(x, y)

# Título do app
st.title("🍕 Prevendo o Valor de uma Pizza")
st.divider()

# Layout: Tabela e Input lado a lado
col1, col2 = st.columns(2)

with col1:
    st.write("### Dados Carregados")
    st.write(df)

with col2:
    st.write("### Previsão de Preço")
    diametro = st.text_input("Digite o tamanho do diâmetro da pizza (em cm):", placeholder="Ex.: 25")
    
    # Exibir a previsão logo após o input
    if diametro:
        try:
            diametro = float(diametro)  # Convertendo a entrada para float
            if diametro <= 0:
                st.warning("Por favor, insira um valor maior que 0.")
            else:
                preco_previsto = modelo.predict([[diametro]])[0][0]
                st.success(f"O valor da pizza com diâmetro de {diametro:.2f} cm é de **R${preco_previsto:,.2f}**.")
        except ValueError:
            st.error("Erro: Por favor, insira um valor numérico válido.")


# Gráfico abaixo ocupando toda a largura
st.subheader("📈 Relação Diâmetro x Preço")
fig, ax = plt.subplots()
ax.scatter(df["diametro"], df["preco"], color="blue", label="Dados")
ax.set_xlabel("Diâmetro (cm)")
ax.set_ylabel("Preço (R$)")
ax.set_title("Diâmetro vs Preço")
# Linha de regressão
reg_line = modelo.predict(x)
ax.plot(df["diametro"], reg_line, color="red", label="Regressão Linear")
ax.legend()
st.pyplot(fig)
