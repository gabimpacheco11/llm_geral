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