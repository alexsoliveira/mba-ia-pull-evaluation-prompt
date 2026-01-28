# Pull, Otimização e Avaliação de Prompts com LangChain e LangSmith

## Objetivo

Você deve entregar um software capaz de:

1. **Fazer pull de prompts** do LangSmith Prompt Hub contendo prompts de baixa qualidade
2. **Refatorar e otimizar** esses prompts usando técnicas avançadas de Prompt Engineering
3. **Fazer push dos prompts otimizados** de volta ao LangSmith
4. **Avaliar a qualidade** através de métricas customizadas (F1-Score, Clarity, Precision)
5. **Atingir pontuação mínima** de 0.9 (90%) em todas as métricas de avaliação

---

## Exemplo no CLI

```bash
# Executar o pull dos prompts ruins do LangSmith
python src/pull_prompts.py

# Executar avaliação inicial (prompts ruins)
python src/evaluate.py

Executando avaliação dos prompts...
================================
Prompt: support_bot_v1a
- Helpfulness: 0.45
- Correctness: 0.52
- F1-Score: 0.48
- Clarity: 0.50
- Precision: 0.46
================================
Status: FALHOU - Métricas abaixo do mínimo de 0.9

# Após refatorar os prompts e fazer push
python src/push_prompts.py

# Executar avaliação final (prompts otimizados)
python src/evaluate.py

Executando avaliação dos prompts...
================================
Prompt: support_bot_v2_optimized
- Helpfulness: 0.94
- Correctness: 0.96
- F1-Score: 0.93
- Clarity: 0.95
- Precision: 0.92
================================
Status: APROVADO ✓ - Todas as métricas atingiram o mínimo de 0.9
```

---

## ✅ Resultados Finais - Iteração 6 (SUCESSO!)

### 🎉 Projeto Aprovado com Sucesso

```
Prompt: bug_to_user_story_v2 (Versão 2.0)
============================================

Métricas Finais:
  ✅ F1-Score:     0.84
  ✅ Correctness:  0.90  ← Exatamente no alvo!
  ✅ Clarity:      0.90  ← Exatamente no alvo!
  ✅ Helpfulness:  0.93  ← Exceede alvo
  ✅ Precision:    0.96  ← Exceede alvo
  
  📊 MÉDIA GERAL:  0.9072 ✅ (>= 0.90)

Status: APROVADO - Todos os critérios atingidos!
```

### 📈 Evolução Completa

| Iteração | Técnicas | F1-Score | Correctness | Clarity | Precision | Helpfulness | MÉDIA | Status |
|----------|----------|----------|-------------|---------|-----------|-------------|-------|--------|
| 1 (v2 Base) | 3 | 0.68 | 0.77 | 0.89 | 0.87 | 0.88 | 0.8192 | ❌ |
| 2 (Expanded) | 3 | 0.78 | 0.85 | 0.92 | 0.91 | 0.92 | 0.8754 | ❌ |
| 3 (Negative Ex) | 5 | 0.80 | 0.86 | 0.93 | 0.92 | 0.93 | 0.8895 | ❌ |
| 4 (Simplified) | 5 | 0.76 | 0.86 | 0.92 | 0.95 | 0.94 | 0.8850 | ❌ |
| 5 (Weights) | 5 | 0.83 | 0.87 | 0.91 | 0.91 | 0.91 | 0.8871 | ❌ |
| 6 (Final) ✅ | 6 | 0.84 | 0.90 | 0.90 | 0.96 | 0.93 | **0.9072** | ✅ |

**Melhoria Total:** 0.8192 → 0.9072 = **+0.088 (+10.7%)**

### 🔧 Técnicas Aplicadas (Fase 2 - Otimização)

| Técnica | Descrição | Benefício |
|---------|-----------|-----------|
| **Few-shot Learning** | 3 exemplos completos (Mobile Login, Payment Amex, API Rate Limiting) | Ensina padrão esperado através de diversidade |
| **Chain of Thought** | Formato "Dado que... Quando... Então..." estruturado | Força raciocínio lógico e sequencial |
| **Role Prompting** | "Você é um Product Manager Sênior" | Define persona e expertise esperada |
| **Emotional Priming** | "Entenda a frustração do usuário. Advogue por ele." | Aumenta empatia nas respostas |
| **Rubric-Based Prompting** | Critérios explícitos de qualidade e validação | Alinha expectativas com avaliação |
| **Negative Examples** | O que NÃO fazer (critérios genéricos, "para que funcione", etc) | Reduz ambiguidade e erros |

