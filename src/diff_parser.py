from dataclasses import dataclass

LANGUAGE_MAP = {
    "py": "python",
    "js": "javascript",
    "ts": "typescript",
    "java": "java",
    "cs": "csharp",
    "go": "go",
    "rb": "ruby",
    "php": "php",
}

@dataclass
class ParsedFile:
    filename: str
    status: str
    language: str
    patch: str
    additions: int
    deletions: int



def detect_language(filename:str) -> str:
    parts = filename.split('.')
    extension = parts[-1]

    if len(parts) == 1:
        return "Unknown"

    if extension in LANGUAGE_MAP:
        return LANGUAGE_MAP[extension]
    else:
        return "Unknown"


