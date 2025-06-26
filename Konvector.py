import requests
import json
from datetime import datetime
def get_exchange_rate(api_key, base_currency, target_currency):
    """Получает актуальный курс обмена с API."""
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{base_currency}"
    try:
        response = requests.get(url)
        data = response.json()
        if data["result"] == "success":
            return data["conversion_rates"][target_currency]
        else:
            print("Ошибка при получении курса:", data["error-type"])
            return None
    except Exception as e:
        print("Ошибка подключения к API:", e)
        return None

def convert_currency(amount, exchange_rate):
    """Конвертирует сумму по заданному курсу."""
    return amount * exchange_rate
def main():
    # API-ключ (можно получить бесплатно на https://www.exchangerate-api.com/)
    API_KEY = "05ec2964b99e212a07e0c6a4"  # Замените на свой ключ!
    print("Конвертер валют с актуальным курсом")
    print("Пример ввода: 100 USD RUB")

    while True:
        try:
            user_input = input("\nВведите сумму и валюты (например, '100 USD EUR') или 'exit' для выхода: ").strip()
            if user_input.lower() == "exit":
                break

            parts = user_input.split()
            if len(parts) != 3:
                print("Неправильный формат! Используйте: <сумма> <из_валюты> <в_валюту>")
                continue

            amount = float(parts[0])
            from_currency = parts[1].upper()
            to_currency = parts[2].upper()

            exchange_rate = get_exchange_rate(API_KEY, from_currency, to_currency)
            if exchange_rate is None:
                print("Не удалось получить курс. Попробуйте позже.")
                continue

            converted_amount = convert_currency(amount, exchange_rate)
            print(f"{amount} {from_currency} = {converted_amount:.2f} {to_currency} (курс: 1 {from_currency} = {exchange_rate:.4f} {to_currency})")

        except ValueError:
            print("Ошибка: введите число для суммы.")
        except Exception as e:
            print("Произошла ошибка:", e)

if __name__ == "__main__":
    main()