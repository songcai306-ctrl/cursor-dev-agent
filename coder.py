class CoderAgent:
    def generate(self, plan: str) -> str:
        # 模拟 Cursor 生成代码
        return """
import requests
from functools import lru_cache

@lru_cache(maxsize=128)
def fetch_json(url: str):
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}
"""
