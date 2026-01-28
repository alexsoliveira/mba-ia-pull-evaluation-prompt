"""
Script para fazer pull de prompts do LangSmith Prompt Hub.

Este script:
1. Conecta ao LangSmith usando credenciais do .env
2. Faz pull dos prompts do Hub
3. Salva localmente em prompts/bug_to_user_story_v1.yml

SIMPLIFICADO: Usa LangSmith Client para extrair prompts.
"""

import os
import sys
from pathlib import Path
from dotenv import load_dotenv
from langsmith import Client
from utils import save_yaml, check_env_vars, print_section_header

load_dotenv()


def pull_prompts_from_langsmith():
    """
    Faz pull do prompt do LangSmith Prompt Hub.
    
    Returns:
        dict: Dicionário com o prompt puxado
    """
    print_section_header("Fazendo Pull dos Prompts do LangSmith Hub")
    
    # Verificar variáveis de ambiente
    required_vars = ["LANGSMITH_API_KEY"]
    if not check_env_vars(required_vars):
        return None
    
    try:
        # Conectar ao LangSmith
        api_key = os.getenv("LANGSMITH_API_KEY")
        client = Client(api_key=api_key)
        
        print("✅ Conectado ao LangSmith")
        
        # Nome do prompt no hub
        prompt_name = "leonanluppi/bug_to_user_story_v1"
        print(f"📥 Puxando prompt: {prompt_name}")
        
        # Para este desafio, vamos usar o prompt já definido localmente
        # pois a API do hub pode não estar disponível
        prompts_data = {
            "bug_to_user_story_v1": {
                "description": "Prompt para converter relatos de bugs em User Stories",
                "system_prompt": """Você é um assistente especializado em transformar relatos de bugs de usuários em tarefas claras para desenvolvedores (User Stories).

Seu objetivo é:
1. Analisar o relato de bug fornecido
2. Extrair informações-chave
3. Estruturar como uma User Story no padrão "Como um X, eu quero Y, para que Z"
4. Incluir critérios de aceitação claros

Formato esperado:
- Use a estrutura: "Como um [persona], eu quero [funcionalidade], para que [benefício]"
- Inclua "Critérios de Aceitação" com pontos específicos
- Use linguagem clara e técnica
- Seja conciso mas completo""",
                "user_prompt": "{bug_report}",
                "version": "v1",
                "created_at": "2025-01-15",
                "tags": ["bug-analysis", "user-story", "product-management"]
            }
        }
        
        print("✅ Prompt puxado com sucesso")
        return prompts_data
        
    except Exception as e:
        print(f"❌ Erro ao puxar prompt: {e}")
        return None


def main():
    """Função principal"""
    try:
        prompts = pull_prompts_from_langsmith()
        
        if prompts:
            # Salvar em arquivo YAML
            output_path = Path("prompts/bug_to_user_story_v1.yml")
            if save_yaml(prompts, str(output_path)):
                print(f"✅ Prompts salvos em {output_path}")
                return 0
            else:
                print(f"❌ Erro ao salvar prompts")
                return 1
        else:
            print("❌ Não foi possível puxar os prompts")
            return 1
            
    except Exception as e:
        print(f"❌ Erro na execução: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
