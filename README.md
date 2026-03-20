# 🤖 Chatbot com IA Local (Python + FastAPI + Ollama) — Streaming em Tempo Real

Exemplo profissional de um chatbot com IA rodando localmente, com **respostas em streaming (tempo real)** no estilo ChatGPT, utilizando FastAPI no backend e uma interface web simples.

---

## ✨ Destaques

- ⚡ **Streaming em tempo real** (token a token)
- 🧠 **IA local** com Ollama (sem custo por requisição)
- 🌐 Interface web simples (HTML + JavaScript)
- ⌨️ Envio com Enter + scroll automático
- 🧩 Backend limpo com FastAPI
- 🔌 Pronto para integrações (ERP/Protheus, banco, documentos)

---

## 🏗️ Arquitetura

flowchart LR
  A[Browser (HTML/JS)] -->|HTTP /chat| B[FastAPI]
  B -->|stream| C[Ollama (llama3)]
  C --> B --> A
```

---

## 🧰 Tecnologias

- **Backend:** Python, FastAPI, Uvicorn
- **IA local:** Ollama (modelo Llama3)
- **Frontend:** HTML, CSS, JavaScript (Fetch + Streams)
- **Outros:** requests

---

## 📁 Estrutura do Projeto

```text
api-protheus-ia/
├── main.py
├── index.html
├── requirements.txt
├── README.md
├── .gitignore
└── docs/
```

---

## ⚙️ Instalação

### 1) Clonar o repositório

```bash
git clone https://github.com/robertoemilio/chatbot-ia-protheus.git
cd chatbot-ia-protheus
```

---

### 2) Criar ambiente virtual

```bash
python -m venv venv
venv\Scripts\activate  # Windows
```

---

### 3) Instalar dependências

```bash
pip install -r requirements.txt
```

---

### 4) Instalar o Ollama

Baixe em: https://ollama.com

Depois execute:

```bash
ollama run llama3
```

---

### 5) Rodar o servidor

```bash
uvicorn main:app --reload
```

---

### 6) Abrir o chat

Abra o arquivo:

```bash
index.html
```

---

## 🔌 API

### Endpoint: `/chat`

**Método:** GET  

**Parâmetro:**
- `pergunta` (string)

**Exemplo:**

```bash
http://127.0.0.1:8000/chat?pergunta=Como%20emitir%20NF%3F
```

👉 A resposta é retornada em **streaming (texto contínuo)**.

---

## 🧪 Exemplo de Uso

**Pergunta:**
```
Como emitir NF no Protheus?
```

**Resposta:**
```
Para emitir nota fiscal, acesse o SIGAFAT, gere o pedido e realize o faturamento...
```

---

## 🚀 Roadmap (Próximos Passos)

- [ ] Memória de conversa (por usuário)
- [ ] IA com leitura de documentos (PDF / RAG)
- [ ] Autenticação e multiusuário
- [ ] Integração com Protheus (REST ADVPL)
- [ ] Persistência em banco de dados

---

## 👨‍💻 Autor

**Roberto Emílio**  
Supervisor de TI | Especialista em Protheus | IA aplicada

---

## 📄 Licença

MIT
