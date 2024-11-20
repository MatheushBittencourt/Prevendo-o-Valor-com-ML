import os
import pandas as pd
import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.neural_network import MLPRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error

# Diretório de uploads
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def save_file(uploaded_file):
    file_path = os.path.join(UPLOAD_FOLDER, uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    return file_path

# Título do app
st.title("Prevendo Valores com Machine Learning")

# Upload e seleção de arquivos
if "file_list" not in st.session_state:
    st.session_state.file_list = [f for f in os.listdir(UPLOAD_FOLDER) if f.endswith(".csv")]
if "active_file" not in st.session_state:
    st.session_state.active_file = None

uploaded_file = st.file_uploader("Carregue um arquivo CSV", type="csv")
if uploaded_file is not None:
    file_path = save_file(uploaded_file)
    if uploaded_file.name not in st.session_state.file_list:
        st.session_state.file_list.append(uploaded_file.name)
    st.session_state.active_file = uploaded_file.name
    st.success(f"Arquivo '{uploaded_file.name}' carregado com sucesso!")

selected_file = st.selectbox(
    "Selecione um arquivo existente:",
    ["Selecione um arquivo"] + st.session_state.file_list,
    index=(st.session_state.file_list.index(st.session_state.active_file) + 1) if st.session_state.active_file else 0,
)
if selected_file and selected_file != "Selecione um arquivo":
    st.session_state.active_file = selected_file

data = None
if st.session_state.active_file:
    file_path = os.path.join(UPLOAD_FOLDER, st.session_state.active_file)
    data = pd.read_csv(file_path)
    st.write(f"Dados carregados do arquivo: {st.session_state.active_file}")
    st.dataframe(data)

# Configuração de modelo
if data is not None:
    columns = list(data.columns)
    st.write("Selecione as colunas para o treinamento do modelo:")
    input_columns = st.multiselect("Colunas de entrada (features):", columns)
    output_column = st.selectbox("Coluna de saída (target):", columns)

    model_type = st.selectbox(
        "Escolha o modelo de aprendizado de máquina:",
        ["Linear Regression", "Decision Tree", "Neural Network"],
    )

    if input_columns and output_column:
        X = data[input_columns]
        y = data[output_column]

        # Divisão dos dados
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Treinamento
        model = None
        scaler = None
        if model_type == "Linear Regression":
            model = LinearRegression()
        elif model_type == "Decision Tree":
            model = DecisionTreeRegressor(random_state=42)
        elif model_type == "Neural Network":
            scaler = StandardScaler()
            X_train = scaler.fit_transform(X_train)
            X_test = scaler.transform(X_test)
            model = MLPRegressor(hidden_layer_sizes=(64, 64), max_iter=500, random_state=42)

        # Treinar o modelo
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)

        # Métricas
        mse = mean_squared_error(y_test, y_pred)
        st.write(f"Modelo: **{model_type}** treinado com sucesso!")
        st.write(f"Erro Quadrático Médio (MSE): {mse:.2f}")

        # Previsões manuais com explicação
        st.subheader("Faça previsões com inputs manuais")
        input_data = {}
        for col in input_columns:
            input_data[col] = st.number_input(f"{col}:", value=None, format="%.2f", placeholder=f"Digite o valor de {col}")

        if st.button("Prever"):
            input_df = pd.DataFrame([input_data])
            if scaler:  # Normaliza os dados, se necessário
                input_df = scaler.transform(input_df)
            prediction = model.predict(input_df)
            st.success(f"A previsão é: {prediction[0]:.2f}")

            # Explicação da previsão
            st.subheader("Como o valor foi encontrado:")
            st.write("Detalhes do modelo utilizado:")
            st.write(f"- **Modelo:** {model_type}")
            st.write(f"- **Colunas de entrada:** {', '.join(input_columns)}")
            st.write("Valores fornecidos para previsão:")
            for col, val in input_data.items():
                st.write(f"- **{col}:** {val}")
            st.write("Este valor foi calculado com base no modelo treinado usando os dados disponíveis e a relação estatística entre os insumos e o preço.")

