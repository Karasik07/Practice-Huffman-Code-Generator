import json
from haffman import CodeGenerator
from FileOperation import funcReadFile,funcWriteFile
def funcMenu():
     while True:
        print("\nВыбор действия:")
        print("[1] Генерация кода Хаффмана для текстовой информации")
        print("[2] Завершение программы")

        try:
            choice = int(input("\nВыбор:"))
        except ValueError:
            print("Ошбика! Не правильный ввод кода действия."); continue

        if(choice == 1):
            print("\nВыбор действия:")
            print("[1] Ввод текстовой информации с клавиатуры")
            print("[2] Выбр файла с информацией")
            print("[3] Завершение программы")

            try:
                choice = int(input("\nВыбор:"))
            except ValueError:
                print("Ошбика! Не правильный ввод кода действия."); continue

            if(choice == 1):
                exCodeGen = CodeGenerator(input("\nТекстовая информация:"))
                exCodeGen.frequencesGenerator(); print(f"(Частота - Символ) текстовой информации: {exCodeGen.frequences}")
                exCodeGen.treeGenerator(); exCodeGen.walk(exCodeGen.frequences[0][1])
                json_data = json.dumps(exCodeGen.code, indent=4); print(f"\nКод Хаффмана: {json_data}")
                funcWriteFile(json_data)
            elif (choice == 2):
                pathToFile = input("\nПуть к файлу:")
                try:
                    text = funcReadFile(pathToFile)
                except FileNotFoundError:
                    print("Ошибка! Указанный файл не найден."); continue
                print(f"\nТекстовая информация из файла:{text}")

                exCodeGen = CodeGenerator(text)
                exCodeGen.frequencesGenerator(); print(f"(Частота - Символ) текстовой информации: {exCodeGen.frequences}")
                exCodeGen.treeGenerator(); exCodeGen.walk(exCodeGen.frequences[0][1])
                json_data = json.dumps(exCodeGen.code, indent=4); print(f"\nКод Хаффмана: {json_data}")
                funcWriteFile(json_data)
            elif (choice == 3):
                exit()
            else: print("Введённый код действия не существует."); continue
        elif (choice == 2):
            exit()
        else: print("Введённый код действия не существует."); continue

funcMenu()