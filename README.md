# Citizen Assist AI 🏛️🤖
### Global Solution 2026.2 — FIAP (1º Ano Ciência da Computação)
**Tema:** *CitizenTech: Da cidade ao campo, tecnologia para a vida cotidiana*

---

### 👥 Integrantes da Equipe (Trio):
- **Miguel Putini** — RM 571624
- **Alexandre Rizzi** — RM 569621
- **Lucas Klein de Veiga** — RM 570029

---

## 📌 Visão Geral do Projeto

O **Citizen Assist AI** é um assistente digital inteligente desenvolvido em **Python** para orientar o cidadão brasileiro sobre serviços públicos, documentos essenciais (como a nova Carteira de Identidade Nacional - CIN), direitos e sustentabilidade energética.

### Destaques da Solução:
- **Backend Nativo em Python (`main.py`):** Utiliza Flask com orquestração segura da API da OpenAI (`gpt-4o-mini`).
- **Arquitetura Zero-Database (LGPD Compliant):** Não necessita nem armazena consultas em banco de dados, protegendo a privacidade dos cidadãos.
- **Design Não Emblemático:** Visual moderno, limpo e tecnológico (sem brasões ou falsas representações de ser canal oficial do governo).
- **Acessibilidade Básica:** Botões de redimensionamento de fonte (`A+` / `A-`), suporte a leitura em voz alta (Web Speech API) e modo escuro/claro.
- **Transparência e Fontes Oficiais:** Cita fontes oficiais autênticas (como `gov.br`, portais municipais e legislações vigentes).
- **Módulo de Energia Sustentável:** Informações sobre economia na conta de luz, Tarifa Social de Energia Elétrica e viabilidade de energia solar.
- **Métricas Acadêmicas:** Medição do tempo de resposta da IA em segundos e avaliação de assertividade pelos usuários.

---

## 🚀 Como Executar o Projeto em Python

### 1. Inicialização Direta pelo Terminal:
No diretório do projeto, basta rodar:
```bash
python main.py
```
> O servidor iniciará em `http://localhost:3000` (ou na porta definida no `.env`) e o navegador será aberto automaticamente!

---

### 2. Ou Duplo Clique no Windows:
Basta dar **duplo clique** no arquivo:
👉 `INICIAR_PROJETO.bat`

---

### Instalação de Dependências (se necessário em outro computador):
```bash
pip install -r requirements.txt
```

---

## 📁 Estrutura de Arquivos

```
gs_video_pitch/
│
├── main.py               # Servidor principal da aplicação em Python (Flask + OpenAI)
├── requirements.txt      # Dependências do Python (Flask, OpenAI, Dotenv, etc.)
├── index.html            # Interface moderna SPA (HTML5, CSS3 Glassmorphism, JS)
├── .env                  # Chave da API OpenAI e porta de execução
├── .gitignore            # Ignora arquivos sensíveis e temporários
├── INICIAR_PROJETO.bat   # Script para rodar com 1 clique (executa python main.py)
│
├── link_video_pitch.txt  # Arquivo para entrega no portal com o link do YouTube
└── README.md             # Esta documentação
```

---

## 🎥 Orientações para a Gravação do Vídeo Pitch

Consulte o arquivo de roteiro completo:
📄 `roteiro-video-pitch.md` (localizado nos artefatos do projeto)

### Checklist Obrigatório da FIAP:
1. **Duração:** Máximo de **3 minutos**.
2. **Narração Humana Obrigatória:** Não use voz sintetizada por IA no vídeo.
3. **Visibilidade no YouTube:** Configurado como **Não Listado**.
4. **Comentários do YouTube:**
   - Indicar se a entrega é **Individual**, **Dupla** ou **Trio**.
   - Colocar os **Nomes completos** e **RMs** de todos os integrantes.
5. **Entrega no Portal:** Apenas **1 integrante** envia o arquivo `link_video_pitch.txt`.
