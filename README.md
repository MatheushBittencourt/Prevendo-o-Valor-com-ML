# 🧠 Machine Learning - Predições Interativas

Este projeto é uma aplicação interativa criada com **Streamlit**, que permite treinar e usar modelos de aprendizado de máquina para realizar previsões com base em arquivos CSV carregados. A aplicação suporta múltiplos algoritmos de aprendizado de máquina e oferece explicações detalhadas sobre como os resultados são calculados.

---

## 🚀 Funcionalidades

- **Treinamento de Modelos**:  
  Treine diferentes modelos de aprendizado de máquina, incluindo:  
  - Regressão Linear  
  - Árvore de Decisão  
  - Redes Neurais  
- **Carregamento de Dados CSV**:  
  Faça upload de arquivos CSV contendo os dados para análise.  
- **Seleção de Arquivos Existentes**:  
  Escolha entre arquivos CSV já carregados anteriormente.  
- **Previsões Interativas**:  
  Insira valores manuais para obter previsões em tempo real.  
- **Explicações Detalhadas**:  
  Veja como cada modelo chegou à sua previsão, com base nos dados fornecidos.  

---

## 📋 Pré-requisitos

Antes de começar, certifique-se de que os seguintes itens estão instalados:

- **Python** (3.7 ou superior)
- **pip** (para gerenciar pacotes Python)

Pacotes necessários (serão instalados automaticamente no processo de instalação):  
- `streamlit`  
- `pandas`  
- `scikit-learn`  
- `tensorflow`  
- `matplotlib`

---

## ⚙️ Instalação

1. Clone este repositório:
   ```bash
   git clone https://github.com/MatheushBittencourt/Prevendo-o-Valor-com-ML
   ```

2. Acesse a pasta do projeto:
   ```bash
   cd Prevendo-o-Valor-com-ML
   ```

3. Instale as dependências:
   - Usando **Poetry**:
     ```bash
     poetry install
     ```
   - Ou diretamente com **pip**:
     ```bash
     pip install -r requirements.txt
     ```

---

## 🧑‍💻 Como Usar

1. Inicie o aplicativo Streamlit:
   ```bash
   streamlit run app.py
   ```

2. Abra o aplicativo em seu navegador (geralmente em [http://localhost:8501](http://localhost:8501)).

3. Use a interface para:  
   - Carregar novos arquivos CSV ou selecionar arquivos previamente carregados.  
   - Treinar modelos de aprendizado de máquina com os dados fornecidos.  
   - Fazer previsões inserindo valores manualmente.  

---

## 📂 Estrutura do Projeto

```
.
├── app.py                # Arquivo principal da aplicação Streamlit
├── uploads/              # Pasta para armazenar os arquivos CSV carregados
├── requirements.txt      # Dependências do projeto
├── README.md             # Este arquivo
└── .venv/                # Ambiente virtual gerado pelo Poetry (opcional)
```

---

## 📊 Detalhes dos Modelos

- **Regressão Linear**:  
  Um modelo estatístico simples que busca ajustar os dados a uma linha reta, ideal para relações lineares entre variáveis.  
- **Árvore de Decisão**:  
  Um modelo que divide os dados em "ramificações" com base em condições, como um fluxograma. É ótimo para capturar relações mais complexas e regras explícitas.  
- **Rede Neural**:  
  Um modelo avançado que utiliza camadas de neurônios para encontrar padrões não-lineares nos dados, indicado para problemas mais complexos.  

---

## 🔍 Exemplos de Uso

1. **Carregar Arquivo CSV**:  
   Faça upload do seu arquivo com as colunas desejadas. Certifique-se de que o formato do arquivo esteja correto.  

2. **Treinar o Modelo**:  
   Escolha um modelo de aprendizado de máquina na interface e clique para treiná-lo.  

3. **Fazer Previsões**:  
   Insira valores manualmente nos campos fornecidos e clique no botão para prever.  

4. **Ver Explicações**:  
   Após obter a previsão, leia uma explicação detalhada de como o modelo chegou ao resultado.  

---

## 🤔 Melhorias Futuras

- Adicionar suporte a mais algoritmos de aprendizado de máquina, como *Random Forests* e *SVM*.  
- Implementar validações automáticas para garantir a qualidade dos dados carregados.  
- Adicionar opções de salvamento/exportação do modelo treinado para uso posterior.  

---

## 🛠️ Tecnologias Utilizadas

- **Python**: Linguagem principal do projeto.  
- **Streamlit**: Framework para construção de interfaces web interativas.  
- **Pandas**: Manipulação e análise de dados.  
- **Scikit-learn**: Treinamento de modelos de aprendizado de máquina.  
- **TensorFlow**: Implementação de redes neurais.  
- **Matplotlib**: Criação de gráficos e visualizações.  

