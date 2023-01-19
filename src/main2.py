import requests
# Перед запуском этой программы запустить main.py!
if __name__ == '__main__':

    HOST = "localhost"
    PORT = 8000
    inp = int(input(
          '0 - Выход\n'
          '1 - create_note\n'
          '2 - get_note\n'
          '3 - up_note\n'
          '4 - get_info\n'
          '5 - delete_note\n'
          '6 - list_note\n'
          '\nВведите номер запроса и параметры: '
    ))
    while(inp!=0):
        if inp == 0:
            print('\nВыход\n')

        elif inp == 1:
            print('\ncreate\n')
            token = input("Введите токен: ")
            response = requests.post(f"http://{HOST}:{PORT}" + "/create", params={"token": token})
            print(f"Status code: {response.status_code}")
            print(f"Response body: {response.text}")

        elif inp == 2:
            print('\nget_note\n')

            token = input("Введите токен: ")
            id = int(input("Введите id заметки: "))
            response = requests.get(f"http://{HOST}:{PORT}" + "/get_note", params={"token": token, "id": id})
            print(f"Status code: {response.status_code}")
            print(f"Response body: {response.text}")

        elif inp == 3:
            print('\nup_note\n')

            token = input("Введите токен: ")
            id = int(input("Введите id заметки: "))
            text = input("Введите текст заметки: ")
            response = requests.patch(f"http://{HOST}:{PORT}" + "/up_note", params={"token": token, "id": id, "text": text})
            print(f"Status code: {response.status_code}")
            print(f"Response body: {response.text}")

        elif inp == 4:
            print('\nget_info\n')

            token = input("Введите токен: ")
            id = int(input("Введите id заметки: "))
            response = requests.get(f"http://{HOST}:{PORT}" + "/get_info", params={"token": token, "id": id})
            print(f"Status code: {response.status_code}")
            print(f"Response body: {response.text}")

        elif inp == 5:
            print('\ndelete_note\n')

            token = input("Введите токен: ")
            id = int(input("Введите id заметки: "))
            response = requests.delete(f"http://{HOST}:{PORT}" + "/delete_note", params={"token": token, "id": id})
            print(f"Status code: {response.status_code}")
            print(f"Response body: {response.text}")

        elif inp == 6:
            print('\nlist_note\n')

            token = input("Введите токен: ")
            response = requests.get(f"http://{HOST}:{PORT}" + "/list_note", params={"token": token})
            print(f"Status code: {response.status_code}")
            print(f"Response body: {response.text}")


        else:

            print('\nВведите корректный номер запроса\n')

        inp=int(input('\nВведите номер запроса и параметры: '))