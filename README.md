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

## ⚙️ Guia de Instalação: Dando Vida ao Tradutor!

Vamos montar nosso tradutor passo a passo. Pense nisso como montar um brinquedo de LEGO: precisamos das peças certas e de um manual de instruções. Este é o nosso manual!

### **Passo 1: As Ferramentas Mágicas (Pré-requisitos)**

Antes de começar, precisamos de três coisas na nossa "bancada de trabalho":

1.  **A Linguagem dos Robôs (Python):** Nosso projeto fala uma linguagem chamada Python. Se você ainda não tem o Python no seu computador, é como não ter as pilhas para o brinquedo. [Você pode baixá-lo aqui](https://www.python.org/downloads/ ). (Versão 3.7 ou mais nova).

2.  **A Super Força da Nuvem (Conta no Azure):** A "inteligência" do nosso tradutor vem de um supercomputador da Microsoft chamado Azure. Precisamos de uma conta para poder usar essa força.

3.  **A Chave do Cofre Mágico (Recurso de Tradutor):** Dentro do Azure, vamos criar um "cofre mágico" que guarda o poder da tradução. Este cofre nos dará chaves secretas para que só a gente possa usar.
    *   **Precisa de ajuda?** Este vídeo da comunidade no YouTube mostra o passo a passo na tela, como se fosse um gameplay: **[Como Criar o Recurso de Tradutor no Azure (Vídeo)](https://www.youtube.com/watch?v=1NMAER2jS4Q )**.
    *   *(Observação: Este é um vídeo útil da comunidade e não um conteúdo oficial da Microsoft.)*

### **Passo 2: Copiando o Projeto (Clonando o Repositório)**

Agora, vamos trazer o projeto para o seu computador.

Abra o seu "mapa de comandos" (o terminal, prompt de comando ou PowerShell) e digite os seguintes feitiços:

```bash
# Feitiço 1: Copia o projeto do GitHub para o seu computador.
git clone https://github.com/EduardoBraga1107/tradutor_inteligente_azure.git

# Feitiço 2: Entra na pasta mágica que acabamos de criar.
cd tradutor_inteligente_azure
```

### **Passo 3: Montando o "Kit de Peças" (Instalando as Dependências )**

Nosso projeto precisa de algumas "peças" extras para funcionar. Vamos criar um espaço de trabalho limpo e instalar tudo.

```bash
# Comando 1: Cria uma "caixa de brinquedos" separada para este projeto.
# Isso se chama ambiente virtual e é uma ótima prática!
python -m venv venv

# Comando 2: "Abre" a caixa de brinquedos para começarmos a usar.
# No Windows:
venv\Scripts\activate
# No macOS/Linux:
source venv/bin/activate

# Comando 3: Lê a nossa "lista de compras" (requirements.txt) e instala todas as peças.
pip install -r requirements.txt
```
Se tudo deu certo, você verá o nome `(venv)` no início da linha do seu terminal.

### **Passo 4: As Chaves Secretas (Configurando as Variáveis de Ambiente)**

Lembra das chaves secretas do cofre mágico do Azure? Nunca devemos deixá-las jogadas no nosso código. Vamos guardá-las em um cofre local.

1.  Na pasta do projeto, crie um novo arquivo de texto e salve-o com o nome exato de `.env` (ponto env).
2.  Abra este arquivo e cole o seguinte conteúdo, substituindo os textos de exemplo pelas suas chaves reais que você pegou no vídeo:

    ```env
    # Arquivo .env
    TRANSLATOR_KEY="COLE_SUA_CHAVE_AQUI"
    TRANSLATOR_ENDPOINT="COLE_SEU_ENDPOINT_AQUI"
    TRANSLATOR_LOCATION="COLE_SUA_REGIAO_AQUI"
    ```
    *   **TRANSLATOR_KEY:** A "senha" do cofre.
    *   **TRANSLATOR_ENDPOINT:** O "endereço" do cofre na internet.
    *   **TRANSLATOR_LOCATION:** A "cidade" onde o cofre está guardado.

### **Passo 5: Ligar! (Executando a Aplicação)**

Chegou a hora da verdade! Com tudo pronto, digite o comando final para dar vida ao nosso tradutor:

```bash
streamlit run app.py
```

O seu navegador de internet vai abrir uma nova aba como num passe de mágica, mostrando a interface do seu Tradutor Inteligente. **Parabéns, você conseguiu!**

Agora você pode fazer o upload dos seus arquivos e testar a tradução.

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
