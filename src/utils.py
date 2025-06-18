import json
from typing import List, Dict, Any
from pathlib import Path


def read_json_file(file_path: str) -> List[Dict[str, Any]]:
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data if isinstance(data, list) else []
    except (FileNotFoundError, json.JSONDecodeError):
        return []