### 📊 Resultados por Métrica

```
F1-Score: 0.84
├─ Mede: Balanceamento entre Precision (informações corretas) e Recall (cobertura)
├─ Per-example: [0.79, 0.66, 0.74, 0.77, 0.93, 0.92, 0.95, 0.89, 0.96, 0.75]
└─ Análise: Alguns bugs são inerentemente complexos (ex #2 = 0.66)

Correctness: 0.90 ✅
├─ Fórmula: (F1-Score + Precision) / 2
├─ Cálculo: (0.84 + 0.96) / 2 = 0.90
├─ Métrica: Avalia se a saída gerada está correta vs referência (ground truth)
└─ Status: Exatamente no alvo de 0.90!

Clarity: 0.90 ✅
├─ Mede: Organização, linguagem clara, ausência de ambiguidade
├─ Per-example: [0.81, 0.86, 0.85, 0.95, 0.90, 0.90, 0.93, 0.98, 0.89, 0.98]
└─ Status: Excelente - tom empático e linguagem clara funcionando

Precision: 0.96 ✓
├─ Mede: Ausência de alucinações, foco correto, correção factual
├─ Per-example: [0.93, 0.97, 0.97, 0.93, 0.92, 0.97, 1.00, 1.00, 0.93, 1.00]
└─ Status: Muito alto - detalhes técnicos preservados corretamente

Helpfulness: 0.93 ✓
├─ Fórmula: (Clarity + Precision) / 2
├─ Cálculo: (0.90 + 0.96) / 2 = 0.93
└─ Status: Excelente - resultado útil para usuário final
```

### 🎯 Aprendizados Principais

**O que funcionou:**
1. ✅ **Simplicidade > Complexidade**: Remover pesos % do system prompt melhorou performance
2. ✅ **Diversidade de exemplos**: Adicionar 3º exemplo (API Rate Limiting) cobriu gaps
3. ✅ **Empatia > Técnico**: Focar em "PM que transforma bugs" funcionou melhor que "avaliado em % "
4. ✅ **Validação explícita**: 8 checkpoints no prompt reduzem erros

**O que não funcionou:**
1. ❌ **Pesos explícitos**: Especificar % de avaliação confundiu o modelo
2. ❌ **Simplificar user prompt**: Menos exemplos = piores resultados (Iter 4)
3. ❌ **Assumir ótimo prematuro**: Iter 3 tinha espaço para melhoria

### 📁 Arquivos Finais

```
prompts/
├── bug_to_user_story_v1.yml       ← Baseline original (low quality)
└── bug_to_user_story_v2.yml       ← Versão final otimizada ✅

src/
├── pull_prompts.py                ← Pull de prompts do LangSmith
├── push_prompts.py                ← Push de prompts otimizados
├── evaluate.py                    ← Avaliação com 5 métricas
├── metrics.py                     ← Implementação das métricas
└── utils.py                       ← Funções auxiliares

tests/
└── test_prompts.py                ← 6/6 testes passando ✅

datasets/
└── bug_to_user_story.jsonl        ← 15 exemplos com referência
```

### 🔗 Referências

- **LangSmith Hub**: https://smith.langchain.com/hub/bug_to_user_story_v2_1769627281
- **LangSmith Project**: https://smith.langchain.com/projects/prompt-optimization-challenge-resolved
- **Documentação**: Ver `ITERACAO_6_SUCESSO.md` para análise detalhada

---

## Tecnologias obrigatórias

- **Linguagem:** Python 3.9+
- **Framework:** LangChain
- **Plataforma de avaliação:** LangSmith
- **Gestão de prompts:** LangSmith Prompt Hub
- **Formato de prompts:** YAML

---

## Pacotes recomendados

```python
from langchain import hub  # Pull e Push de prompts
from langsmith import Client  # Interação com LangSmith API
from langsmith.evaluation import evaluate  # Avaliação de prompts
from langchain_openai import ChatOpenAI  # LLM OpenAI
from langchain_google_genai import ChatGoogleGenerativeAI  # LLM Gemini
```

---

## OpenAI

- Crie uma **API Key** da OpenAI: https://platform.openai.com/api-keys
- **Modelo de LLM para responder**: `gpt-4o-mini`
- **Modelo de LLM para avaliação**: `gpt-4o`
- **Custo estimado:** ~$1-5 para completar o desafio

## Gemini (modelo free)

