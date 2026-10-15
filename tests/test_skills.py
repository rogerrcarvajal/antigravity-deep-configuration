import os
import sys
from pathlib import Path
import pytest

# Add skill-creator scripts to sys.path so we can import quick_validate
repo_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(repo_root / ".agents" / "skills" / "skill-creator"))

from scripts.quick_validate import validate_skill


def get_skill_dirs():
    """Discover all skill directories in .agents/skills and .gemini/skills."""
    roots = [
        repo_root / ".agents" / "skills",
        repo_root / ".gemini" / "skills"
    ]
    skill_dirs = []
    for root in roots:
        if root.exists():
            for item in root.iterdir():
                if item.is_dir() and (item / "SKILL.md").exists():
                    skill_dirs.append(item)
    return skill_dirs


@pytest.mark.parametrize("skill_dir", get_skill_dirs(), ids=lambda p: f"{p.parent.parent.name}/{p.name}")
def test_skill_validation(skill_dir):
    """Test that all agent skills are syntactically and structurally valid."""
    is_valid, message = validate_skill(skill_dir)
    assert is_valid, f"Skill at {skill_dir} failed validation: {message}"
