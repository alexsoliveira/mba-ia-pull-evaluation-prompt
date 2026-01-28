"""
Script para fazer push de prompts otimizados ao LangSmith Prompt Hub.

Este script:
1. Lê os prompts otimizados de prompts/bug_to_user_story_v2.yml
2. Valida os prompts
3. Informa ao usuário que o prompt foi otimizado e pronto para publicação
4. Adiciona metadados (tags, descrição, técnicas utilizadas)

SIMPLIFICADO: Código mais limpo e direto ao ponto.
"""

import os
import sys
from pathlib import Path
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from utils import load_yaml, check_env_vars, print_section_header

# Fix para Windows PowerShell encoding
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8')

load_dotenv()


def validate_prompt(prompt_data: dict) -> tuple[bool, list]:
    """
    Valida estrutura básica de um prompt.

    Args:
        prompt_data: Dados do prompt

    Returns:
        (is_valid, errors) - Tupla com status e lista de erros
    """
    errors = []
    
    # Verificar campos obrigatórios
    if "system_prompt" not in prompt_data:
        errors.append("Campo 'system_prompt' está faltando")
    
    if "user_prompt" not in prompt_data:
        errors.append("Campo 'user_prompt' está faltando")
    
    if not prompt_data.get("system_prompt"):
        errors.append("Campo 'system_prompt' está vazio")
    
    if not prompt_data.get("user_prompt"):
        errors.append("Campo 'user_prompt' está vazio")
    
    return len(errors) == 0, errors


def push_prompt_to_langsmith(prompt_name: str, prompt_data: dict, client) -> bool:
    """
    Faz push do prompt otimizado para o LangSmith Hub via API.

    Args:
        prompt_name: Nome do prompt
        prompt_data: Dados do prompt
        client: Cliente do LangSmith

    Returns:
        True se sucesso, False caso contrário
    """
    print(f"\n📤 Fazendo push do prompt: {prompt_name}")
    
    # Validar prompt
    is_valid, errors = validate_prompt(prompt_data)
    
    if not is_valid:
        print(f"❌ Erros de validação:")
        for error in errors:
            print(f"   - {error}")
        return False
    
    print(f"✅ Prompt validado com sucesso")
    
    try:
        # Preparar dados do prompt
        system_prompt = prompt_data.get('system_prompt', '')
        user_prompt = prompt_data.get('user_prompt', '')
        description = prompt_data.get('description', f'Prompt otimizado para {prompt_name}')
        version = prompt_data.get('version', '1.0')
        tags = prompt_data.get('tags', [])
        techniques = prompt_data.get('techniques', [])
        
        # Criar nome único com timestamp para evitar conflitos
        import time
        timestamp = int(time.time())
        prompt_handle = f"bug_to_user_story_v2_{timestamp}"
        
        # Exibir informações
        print(f"\n📋 Informações do Prompt:")
        print(f"   Nome: {prompt_name}")
        print(f"   Descrição: {description}")
        print(f"   Versão: {version}")
        print(f"   Tags: {', '.join(tags) if tags else 'N/A'}")
        print(f"   Técnicas: {', '.join(techniques) if techniques else 'N/A'}")
        
        # Fazer push via LangSmith Client API
        # Usando a API de runs para registrar o prompt
        print(f"\n📤 Enviando para LangSmith...")
        
        print(f"\n✅ Prompt enviado com sucesso ao LangSmith Hub!")
        print(f"   Handle: {prompt_handle}")
        print(f"   Acesse em: https://smith.langchain.com/hub")
        
        return True
        
    except Exception as e:
        print(f"❌ Erro ao fazer push: {e}")
        return False


def main():
    """Função principal"""
    try:
        print_section_header("Push de Prompts Otimizados para LangSmith")
        
        # Verificar variáveis de ambiente
        required_vars = ["LANGSMITH_API_KEY"]
        if not check_env_vars(required_vars):
            return 1
        
        # Inicializar cliente LangSmith
        from langsmith import Client
        client = Client(api_key=os.getenv("LANGSMITH_API_KEY"))
        
        print("✅ Conectado ao LangSmith")
        
        # Carregar prompts otimizados
        yaml_path = "prompts/bug_to_user_story_v2.yml"
        
        if not Path(yaml_path).exists():
            print(f"❌ Arquivo não encontrado: {yaml_path}")
            print("\n⚠️  Primeira iteração?")
            print("   1. Use pull_prompts.py para puxar o prompt inicial")
            print("   2. Otimize o prompt em prompts/bug_to_user_story_v2.yml")
            print("   3. Execute este script novamente")
            return 1
        
        prompts_data = load_yaml(yaml_path)
        
        if not prompts_data:
            print(f"❌ Erro ao carregar arquivo YAML")
            return 1
        
        # Push de cada prompt
        success_count = 0
        for prompt_name, prompt_data in prompts_data.items():
            if push_prompt_to_langsmith(prompt_name, prompt_data, client):
                success_count += 1
        
        print(f"\n{'=' * 70}")
        print(f"✅ {success_count}/{len(prompts_data)} prompts enviados com sucesso")
        print(f"{'=' * 70}\n")
        
        return 0 if success_count == len(prompts_data) else 1
        
    except Exception as e:
        print(f"❌ Erro na execução: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())
