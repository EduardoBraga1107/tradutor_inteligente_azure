# 🚀 Tradutor Profissional de Arquivos com Azure AI

Este projeto é uma aplicação web robusta, construída com Python e Streamlit, que utiliza o poder do **Azure AI Translator** para traduzir o conteúdo de arquivos de texto para diferentes idiomas.

Esta versão foi aprimorada para incluir funcionalidades de nível profissional, demonstrando não apenas a integração com a IA do Azure, mas também as melhores práticas de desenvolvimento de software, como otimização de performance, tratamento de erros e segurança.

## Funcionalidades Principais

- **Interface Web Interativa:** Criada com Streamlit para uma experiência de usuário amigável e intuitiva.
- **Tradução de Múltiplos Arquivos:** Faça o upload de vários arquivos `.txt` de uma só vez.
- **Cache Inteligente:** Traduções de textos idênticos são armazenadas em memória. Isso torna as repetições instantâneas e **economiza custos** de API.
- **Tratamento de Erros Robusto:** A aplicação fornece feedback claro e específico para o usuário em caso de falhas, como chaves de API incorretas ou problemas de conexão.
- **Segurança:** As credenciais da API do Azure são gerenciadas de forma segura através de variáveis de ambiente, nunca expostas no código.
- **Download de Resultados:** Baixe cada texto traduzido com um único clique.

## Tecnologias Utilizadas

- **Python**
- **Azure AI Translator Service**
- **Streamlit** (para a interface web)
- **Requests** (para chamadas de API)
- **Dotenv** (para gerenciamento de segredos)

---

## Guia de Instalação e Execução

Siga os passos abaixo para executar o projeto em sua máquina local.

### 1. Pré-requisitos

- **Python 3.7+** instalado.
- Uma conta no **Microsoft Azure** com uma assinatura ativa.
- Um recurso do **Serviço de Tradutor (Translator Service)** criado no Azure. Se não tiver um, [siga este guia para criar](https://learn.microsoft.com/pt-br/azure/ai-services/translator/translator-how-to-signup ).

### 2. Clone o Repositório

```bash
git clone https://github.com/EduardoBraga1107/tradutor_inteligente_azure.git
cd tradutor_inteligente_azure
```

### 3. Instale as Dependências

Crie um ambiente virtual (altamente recomendado ) e instale as bibliotecas necessárias.

```bash
# Crie um ambiente virtual
python -m venv venv

# Ative o ambiente virtual
# No Windows:
venv\Scripts\activate
# No macOS/Linux:
source venv/bin/activate

# Instale as bibliotecas a partir do arquivo requirements.txt
pip install -r requirements.txt
```

### 4. Configure as Variáveis de Ambiente

As suas credenciais secretas do Azure devem ser armazenadas de forma segura.

1.  Na raiz do projeto, crie um arquivo chamado `.env`.
2.  Adicione suas credenciais a este arquivo, substituindo os valores de exemplo:

    ```env
    # Arquivo .env
    TRANSLATOR_KEY="SUA_CHAVE_DA_API_AQUI"
    TRANSLATOR_ENDPOINT="SEU_ENDPOINT_AQUI"
    TRANSLATOR_LOCATION="SUA_REGIAO_AQUI" 
    ```
    *   **TRANSLATOR_KEY:** Uma das chaves (Key 1 ou Key 2) do seu recurso no Azure.
    *   **TRANSLATOR_ENDPOINT:** O endpoint de texto encontrado na visão geral do seu recurso.
    *   **TRANSLATOR_LOCATION:** A região/localização do seu recurso (ex: `eastus`, `brazilsouth`).

### 5. Execute a Aplicação

Com tudo configurado, inicie a aplicação Streamlit com o seguinte comando no terminal:

```bash
streamlit run app.py
```

Seu navegador abrirá automaticamente com a aplicação rodando! Agora você pode seguir o guia de testes para validar todas as funcionalidades, incluindo o cache e o tratamento de erros.

---

## 👨‍💻 Desenvolvido por

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/EduardoBraga1107">
        <img src="https://avatars.githubusercontent.com/u/101203895?v=4" width="100px;" alt="Foto de Eduardo Braga no GitHub"/>  

        <sub>
          <b>Eduardo Braga</b>
        </sub>
      </a>
    </td>
  </tr>
</table>

**Conecte-se comigo:**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white )](https://www.linkedin.com/in/eduardo-braga-ribeiro-781254237/ )
