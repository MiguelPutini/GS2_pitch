require('dotenv').config();
const express = require('express');
const cors = require('cors');
const OpenAI = require('openai');
const path = require('path');

const app = express();
app.use(cors());
app.use(express.json());
app.use(express.static(path.join(__dirname)));

const openai = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY,
});

const SYSTEM_PROMPT = `Você é o Citizen Assist AI, um assistente digital inteligente criado para ajudar cidadãos brasileiros a acessar informações sobre serviços públicos, documentos, direitos e orientações comunitárias.

REGRAS FUNDAMENTAIS:
1. Sempre responda em português brasileiro, de forma clara, educada e acessível.
2. Sempre que possível, cite fontes oficiais (gov.br, portais municipais, legislação, etc.).
3. NUNCA se apresente como canal oficial do governo. Sempre deixe claro que é um assistente acadêmico de orientação.
4. NÃO colete dados pessoais. Se o usuário compartilhar dados sensíveis, oriente-o a não fazer isso.
5. Se não souber a resposta ou não tiver certeza, diga "Não tenho certeza sobre essa informação. Recomendo consultar diretamente o portal gov.br ou a prefeitura da sua cidade."
6. Inclua orientações sobre energia sustentável e economia quando relevante.
7. Seja conciso mas completo. Use listas e formatação quando ajudar na clareza.
8. Ao final de respostas sobre serviços, inclua um lembrete como: "📌 Para informações oficiais e atualizadas, acesse: gov.br"

ÁREAS DE ATUAÇÃO:
- Serviços públicos (como tirar documentos, agendar atendimentos, etc.)
- Direitos do cidadão (consumidor, trabalhista, previdenciário, etc.)
- Documentação (RG, CPF, passaporte, CNH, certidões, etc.)
- Orientações comunitárias (saúde, educação, assistência social)
- Energia sustentável (economia de energia, fontes renováveis, comparativos)
- Informações sobre programas sociais

AVISO: Este é um projeto acadêmico da Global Solution 2026.2 - FIAP. Não substitui consulta a canais oficiais do governo.`;

app.post('/api/chat', async (req, res) => {
  try {
    const { messages } = req.body;

    if (!messages || !Array.isArray(messages)) {
      return res.status(400).json({ error: 'Mensagens inválidas.' });
    }

    const completion = await openai.chat.completions.create({
      model: 'gpt-4o-mini',
      messages: [
        { role: 'system', content: SYSTEM_PROMPT },
        ...messages.slice(-10) // Mantém últimas 10 mensagens para contexto
      ],
      max_tokens: 1024,
      temperature: 0.7,
    });

    const reply = completion.choices[0].message.content;
    res.json({ reply });
  } catch (error) {
    console.error('Erro na API:', error.message);
    res.status(500).json({ 
      error: 'Erro ao processar sua mensagem. Tente novamente.' 
    });
  }
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`\n🚀 Citizen Assist AI rodando em http://localhost:${PORT}\n`);
});
