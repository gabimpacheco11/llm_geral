# certificar se o pip esta instalado:
python -m ensurepip

# Atualizando o pip:
python -m pip install --upgrade pip

# Criando variavel de ambiente.
    # Cada projeto pode ter suas próprias versões de pacotes sem interferir nos outros.
    # Com um ambiente virtual, os pacotes ficam organizados apenas dentro do projeto.
        # Isso resolve erros como "Permission Denied" ao tentar instalar algo no Python global.


python -m venv venv
venv\Scripts\activate

# Bibliotecas para o projeto:
pip install -q langchain
pip install -q langchain-community
pip install -q langchain-huggingface
pip install -q langchainhub
pip install -q langchain_chroma
pip install bitsandbytes-cuda110 bitsandbytes

=======================================================================================================================

                Documentação:


**1. Introdução**
- Descrição do projeto: O projeto visa construir uma plataforma de conversão de documentos em texto para consulta e resposta utilizando a linguagem de programação Python e as bibliotecas LangChain e ChromaDB.
- Objetivos do projeto: O objetivo principal é fornecer uma interface amigável para usuários finais para pesquisar e interagir com documentos, além de permitir a geração de respostas baseadas em contexto.

**2. Arquitetura do Projeto**
- Visão geral: O projeto é dividido em três aplicativos principais: `projeto1.py`, `projeto2.py`, e `projeto3.py`. O `projeto1.py` é responsável por converter documentos em texto, enquanto os outros dois aplicativos (`projeto2.py` e `projeto3.py`) lidam com a indexação e a geração de respostas.
- Comunicação entre aplicativos: Os aplicativos se comunicam através de uploads de arquivos e troca de mensagens. O `projeto3.py` é responsável por carregar os documentos, dividi-los em pedaços de texto, indexá-los no ChromaDB, e configurar o retriever. O `projeto2.py` é responsável por receber consultas do usuário, recuperar documentos relevantes usando o retriever, e gerar respostas baseadas em contexto.

**3. Requisitos e Dependências**
- Requisitos: O projeto requer Python 3.9 ou superior, bem como as bibliotecas LangChain, ChromaDB, e outras dependências listadas no arquivo `requirements.txt`.
- Dependências:
  - LangChain: `langchain==0.3.15`
  - LangChain-Community: `langchain-community==0.3.15`
  - LangChain-HuggingFace: `langchain-huggingface`
  - LangChainHub: `langchainhub`
  - LangChain-Chroma: `langchain_chroma`
  - LangChain-Ollama: `langchain_ollama`
  - LangChain-OpenAI: `langchain_openai`
  - BitsAndBytes-CUDA110: `bitsandbytes-cuda110`
  - BitsAndBytes: `bitsandbytes`

**4. Configuração e Instalação**
- Criar um ambiente virtual: Siga as instruções para criar um ambiente virtual usando o Python e o gerenciador de pacotes de sua preferência (como `venv` ou `conda`).
- Instalar dependências: Instale as dependências listadas no arquivo `requirements.txt` usando o comando `pip install -r requirements.txt`.

**5. Execução do Projeto**
- Executar os aplicativos: Execute os aplicativos `projeto1.py`, `projeto2.py`, e `projeto3.py` em terminais separados ou usando um gerenciador de tarefas.
- Acessar a interface: Acesse a interface do usuário através de um navegador web, inserindo a URL `http://localhost:8501` (ou a porta especificada no arquivo de configuração do Streamlit).

**6. Funcionalidades**
- Conversão de documentos em texto: O `projeto1.py` é responsável por converter documentos em formatos comuns (como PDF, Word, e outros) em texto legível.
- Indexação de documentos: O `projeto3.py` é responsável por carregar os documentos convertidos em texto, dividi-los em pedaços de texto, e armazená-los no ChromaDB para indexação e recuperação.
- Geração de respostas: O `projeto2.py` é responsável por receber consultas do usuário, recuperar documentos relevantes usando o retriever, e gerar respostas baseadas em contexto.

**7. Testes e Depuração**
- Testes unitários: Não há testes unitários disponíveis no repositório.
- Testes de integração: Não há testes de integração disponíveis no repositório.
- Depuração: Utilize ferramentas de depuração do Python, como `pdb`, `ipdb`, ou `PyCharm`, para depurar e resolver problemas no código.

**8. Melhorias e Contribuições**
- Melhorias: O código pode ser melhorado para lidar com erros e exceções, além de ser otimizado para desempenho.
- Contribuições: Contribuições são sempre bem-vindas! Sinta-se à vontade para abrir pull requests ou reportar problemas no repositório.

**9. Referências**
- Documentação LangChain: https://python.langchain.com/
- Documentação ChromaDB: https://docs.trychroma.com/
- Documentação Streamlit: https://docs.streamlit.io/

