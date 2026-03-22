# 🤖 Telegram AI Bot (Groq Cloud)

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Telegram API](https://img.shields.io/badge/Telegram-Bot%20API-blue.svg)](https://core.telegram.org/bots/api)
[![Groq](https://img.shields.io/badge/AI-Groq%20Cloud-orange.svg)](https://groq.com/)

Um assistente pessoal para Telegram integrado à API do **Groq Cloud**, utilizando o modelo **Llama 3.3 70b** para respostas ultrarrápidas e inteligentes. O bot possui memória de contexto para manter conversas fluidas.

---

## ✨ Funcionalidades

- ⚡ **Respostas Instantâneas:** Baixíssima latência graças à infraestrutura da Groq.
- 🧠 **Memória de Curto Prazo:** Mantém o histórico das últimas 10 mensagens por usuário para entender o contexto.
- 🛠️ **Fácil Configuração:** Utiliza variáveis de ambiente para segurança das chaves de API.
- 🐍 **Totalmente Assíncrono:** Desenvolvido com `python-telegram-bot` v20+.

---

## 🚀 Tecnologias Utilizadas

- Python 3.10+
- python-telegram-bot — Framework para bots do Telegram
- Requests — Para chamadas HTTP
- Groq Cloud API — Processamento de IA em alta velocidade

---

## 🧩 Arquitetura

O funcionamento do bot segue o fluxo:

1. Usuário envia mensagem no Telegram  
2. O bot recebe via polling  
3. A mensagem é enviada para a API do Groq  
4. A IA processa e retorna a resposta  
5. O bot responde ao usuário  
6. O histórico é armazenado temporariamente em memória  

---

## 📸 Exemplo de uso

**Usuário:** Olá  
**Bot:** Olá! Como posso te ajudar hoje?

---

## 📦 Como Instalar e Rodar

### 1. Requisitos

Você precisará de:

- Um **Token de Bot** (obtido no BotFather)
- Uma **API Key do Groq** (obtida no console da Groq)

---

### 2. Clonar o repositório

```bash
git clone https://github.com/mateuspauperio/bot-telegram-groq.git
cd bot-telegram-groq
