from web3 import Web3
import csv

# Функция для создания метамасок
def create_metamasks(num_accounts):
    # Подключение к локальной ноде Ethereum (можно изменить URL для подключения к другой ноде)
    web3 = Web3(Web3.HTTPProvider('http://localhost:8545'))

    accounts = []
    for _ in range(num_accounts):
        # Создание нового аккаунта (метамаски)
        account = web3.eth.account.create()
        accounts.append(account)

    print(f"Успешно создано {num_accounts} метамасок")
    return accounts

# Функция для выгрузки приватных ключей в текстовый файл
def export_private_keys(private_keys, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write("Приватные ключи:\n")
        for key in private_keys:
            file.write(key + "\n")
    print(f"Приватные ключи успешно выгружены в файл: {filename}")

# Функция для выгрузки адресов в текстовый файл
def export_addresses(accounts, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write("Адреса:\n")
        for account in accounts:
            file.write(account.address + "\n")
    print(f"Адреса успешно выгружены в файл: {filename}")


def main():
    num_accounts = 474  # Количество метамасок для создания

    # Создание метамасок
    metamask_accounts = create_metamasks(num_accounts)

    # Сбор приватных ключей метамасок
    private_keys = [account._private_key.hex() for account in metamask_accounts]

    # Выгрузка приватных ключей в файл
    export_private_keys(private_keys, 'private_keys.txt')

    # Выгрузка адресов в файл
    export_addresses(metamask_accounts, 'addresses.txt')

if __name__ == "__main__":
    main()
