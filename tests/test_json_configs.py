import json
from pathlib import Path
import pytest

repo_root = Path(__file__).resolve().parent.parent


def test_agents_registry_json():
    """Verify that agents registry files in both .agents and .gemini are valid JSON and well-formed."""
    files = [
        repo_root / ".agents" / "agents" / "agents_registry.json",
        repo_root / ".gemini" / "agents" / "agents_registry.json",
        repo_root / "Docs" / "agents_registry.json",
    ]
    for file_path in files:
        if file_path.exists():
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            assert "agents" in data, f"'agents' key missing in {file_path}"
            assert isinstance(data["agents"], list), f"'agents' must be a list in {file_path}"
            assert len(data["agents"]) >= 5, f"Expected at least 5 agent roles in {file_path}"
            role_names = {agent["name"] for agent in data["agents"]}
            expected_roles = {
                "solution-architect",
                "python-ai-engineer",
                "backend-core-dev",
                "ui-ux-designer",
                "qa-security-auditor"
            }
            assert expected_roles.issubset(role_names), f"Missing expected roles in {file_path}: {expected_roles - role_names}"


def test_mcp_config_json():
    """Verify that mcp_config.json files in both .agents and .gemini are valid JSON."""
    files = [
        repo_root / ".agents" / "mcp_config.json",
        repo_root / ".gemini" / "mcp_config.json",
    ]
    for file_path in files:
        assert file_path.exists(), f"Missing config file: {file_path}"
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        assert "mcpServers" in data, f"'mcpServers' missing in {file_path}"
        assert "github" in data["mcpServers"], f"'github' MCP server definition missing in {file_path}"
