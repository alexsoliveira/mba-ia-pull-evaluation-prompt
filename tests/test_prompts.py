"""
Testes automatizados para validação de prompts.
"""
import pytest
import yaml
import sys
from pathlib import Path

# Adicionar src ao path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

def load_prompts(file_path: str):
    """Carrega prompts do arquivo YAML."""
    with open(file_path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

class TestPrompts:
    
    @pytest.fixture
    def prompt_data(self):
        """Fixture para carregar os dados do prompt v2."""
        return load_prompts("prompts/bug_to_user_story_v2.yml")
    
    def test_prompt_has_system_prompt(self, prompt_data):
        """Verifica se o campo 'system_prompt' existe e não está vazio."""
        assert "bug_to_user_story_v2" in prompt_data, "Chave 'bug_to_user_story_v2' não encontrada"
        
        prompt_config = prompt_data["bug_to_user_story_v2"]
        assert "system_prompt" in prompt_config, "Campo 'system_prompt' ausente"
        assert prompt_config["system_prompt"], "Campo 'system_prompt' está vazio"
        assert len(prompt_config["system_prompt"]) > 10, "Campo 'system_prompt' muito curto"
    
    def test_prompt_has_role_definition(self, prompt_data):
        """Verifica se o prompt define uma persona (ex: "Você é um especialista")."""
        prompt_config = prompt_data["bug_to_user_story_v2"]
        system_prompt = prompt_config.get("system_prompt", "").lower()
        
        # Verificar se contém definição de papel
        role_keywords = ["você é", "você é um", "especialista", "expert", "transformar"]
        has_role = any(keyword in system_prompt for keyword in role_keywords)
        
        assert has_role, f"Nenhuma definição de papel encontrada no system_prompt. Keywords esperados: {role_keywords}"
    
    def test_prompt_mentions_format(self, prompt_data):
        """Verifica se o prompt exige formato específico (User Story, BDD, etc)."""
        prompt_config = prompt_data["bug_to_user_story_v2"]
        user_prompt = (prompt_config.get("user_prompt", "") + 
                      prompt_config.get("system_prompt", "")).lower()
        
        # Verificar se menciona formatos esperados
        format_keywords = [
            "como um",
            "eu quero",
            "para que",
            "dado que",
            "quando",
            "então",
            "formato",
            "estrutura"
        ]
        
        found_keywords = [kw for kw in format_keywords if kw in user_prompt]
        assert len(found_keywords) >= 3, f"Apenas {len(found_keywords)} keywords de formato encontrados (esperado >= 3). Encontrados: {found_keywords}"
    
    def test_prompt_has_few_shot_examples(self, prompt_data):
        """Verifica se o prompt contém exemplos de entrada/saída (técnica Few-shot)."""
        prompt_config = prompt_data["bug_to_user_story_v2"]
        user_prompt = prompt_config.get("user_prompt", "")
        
        # Verificar se contém exemplos
        has_bug_example = "bug:" in user_prompt.lower()
        has_example_keyword = "exemplo" in user_prompt.lower()
        
        # Contar linhas que parecem ser exemplos
        example_count = user_prompt.count("Exemplo")
        
        assert has_bug_example or example_count >= 1, "Nenhum exemplo encontrado no prompt"
        assert user_prompt.count("Como um") >= 2, "Menos de 2 exemplos de 'Como um' encontrados"
    
    def test_prompt_no_todos(self, prompt_data):
        """Garante que não há TODOs não preenchidos no prompt."""
        prompt_config = prompt_data["bug_to_user_story_v2"]
        
        # Verificar todos os campos de texto
        text_fields = [
            prompt_config.get("system_prompt", ""),
            prompt_config.get("user_prompt", ""),
            prompt_config.get("description", "")
        ]
        
        full_text = "\n".join(text_fields)
        
        assert "[TODO]" not in full_text, "Encontrados TODOs não preenchidos [TODO]"
        assert "[FIXME]" not in full_text, "Encontrados FIXMEs [FIXME]"
        assert "TODO:" not in full_text, "Encontrados TODOs em formato TODO:"
        assert "FIXME:" not in full_text, "Encontrados FIXMEs em formato FIXME:"
    
    def test_minimum_techniques(self, prompt_data):
        """Verifica se pelo menos 2 técnicas foram listadas nos metadados."""
        prompt_config = prompt_data["bug_to_user_story_v2"]
        
        assert "techniques" in prompt_config, "Campo 'techniques' ausente"
        techniques = prompt_config.get("techniques", [])
        
        assert isinstance(techniques, list), "Campo 'techniques' deve ser uma lista"
        assert len(techniques) >= 2, f"Apenas {len(techniques)} técnicas listadas (esperado >= 2). Técnicas: {techniques}"
        
        # Verificar se são técnicas válidas
        valid_techniques = [
            "Few-shot Learning",
            "Chain of Thought",
            "Tree of Thought",
            "Skeleton of Thought",
            "ReAct",
            "Role Prompting",
            "Structured Output Format",
            "BDD",
            "Gherkin"
        ]
        
        found_techniques = [t for t in techniques if t in valid_techniques]
        assert len(found_techniques) >= 2, f"Menos de 2 técnicas válidas encontradas. Encontradas: {found_techniques}"

if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])