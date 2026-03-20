from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
import json
import requests

historico = []

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"msg": "Chatbot com IA local rodando 🚀"}


@app.get("/chat")
def chat(pergunta: str):

    global historico

    contexto = """
    Você é um assistente de TI interno especialista em Protheus.
    Responda de forma clara e objetiva.
    """

    historico.append(f"Usuário: {pergunta}")

    prompt = contexto + "\n\n" + "\n".join(historico) + "\nAssistente:"

    def gerar():
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3",
                "prompt": prompt,
                "stream": True
            },
            stream=True
        )

        resposta_completa = ""

        for linha in response.iter_lines():
            if linha:
                dados = json.loads(linha.decode("utf-8"))
                if "response" in dados:
                    texto = dados["response"]
                    resposta_completa += texto
                    yield texto

        historico.append(f"Assistente: {resposta_completa}")

    return StreamingResponse(gerar(), media_type="text/plain")

