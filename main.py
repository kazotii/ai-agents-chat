from logic import generate_gpt_question, generate_hyperbolic_answer
import time

def main():
    print("Диалог Open Router и Hyperbolic запущен! Ctrl+C для остановки")
    try:
        while True:
            try:
                question = generate_gpt_question()
                if not question:
                    print("Пропуск из-за ошибки вопроса")
                    time.sleep(2)
                    continue
                print(f"\nВопрос от GPT: {question}")
                
                answer = generate_hyperbolic_answer(question)
                if not answer:
                    print("Пропуск из-за ошибки ответа")
                    time.sleep(2)
                    continue
                
                print(f"Ответ от Hyperbolic: {answer}")
                time.sleep(1)
                
            except KeyboardInterrupt:
                print("\nСкрипт остановлен вручную")
                break
            except Exception as e:
                print(f"Непредвиденная ошибка: {str(e)}")
                time.sleep(5)

    except Exception as global_error:
        print(f"Критическая ошибка: {str(global_error)}")

if __name__ == "__main__":
    main()