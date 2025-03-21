# Testing script for LLMs

from langchain_huggingface import ChatHuggingFace
from langchain_community.llms import HuggingFaceHub
from langchain_ollama import ChatOllama
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

# Carrega as informações do arquivo de configuração .env 
load_dotenv()

# Exemplo com Hugging Face
llm = HuggingFaceHub(
    repo_id="meta-llama/Meta-Llama-3-8B-Instruct",
    model_kwargs={
        "temperature": 0.1,
        "return_full_text": False,
        "max_new_tokens": 512,
        #"stop": ["<|eot_id|>"],
        # demais parâmetros que desejar
    }
)

# Definição do prompt 
system_prompt = "Você é um assistente prestativo e está respondendo perguntas gerais."
user_prompt = "{input}"

# Tokens de inicio (token_s) e token de final (token_e)
token_s, token_e = "<|begin_of_text|><|start_header_id|>system<|end_header_id|>", "<|eot_id|><|start_header_id|>assistant<|end_header_id|>"

# Criação do prompt
prompt = ChatPromptTemplate.from_messages([
    ("system", token_s + system_prompt),
    ("user", user_prompt + token_e)
])

chain = prompt | llm

input = "Explique para mim em até 1 parágrafo o conceito de redes neurais, de forma clara e objetiva"

res = chain.invoke({"input": input})
print(res)
print("-----")

### Exemplo com Ollama
""" 
llm = ChatOllama(
    model="phi3",
    temperature=0.1
)

chain3 = prompt | llm
res = chain3.invoke({"input": input})
print(res.content) """
