import requests
import time
from typing import Optional
from config import *

def generate_gpt_question() -> Optional[str]:
    """Генерирует вопрос через Open Router"""
    headers = {
        "Authorization": "Bearer ",
        "Content-Type": "application/json"
    }
    
    data = {
        "model": "mistralai/mistral-7b-instruct",
        "messages": [
            {
                "role": "system", 
                "content": (
                    "Ты — генератор уникальных вопросов. Жесткие правила:\n"
                    "1. Только один вопрос на темы: технологии, наука, история\n"
                    "2. Должен заканчиваться на '?'\n"
                    "3. 5-12 слов\n"
                    "4. Без кавычек и лишних символов\n\n"
                    "Примеры:\n"
                    "- Почему ИИ не может понять человеческие эмоции?\n"
                    "- Какие технологии заменят смартфоны через 5 лет?"
                )
            },
            {
                "role": "user", 
                "content": "Сгенерируй новый уникальный вопрос строго по правилам выше."
            }
        ],
        "temperature": 0.7, 
        "max_tokens": 50,
        "stop": ["\n", "Пример:"],
        "frequency_penalty": 1.0
    }

    try:
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers=headers,
            json=data,
            timeout=REQUEST_TIMEOUT
        )
        answer = response.json()["choices"][0]["message"]["content"]
        return answer.strip() if answer.endswith('?') else None
    except Exception as e:
        print(f"Ошибка генерации вопроса: {str(e)}")
        return None

def generate_hyperbolic_answer(prompt: str, proxy: str = HYPERBOLIC_PROXY) -> Optional[str]:
    """Получает ответ от Hyperbolic"""
    headers = {
        "Authorization": "Bearer ",
        "Content-Type": "application/json"
    }
    
    data = {
        "model": HYPERBOLIC_MODEL,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.9,
        "max_tokens": 1000
    }
    
    try:
        response = requests.post(
            HYPERBOLIC_API_URL,
            headers=headers,
            json=data,
            timeout=REQUEST_TIMEOUT,
            proxies={"http": proxy, "https": proxy}
        )
        return response.json()["choices"][0]["message"]["content"]
    except Exception as e:
        print(f"Ошибка Hyperbolic: {str(e)}")
        return None

