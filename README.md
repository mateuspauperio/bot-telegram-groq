# 🤖 Telegram AI Bot (Groq Cloud)

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Telegram API](https://img.shields.io/badge/Telegram-Bot%20API-blue.svg)](https://core.telegram.org/bots/api)
[![Groq](https://img.shields.io/badge/AI-Groq%20Cloud-orange.svg)](https://groq.com/)

Um assistente pessoal para Telegram integrado à API do **Groq Cloud**, utilizando o modelo **Llama 3.3 70b** para respostas ultrarrápidas e inteligentes. O bot possui memória de contexto para manter conversas fluidas.

## ✨ Funcionalidades

- ⚡ **Respostas Instantâneas:** Baixíssima latência graças à infraestrutura da Groq.
- 🧠 **Memória de Curto Prazo:** Mantém o histórico das últimas 10 mensagens por usuário para entender o contexto.
- 🛠️ **Fácil Configuração:** Utiliza variáveis de ambiente para segurança das chaves de API.
- 🐍 **Totalmente Assíncrono:** Desenvolvido com `python-telegram-bot` v20+.

## 🚀 Tecnologias Utilizadas

* [Python 3.10+](https://www.python.org/)
* [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot) - Framework para bots de Telegram.
* [Requests](https://requests.readthedocs.io/) - Para chamadas à API do Groq.
* [Groq Cloud API](https://console.groq.com/) - Processamento de LLM em alta velocidade.

## 📦 Como Instalar e Rodar

### 1. Requisitos
Você precisará de:
- Um **Token de Bot** (obtido no [@BotFather](https://t.me/botfather)).
- Uma **API Key do Groq** (obtida no [Groq Console](https://console.groq.com/)).

### 2. Clonar o Repositório
```bash
git clone [https://github.com/mateuspauperio/bot-telegram-groq.git](https://github.com/mateuspauperio/bot-telegram-groq.git)
cd bot-telegram-groq
