import requests
from config import HYPERBOLIC_PROXY, HYPERBOLIC_API_URL, HYPERBOLIC_MODEL

def test_hyperbolic_proxy():
    """Тестирование Hyperbolic API через прокси"""
    print("Тестируем Hyperbolic через прокси...")
    
    # проверка прокси
    try:
        ip_check = requests.get(
            "https://httpbin.org/ip",
            proxies={"http": HYPERBOLIC_PROXY, "https": HYPERBOLIC_PROXY},
            timeout=5
        )
        print(f"IP прокси: {ip_check.json()['origin']}")
    except Exception as e:
        print(f"Ошибка прокси: {e}")
        return

    # прогоняем апи ключ через прокси
    headers = {
        "Authorization": "Bearer ",
        "Content-Type": "application/json"
    }
    
    test_prompt = "Выведи такой текст - HELLO"
    
    try:
        response = requests.post(
            HYPERBOLIC_API_URL,
            headers=headers,
            json={
                "model": HYPERBOLIC_MODEL,
                "messages": [{"role": "user", "content": test_prompt}],
                "temperature": 0.2,
                "max_tokens": 50
            },
            proxies={"http": HYPERBOLIC_PROXY, "https": HYPERBOLIC_PROXY},
            timeout=10
        )
        
        print("Сырой ответ сервера:", response.text)
        
        if response.status_code == 200:
            answer = response.json()["choices"][0]["message"]["content"]
            print(f"Ответ Hyperbolic: {answer}")
        else:
            print(f"Ошибка HTTP {response.status_code}: {response.text}")
            
    except Exception as e:
        print(f"Критическая ошибка: {e}")

if __name__ == "__main__":
    test_hyperbolic_proxy()