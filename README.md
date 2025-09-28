# 🚀 Tradutor Profissional de Arquivos com Azure AI

Este projeto é uma aplicação web robusta, construída com Python e Streamlit, que utiliza o poder do **Azure AI Translator** para traduzir o conteúdo de arquivos de texto para diferentes idiomas.

Esta versão foi aprimorada para incluir funcionalidades de nível profissional, demonstrando não apenas a integração com a IA do Azure, mas também as melhores práticas de desenvolvimento de software, como otimização de performance, tratamento de erros e segurança.

## ✨ Funcionalidades Principais

- **Interface Web Interativa:** Criada com Streamlit para uma experiência de usuário amigável e intuitiva.
- **Tradução de Múltiplos Arquivos:** Faça o upload de vários arquivos `.txt` de uma só vez.
- **Cache Inteligente:** Traduções de textos idênticos são armazenadas em memória. Isso torna as repetições instantâneas e **economiza custos** de API.
- **Tratamento de Erros Robusto:** A aplicação fornece feedback claro e específico para o usuário em caso de falhas, como chaves de API incorretas ou problemas de conexão.
- **Segurança:** As credenciais da API do Azure são gerenciadas de forma segura através de variáveis de ambiente, nunca expostas no código.
- **Download de Resultados:** Baixe cada texto traduzido com um único clique.

## 🛠️ Tecnologias Utilizadas

- **Python**
- **Azure AI Translator Service**
- **Streamlit** (para a interface web)
- **Requests** (para chamadas de API)
- **Dotenv** (para gerenciamento de segredos)

---

## ⚙️ Guia de Instalação e Execução

Este guia detalha o processo de setup e execução do projeto em um ambiente de desenvolvimento local. Cada passo foi projetado para garantir uma configuração limpa e funcional.

### **Passo 1: Pré-requisitos do Ambiente**

Antes de iniciar, certifique-se de que seu ambiente de desenvolvimento atende aos seguintes requisitos:

1.  **Interpretador Python:** O projeto requer Python 3.7 ou superior. Verifique sua versão com `python --version`. Se necessário, [instale a partir do site oficial](https://www.python.org/downloads/ ).

2.  **Assinatura do Microsoft Azure:** É necessária uma conta ativa no Azure para provisionar os serviços de IA.

3.  **Recurso do Azure AI Translator:** Um recurso do Serviço de Tradutor deve ser criado no portal do Azure. Este recurso fornecerá as credenciais de API (chave, endpoint e localização) necessárias para a autenticação.
    *   **Precisa de orientação?** O vídeo oficial da Microsoft Azure mostra como criar o recurso e localizar as credenciais necessárias: **[Guia Rápido: Criando um Recurso de Tradução no Azure (Vídeo Oficial)](https://www.youtube.com/watch?v=Xam_QQnb5wQ )**.

### **Passo 2: Clonagem do Repositório**

Clone o código-fonte do projeto para sua máquina local utilizando o Git.

Abra seu terminal ou console de linha de comando e execute os seguintes comandos:

```bash
# Clona o repositório a partir do GitHub.
git clone https://github.com/EduardoBraga1107/tradutor_inteligente_azure.git

# Navega para o diretório raiz do projeto recém-clonado.
cd tradutor_inteligente_azure
```

### **Passo 3: Configuração do Ambiente Virtual e Dependências**

É uma prática recomendada isolar as dependências do projeto em um ambiente virtual para evitar conflitos com outros projetos Python.

```bash
# 1. Cria um ambiente virtual chamado "venv" no diretório do projeto.
python -m venv venv

# 2. Ativa o ambiente virtual.
#    No Windows:
venv\Scripts\activate
#    No macOS/Linux:
source venv/bin/activate

# 3. Instala todas as bibliotecas listadas no arquivo requirements.txt.
#    O pip é o gerenciador de pacotes do Python.
pip install -r requirements.txt
```
Após a ativação, o nome do ambiente (`venv` ) aparecerá no prompt do seu terminal, indicando que ele está ativo.

### **Passo 4: Gerenciamento de Credenciais (Variáveis de Ambiente)**

Credenciais de API são informações sensíveis e não devem ser codificadas diretamente no código-fonte (hardcoding). A abordagem correta é gerenciá-las através de variáveis de ambiente.

1.  Na raiz do projeto, crie um arquivo chamado `.env`. Este arquivo será ignorado pelo Git (conforme definido no `.gitignore`), garantindo que seus segredos não sejam enviados para o repositório público.
2.  Adicione as seguintes variáveis ao arquivo `.env`, substituindo os placeholders pelas suas credenciais reais do Azure:

    ```env
    # Arquivo .env
    TRANSLATOR_KEY="SUA_CHAVE_DA_API_AQUI"
    TRANSLATOR_ENDPOINT="SEU_ENDPOINT_AQUI"
    TRANSLATOR_LOCATION="SUA_REGIAO_AQUI"
    ```
    *   **TRANSLATOR_KEY:** A chave de assinatura para autenticação na API.
    *   **TRANSLATOR_ENDPOINT:** A URL base para todas as chamadas da API.
    *   **TRANSLATOR_LOCATION:** A região do Azure onde seu recurso está hospedado.

### **Passo 5: Execução da Aplicação**

Com o ambiente configurado e as credenciais no lugar, inicie o servidor de desenvolvimento do Streamlit.

Execute o seguinte comando no seu terminal (com o ambiente virtual ainda ativo):

```bash
streamlit run app.py
```

O Streamlit iniciará um servidor web local e abrirá automaticamente uma aba no seu navegador padrão com a aplicação em execução. Agora você pode interagir com a interface, fazer o upload de arquivos e validar a funcionalidade de tradução.

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
