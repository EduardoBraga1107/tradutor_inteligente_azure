# app.py 

import streamlit as st
import requests
import os
import uuid
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
# Isso é ótimo para segurança, pois mantém suas chaves fora do código
load_dotenv()

# --- Funções de Lógica ---

# Cache Inteligente com Streamlit:
# O Streamlit vai "lembrar" o resultado desta função. Se chamarmos a função
# com os mesmos `texto` e `idioma_destino`, ele retorna o resultado salvo
# em vez de executar a função novamente, economizando chamadas de API.
@st.cache_data
def traduzir_texto(texto, idioma_destino):
    """
    Função que chama a API do Azure AI Translator para traduzir um texto.
    Agora com cache e tratamento de erros aprimorado.
    """
    # Pega as credenciais do Azure a partir das variáveis de ambiente
    chave_api = os.environ.get('TRANSLATOR_KEY')
    endpoint = os.environ.get('TRANSLATOR_ENDPOINT')
    localizacao = os.environ.get('TRANSLATOR_LOCATION')

    # Verifica se todas as credenciais estão presentes
    if not all([chave_api, endpoint, localizacao]):
        # Retorna uma tupla: (Sucesso, Mensagem/Resultado)
        return (False, "As variáveis de ambiente do Azure não foram configuradas. Verifique seu arquivo .env.")

    # Monta a URL da API
    path = '/translate'
    url_construida = endpoint + path
    params = {'api-version': '3.0', 'to': [idioma_destino]}
    headers = {
        'Ocp-Apim-Subscription-Key': chave_api,
        'Ocp-Apim-Subscription-Region': localizacao,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }
    body = [{'text': texto}]

    try:
        request = requests.post(url_construida, params=params, headers=headers, json=body)
        
        # Tratamento de Erros Específicos
        # Se o status for 401, é um erro de autenticação (chave errada).
        if request.status_code == 401:
            return (False, "Erro de Autenticação (401): Sua chave da API ou região do Azure está incorreta. Verifique o arquivo .env.")
        
        # Lança um erro para outros status HTTP ruins (4xx ou 5xx)
        request.raise_for_status()

        resposta = request.json()
        traducao = resposta[0]['translations'][0]['text']
        # Retorna sucesso e o texto traduzido
        return (True, traducao)
        
    except requests.exceptions.RequestException as e:
        # Erro de conexão
        return (False, f"Erro de Conexão: Não foi possível conectar à API do Azure. Verifique sua internet ou o endpoint. Detalhes: {e}")
    except (KeyError, IndexError):
        # Erro se a resposta do Azure não vier no formato esperado
        return (False, f"Erro Inesperado: A resposta da API não veio no formato esperado. Resposta recebida: {request.text}")

# --- Interface Gráfica com Streamlit ---

st.set_page_config(page_title="Tradutor Pro com Azure AI", layout="wide")
st.title("🚀 Tradutor Profissional de Arquivos com Azure AI")

st.markdown("""
Esta aplicação utiliza a API do **Azure AI Translator** para traduzir arquivos de texto. 
**Recursos aprimorados:**
- **Cache Inteligente:** Traduções repetidas são instantâneas e não custam nada.
- **Tratamento de Erros:** Mensagens claras em caso de falha na autenticação ou conexão.
""")

# Layout em colunas para melhor organização
col1, col2 = st.columns(2)

with col1:
    st.subheader("1. Configuração")
    idioma_opcoes = {"Português": "pt", "Inglês": "en", "Espanhol": "es", "Francês": "fr", "Alemão": "de"}
    idioma_selecionado_nome = st.selectbox("Traduzir para:", list(idioma_opcoes.keys()))
    idioma_selecionado_codigo = idioma_opcoes[idioma_selecionado_nome]

    st.subheader("2. Upload de Arquivos (.txt)")
    arquivos_enviados = st.file_uploader(
        "Escolha um ou mais arquivos", 
        type=['txt'], 
        accept_multiple_files=True
    )

if st.button("Traduzir Arquivos", type="primary"):
    if arquivos_enviados:
        st.subheader("3. Resultados da Tradução")
        
        for arquivo in arquivos_enviados:
            st.markdown(f"---")
            st.markdown(f"#### Arquivo: `{arquivo.name}`")
            
            try:
                conteudo_original = arquivo.getvalue().decode("utf-8")
                
                # Layout lado a lado para comparação
                res_col1, res_col2 = st.columns(2)
                with res_col1:
                    st.text_area("Conteúdo Original:", conteudo_original, height=200, key=f"original_{arquivo.name}")

                with res_col2:
                    with st.spinner("Traduzindo com a IA do Azure..."):
                        # A função agora retorna uma tupla (sucesso, resultado)
                        sucesso, resultado = traduzir_texto(conteudo_original, idioma_selecionado_codigo)
                    
                    if sucesso:
                        st.text_area("Conteúdo Traduzido:", resultado, height=200, key=f"traduzido_{arquivo.name}")
                        st.download_button(
                            label="📥 Baixar Tradução",
                            data=resultado,
                            file_name=f"traduzido_{arquivo.name}",
                            mime="text/plain"
                        )
                    else:
                        # Se não teve sucesso, 'resultado' contém a mensagem de erro
                        st.error(resultado)

            except Exception as e:
                st.error(f"Ocorreu um erro ao processar o arquivo {arquivo.name}: {e}")
    else:
        st.warning("Por favor, faça o upload de pelo menos um arquivo antes de traduzir.")
