class CoderAgent:
    def generate(self, plan):
        # 模拟 Cursor 生成代码
        return """
import requests
from functools import lru_cache

@lru_cache(maxsize=100)
def fetch(url):
    try:
        response = requests.get(url)
        return response.json()
    except Exception as e:
        return {"error": str(e)}
"""
