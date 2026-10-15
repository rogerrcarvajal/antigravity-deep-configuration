import sys
from pathlib import Path
import pytest

repo_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(repo_root / ".agents" / "skills" / "skill-creator"))

from scripts.utils import parse_skill_md
from scripts.quick_validate import validate_skill


def test_parse_skill_md(tmp_path):
    """Test parsing a valid SKILL.md file."""
    skill_file = tmp_path / "SKILL.md"
    skill_file.write_text("""---
name: test-skill
description: A test skill description for testing parser.
---

# Test Skill Content
""", encoding="utf-8")

    name, desc, full = parse_skill_md(tmp_path)
    assert name == "test-skill"
    assert desc == "A test skill description for testing parser."
    assert "# Test Skill Content" in full


def test_validate_skill_valid(tmp_path):
    """Test that a compliant skill folder passes validation."""
    skill_file = tmp_path / "SKILL.md"
    skill_file.write_text("""---
name: valid-skill
description: Valid skill description without special symbols.
---

# Instructions
""", encoding="utf-8")

    valid, message = validate_skill(tmp_path)
    assert valid is True
    assert message == "Skill is valid!"


def test_validate_skill_invalid_name(tmp_path):
    """Test that non-kebab-case names are rejected."""
    skill_file = tmp_path / "SKILL.md"
    skill_file.write_text("""---
name: Invalid_Name_Skill
description: Valid skill description.
---
""", encoding="utf-8")

    valid, message = validate_skill(tmp_path)
    assert valid is False
    assert "kebab-case" in message
