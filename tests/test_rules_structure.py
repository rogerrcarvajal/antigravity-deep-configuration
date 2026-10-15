from pathlib import Path
import pytest

repo_root = Path(__file__).resolve().parent.parent

EXPECTED_RULES = [
    "00-global-principles.md",
    "10-workspace-architecture.md",
    "20-python-ai-services.md",
    "30-backend-services.md",
    "40-frontend-uiux.md",
    "50-security-and-devops.md",
]


@pytest.mark.parametrize("rule_filename", EXPECTED_RULES)
def test_agents_rules_presence(rule_filename):
    """Ensure all core rule files exist and have substantial content in .agents/rules."""
    rule_path = repo_root / ".agents" / "rules" / rule_filename
    assert rule_path.exists(), f"Rule file missing: {rule_path}"
    content = rule_path.read_text(encoding="utf-8")
    assert len(content.strip()) > 100, f"Rule file {rule_filename} is empty or too short."


@pytest.mark.parametrize("rule_filename", EXPECTED_RULES)
def test_gemini_rules_presence(rule_filename):
    """Ensure all core rule files exist and have substantial content in .gemini/rules."""
    rule_path = repo_root / ".gemini" / "rules" / rule_filename
    assert rule_path.exists(), f"Rule file missing: {rule_path}"
    content = rule_path.read_text(encoding="utf-8")
    assert len(content.strip()) > 100, f"Rule file {rule_filename} is empty or too short."


def test_docs_presence():
    """Ensure key documentation files exist and are populated."""
    docs = [
        repo_root / "README.md",
        repo_root / "Docs" / "PLAN_IMPLEMENTACION_ANTIGRAVITY.md",
        repo_root / "Docs" / "WALKTHROUGH_EJECUCION.md",
        repo_root / "Docs" / "GUIA_HABILIDADES_AGENTICAS.md",
        repo_root / "Docs" / "creador-de-skills-antigravity.md",
    ]
    for doc in docs:
        assert doc.exists(), f"Documentation file missing: {doc}"
        assert len(doc.read_text(encoding="utf-8").strip()) > 200, f"Doc {doc.name} is too short."