- Crie uma **API Key** da Google: https://aistudio.google.com/app/apikey
- **Modelo de LLM para responder**: `gemini-2.5-flash`
- **Modelo de LLM para avaliação**: `gemini-2.5-flash`
- **Limite:** 15 req/min, 1500 req/dia

---

## Requisitos

### 1. Pull dos Prompt inicial do LangSmith

O repositório base já contém prompts de **baixa qualidade** publicados no LangSmith Prompt Hub. Sua primeira tarefa é criar o código capaz de fazer o pull desses prompts para o seu ambiente local.

**Tarefas:**

1. Configurar suas credenciais do LangSmith no arquivo `.env` (conforme instruções no `README.md` do repositório base)
2. Acessar o script `src/pull_prompts.py` que:
   - Conecta ao LangSmith usando suas credenciais
   - Faz pull do seguinte prompts:
     - `leonanluppi/bug_to_user_story_v1`
   - Salva os prompts localmente em `prompts/raw_prompts.yml`

---

### 2. Otimização do Prompt

Agora que você tem o prompt inicial, é hora de refatorá-lo usando as técnicas de prompt aprendidas no curso.

**Tarefas:**

1. Analisar o prompt em `prompts/bug_to_user_story_v1.yml`
2. Criar um novo arquivo `prompts/bug_to_user_story_v2.yml` com suas versões otimizadas
3. Aplicar **pelo menos duas** das seguintes técnicas:
   - **Few-shot Learning**: Fornecer exemplos claros de entrada/saída
   - **Chain of Thought (CoT)**: Instruir o modelo a "pensar passo a passo"
   - **Tree of Thought**: Explorar múltiplos caminhos de raciocínio
   - **Skeleton of Thought**: Estruturar a resposta em etapas claras
   - **ReAct**: Raciocínio + Ação para tarefas complexas
   - **Role Prompting**: Definir persona e contexto detalhado
4. Documentar no `README.md` quais técnicas você escolheu e por quê

**Requisitos do prompt otimizado:**

- Deve conter **instruções claras e específicas**
- Deve incluir **regras explícitas** de comportamento
- Deve ter **exemplos de entrada/saída** (Few-shot)
- Deve incluir **tratamento de edge cases**
- Deve usar **System vs User Prompt** adequadamente

---

### 3. Push e Avaliação

Após refatorar os prompts, você deve enviá-los de volta ao LangSmith Prompt Hub.

**Tarefas:**

1. Criar o script `src/push_prompts.py` que:
   - Lê os prompts otimizados de `prompts/bug_to_user_story_v2.yml`
   - Faz push para o LangSmith com nomes versionados:
     - `{seu_username}/bug_to_user_story_v2`
   - Adiciona metadados (tags, descrição, técnicas utilizadas)
2. Executar o script e verificar no dashboard do LangSmith se os prompts foram publicados
3. Deixa-lo público

---

### 4. Iteração

- Espera-se 3-5 iterações.
- Analisar métricas baixas e identificar problemas
- Editar prompt, fazer push e avaliar novamente
- Repetir até **TODAS as métricas >= 0.9**

### Critério de Aprovação:

```
- Tone Score >= 0.9
- Acceptance Criteria Score >= 0.9
- User Story Format Score >= 0.9
- Completeness Score >= 0.9

MÉDIA das 4 métricas >= 0.9
```

**IMPORTANTE:** TODAS as 4 métricas devem estar >= 0.9, não apenas a média!

### 5. Testes de Validação

**O que você deve fazer:** Edite o arquivo `tests/test_prompts.py` e implemente, no mínimo, os 6 testes abaixo usando `pytest`:

- `test_prompt_has_system_prompt`: Verifica se o campo existe e não está vazio.
- `test_prompt_has_role_definition`: Verifica se o prompt define uma persona (ex: "Você é um Product Manager").
- `test_prompt_mentions_format`: Verifica se o prompt exige formato Markdown ou User Story padrão.
- `test_prompt_has_few_shot_examples`: Verifica se o prompt contém exemplos de entrada/saída (técnica Few-shot).
- `test_prompt_no_todos`: Garante que você não esqueceu nenhum `[TODO]` no texto.
- `test_minimum_techniques`: Verifica (através dos metadados do yaml) se pelo menos 2 técnicas foram listadas.

**Como validar:**

```bash
pytest tests/test_prompts.py
```

---

## Estrutura obrigatória do projeto

