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

### **Passo 4: Gerenciamento de Credenciais com Variáveis de Ambiente (Passo Crucial de Segurança)**

Esta é uma das etapas mais importantes para garantir que seu projeto seja seguro e profissional.

#### **O Porquê: Por que não colocar as chaves direto no código?**

As suas credenciais da API do Azure (chave, endpoint, etc.) são como a senha do seu banco. Se você as coloca diretamente no código (uma prática chamada "hardcoding"), qualquer pessoa que veja seu código no GitHub terá acesso total ao seu recurso do Azure. Isso pode levar a usos indevidos e custos inesperados na sua conta.

A solução profissional é separar as "configurações" (que podem ser públicas) do "código" (que pode ser público) dos "segredos" (que devem ser sempre privados). Fazemos isso usando **Variáveis de Ambiente**.

Neste projeto, usamos um arquivo `.env` para simular esse comportamento em um ambiente de desenvolvimento local. Este arquivo funciona como um "cofre de senhas" que só existe no seu computador. Nosso código é inteligente o suficiente para abrir este cofre e pegar as senhas quando precisa, sem que elas estejam escritas no código principal.

#### **O Como: Configurando o seu cofre local (`.env`)**

1.  **Crie o Cofre:** Na pasta principal do projeto (a mesma onde está o `app.py`), crie um novo arquivo de texto e salve-o com o nome exato de **`.env`**.

2.  **Guarde seus Segredos:** Abra o arquivo `.env` e cole o conteúdo abaixo. Em seguida, substitua os textos de exemplo pelas suas credenciais reais que você pegou no portal do Azure.

    ```env
    # Arquivo .env - Este arquivo é o seu cofre local e NUNCA deve ser enviado para o GitHub.

    TRANSLATOR_KEY="SUA_CHAVE_DA_API_AQUI"
    TRANSLATOR_ENDPOINT="SEU_ENDPOINT_AQUI"
    TRANSLATOR_LOCATION="SUA_REGIAO_AQUI"
    ```
    *   **TRANSLATOR_KEY:** A "senha" para se autenticar na API. É a credencial mais crítica.
    *   **TRANSLATOR_ENDPOINT:** O "endereço de internet" do serviço de tradução. Diz ao nosso código para onde enviar as solicitações.
    *   **TRANSLATOR_LOCATION:** A "região geográfica" (ex: `eastus`, `brazilsouth`) onde seu recurso está hospedado. É necessária para algumas APIs do Azure.

3.  **Garanta a Segurança:** O arquivo `.gitignore` que já está no projeto tem uma linha que diz para o Git ignorar o arquivo `.env`. Isso garante que, mesmo que você tente, não enviará acidentalmente seus segredos para o repositório público.

Com isso, seu código permanece limpo e seguro, enquanto suas credenciais ficam protegidas no seu ambiente local.

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
