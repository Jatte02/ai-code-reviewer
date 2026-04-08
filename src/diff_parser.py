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


def parse_files(files:list) -> list[ParsedFile]:
    parsed_files = []
    extensions_ignore = ["md", "txt", "lock", "png", "jpg", "exe"]

    for file in files:
        if not file.patch:
            continue
        parts = file.filename.split('.')
        extension = parts[-1]
        if extension in extensions_ignore:
            continue
        lines = file.patch.split('\n')
        amount_lines = len(lines)
        if amount_lines > 500:
            patch = '\n'.join(lines[:500])
        else:
            patch = file.patch

    return 

            