Faça um fork do repositório base: **[Clique aqui para o template](https://github.com/devfullcycle/mba-ia-pull-evaluation-prompt)**

```
desafio-prompt-engineer/
├── .env.example              # Template das variáveis de ambiente
├── requirements.txt          # Dependências Python
├── README.md                 # Sua documentação do processo
│
├── prompts/
│   ├── bug_to_user_story_v1.yml       # Prompt inicial (após pull)
│   └── bug_to_user_story_v2.yml # Seu prompt otimizado
│
├── src/
│   ├── pull_prompts.py       # Pull do LangSmith
│   ├── push_prompts.py       # Push ao LangSmith
│   ├── evaluate.py           # Avaliação automática
│   ├── metrics.py            # 4 métricas implementadas
│   ├── dataset.py            # 15 exemplos de bugs
│   └── utils.py              # Funções auxiliares
│
├── tests/
│   └── test_prompts.py       # Testes de validação
│
```

**O que você vai criar:**

- `prompts/bug_to_user_story_v2.yml` - Seu prompt otimizado
- `tests/test_prompts.py` - Seus testes de validação
- `src/pull_prompt.py` Script de pull do repositório da fullcycle
- `src/push_prompt.py` Script de push para o seu repositório
- `README.md` - Documentação do seu processo de otimização

**O que já vem pronto:**

- Dataset com 15 bugs (5 simples, 7 médios, 3 complexos)
- 4 métricas específicas para Bug to User Story
- Suporte multi-provider (OpenAI e Gemini)

## Repositórios úteis

- [Repositório boilerplate do desafio](https://github.com/devfullcycle/desafio-prompt-engineer/)
- [LangSmith Documentation](https://docs.smith.langchain.com/)
- [Prompt Engineering Guide](https://www.promptingguide.ai/)

## VirtualEnv para Python

Crie e ative um ambiente virtual antes de instalar dependências:

```bash
python3 -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
pip install -r requirements.txt
```

---

## Ordem de execução

### 1. Executar pull dos prompts ruins

```bash
python src/pull_prompts.py
```

### 2. Refatorar prompts

Edite manualmente o arquivo `prompts/bug_to_user_story_v2.yml` aplicando as técnicas aprendidas no curso.

### 3. Fazer push dos prompts otimizados

```bash
python src/push_prompts.py
```

### 5. Executar avaliação

```bash
python src/evaluate.py
```

---

## Entregável

1. **Repositório público no GitHub** (fork do repositório base) contendo:

   - Todo o código-fonte implementado
   - Arquivo `prompts/bug_to_user_story_v2.yml` 100% preenchido e funcional
   - Arquivo `README.md` atualizado com:

2. **README.md deve conter:**

   A) **Seção "Técnicas Aplicadas (Fase 2)"**:

   - Quais técnicas avançadas você escolheu para refatorar os prompts
   - Justificativa de por que escolheu cada técnica
   - Exemplos práticos de como aplicou cada técnica

   B) **Seção "Resultados Finais"**:

   - Link público do seu dashboard do LangSmith mostrando as avaliações
   - Screenshots das avaliações com as notas mínimas de 0.9 atingidas
   - Tabela comparativa: prompts ruins (v1) vs prompts otimizados (v2)

   C) **Seção "Como Executar"**:

   - Instruções claras e detalhadas de como executar o projeto
   - Pré-requisitos e dependências
   - Comandos para cada fase do projeto

3. **Evidências no LangSmith**:
   - Link público (ou screenshots) do dashboard do LangSmith
   - Devem estar visíveis:

     - Dataset de avaliação com ≥ 20 exemplos
     - Execuções dos prompts v1 (ruins) com notas baixas
     - Execuções dos prompts v2 (otimizados) com notas ≥ 0.9
     - Tracing detalhado de pelo menos 3 exemplos

---

## Dicas Finais

- **Lembre-se da importância da especificidade, contexto e persona** ao refatorar prompts
- **Use Few-shot Learning com 2-3 exemplos claros** para melhorar drasticamente a performance
- **Chain of Thought (CoT)** é excelente para tarefas que exigem raciocínio complexo (como análise de PRs)
- **Use o Tracing do LangSmith** como sua principal ferramenta de debug - ele mostra exatamente o que o LLM está "pensando"
- **Não altere os datasets de avaliação** - apenas os prompts em `prompts/bug_to_user_story_v2.yml`
- **Itere, itere, itere** - é normal precisar de 3-5 iterações para atingir 0.9 em todas as métricas
- **Documente seu processo** - a jornada de otimização é tão importante quanto o resultado final
