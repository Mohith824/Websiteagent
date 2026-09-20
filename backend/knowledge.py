"""Knowledge base loader for Srinivas Institute of Technology (SIT) Mangaluru.

This module is responsible for loading the verified facts file (`data/facts.md`).
The content loaded here serves as the single source of truth for our AI agent,
ensuring it never fabricates or hallucinates information.
"""

from pathlib import Path
from typing import Optional

# Resolve the absolute path to the project root directory (d:\WEBSITEAGENT)
# __file__ is d:\WEBSITEAGENT\backend\knowledge.py -> .parent is backend -> .parent.parent is project root
BASE_DIR = Path(__file__).resolve().parent.parent
DEFAULT_FACTS_PATH = BASE_DIR / "data" / "facts.md"

# In-memory cache variable so we only read the file from disk once
_FACTS_CACHE: Optional[str] = None


def load_college_facts(file_path: Optional[Path | str] = None, reload: bool = False) -> str:
    """Load the college facts from the markdown file.

    Args:
        file_path: Optional custom path to the facts file. Defaults to `data/facts.md`.
        reload: If True, bypasses the in-memory cache and re-reads from disk.

    Returns:
        The complete markdown text containing verified college facts.

    Raises:
        FileNotFoundError: If the specified facts file does not exist.
        ValueError: If the facts file is empty or whitespace only.
    """
    global _FACTS_CACHE

    # Return cached content if already loaded and reload wasn't requested
    if _FACTS_CACHE is not None and not reload and file_path is None:
        return _FACTS_CACHE

    target_path = Path(file_path) if file_path else DEFAULT_FACTS_PATH

    if not target_path.exists():
        raise FileNotFoundError(f"Facts file not found at: {target_path}")

    content = target_path.read_text(encoding="utf-8").strip()

    if not content:
        raise ValueError(f"Facts file at {target_path} is empty.")

    # Save to in-memory cache if using the default facts file
    if file_path is None:
        _FACTS_CACHE = content

    return content


def get_facts_summary() -> dict:
    """Return quick diagnostic metadata about the loaded knowledge base."""
    facts = load_college_facts()
    return {
        "character_count": len(facts),
        "has_kcet_code": "E144" in facts,
        "has_comedk_code": "E138" in facts,
        "has_not_available_section": "NOT AVAILABLE" in facts,
    }
