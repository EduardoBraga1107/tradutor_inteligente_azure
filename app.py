# app.py

import streamlit as st
import requests
import uuid
import os
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
# Isso mantém suas chaves secretas seguras e fora do código
load_dotenv()

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="Tradutor Inteligente com Azure AI",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- FUNÇÕES DE LÓGICA ---

# Função para buscar as credenciais do Azure de forma segura
def get_azure_credentials():
    """Busca as credenciais da API do Azure a partir das variáveis de ambiente."""
    try:
        translator_key = os.environ["TRANSLATOR_KEY"]
        translator_endpoint = os.environ["TRANSLATOR_ENDPOINT"]
        translator_location = os.environ["TRANSLATOR_LOCATION"]
        return translator_key, translator_endpoint, translator_location
    except KeyError as e:
        # Se uma variável de ambiente não for encontrada, retorna None e o nome da chave faltante
        return None, None, None, str(e)

# Função que chama a API de Tradução do Azure
# O @st.cache_data "lembra" o resultado para entradas idênticas, economizando tempo e dinheiro.
@st.cache_data
def traduzir_texto(texto_original, idioma_destino, _translator_key, _translator_endpoint, _translator_location):
    """
    Chama a API do Azure AI Translator para traduzir o texto.
    Usa cache para otimizar performance e custos.
    """
    # Monta a URL da API
    path = '/translate'
    constructed_url = _translator_endpoint + path

    # Parâmetros da requisição
    params = {
        'api-version': '3.0',
        'to': idioma_destino
    }

    # Cabeçalhos da requisição, incluindo a chave de autenticação
    headers = {
        'Ocp-Apim-Subscription-Key': _translator_key,
        'Ocp-Apim-Subscription-Region': _translator_location,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }

    # Corpo da requisição com o texto a ser traduzido
    body = [{'text': texto_original}]

    # Faz a chamada para a API
    try:
        request = requests.post(constructed_url, params=params, headers=headers, json=body)
        request.raise_for_status()  # Lança um erro para respostas HTTP 4xx/5xx
        response = request.json()
        return response[0]['translations'][0]['text']
    except requests.exceptions.RequestException as e:
        # Retorna uma mensagem de erro clara se a chamada falhar
        return f"Erro na API: {e}"

# --- INTERFACE DO USUÁRIO (Streamlit) ---

st.title("🚀 Tradutor Profissional de Arquivos com Azure AI")
st.markdown("Faça o upload de um ou mais arquivos de texto (`.txt`) e veja a mágica acontecer!")

# Sidebar para configuração e ajuda
with st.sidebar:
    st.header("Configurações")
    idioma_destino = st.selectbox(
        "Selecione o idioma para tradução:",
        ("en", "es", "fr", "de", "pt", "it", "ja", "ko", "ru"),
        format_func=lambda x: {
            "en": "Inglês", "es": "Espanhol", "fr": "Francês", "de": "Alemão",
            "pt": "Português", "it": "Italiano", "ja": "Japonês", "ko": "Coreano", "ru": "Russo"
        }[x]
    )
    st.info("Este projeto utiliza cache para otimizar o desempenho. Textos idênticos são traduzidos instantaneamente após a primeira vez.")
    st.warning("Suas chaves da API do Azure são carregadas de forma segura a partir de um arquivo `.env` e não são expostas no código.")

# Busca as credenciais do Azure
translator_key, translator_endpoint, translator_location, error_key = get_azure_credentials()

# Verifica se as credenciais foram carregadas com sucesso
if not all([translator_key, translator_endpoint, translator_location]):
    st.error(f"❌ **Erro de Configuração:** A variável de ambiente {error_key} não foi encontrada.")
    st.error("Por favor, verifique se o seu arquivo `.env` está na pasta raiz do projeto e contém todas as chaves necessárias (TRANSLATOR_KEY, TRANSLATOR_ENDPOINT, TRANSLATOR_LOCATION).")
else:
    # Área para upload de arquivos
    uploaded_files = st.file_uploader(
        "Escolha os arquivos de texto (`.txt`)",
        type="txt",
        accept_multiple_files=True
    )

    if uploaded_files:
        st.header("Resultados da Tradução")
        # Itera sobre cada arquivo enviado
        for uploaded_file in uploaded_files:
            try:
                # Lê o conteúdo do arquivo
                texto_original = uploaded_file.getvalue().decode("utf-8")

                # Cria duas colunas para exibir o texto original e o traduzido lado a lado
                col1, col2 = st.columns(2)

                with col1:
                    st.subheader(f"Original ({uploaded_file.name})")
                    st.text_area("Conteúdo Original", texto_original, height=200, key=f"original_{uploaded_file.name}")

                with col2:
                    st.subheader(f"Traduzido ({idioma_destino.upper()})")
                    # Chama a função de tradução com um spinner de carregamento
                    with st.spinner(f"Traduzindo {uploaded_file.name}..."):
                        texto_traduzido = traduzir_texto(
                            texto_original, idioma_destino,
                            translator_key, translator_endpoint, translator_location
                        )

                    # Verifica se a tradução retornou um erro
                    if texto_traduzido.startswith("Erro na API:"):
                        st.error(f"Falha ao traduzir {uploaded_file.name}: {texto_traduzido}")
                    else:
                        st.text_area("Conteúdo Traduzido", texto_traduzido, height=200, key=f"traduzido_{uploaded_file.name}")
                        # Adiciona um botão de download para o texto traduzido
                        st.download_button(
                            label="📥 Baixar Tradução",
                            data=texto_traduzido.encode('utf-8'),
                            file_name=f"traduzido_{uploaded_file.name}",
                            mime='text/plain',
                        )
                st.divider() # Adiciona uma linha divisória entre os arquivos
            except Exception as e:
                st.error(f"Ocorreu um erro ao processar o arquivo {uploaded_file.name}: {e}")
                
