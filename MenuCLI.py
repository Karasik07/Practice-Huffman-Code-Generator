from haffman import CodeGenerator
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
            print("[1] Выбор файла с информацией")
            print("[2] Завершение программы")

            try:
                choice = int(input("\nВыбор:"))
            except ValueError:
                print("Ошбика! Не правильный ввод кода действия."); continue
            
            if (choice == 1):
                pathToFile = input("\nПуть к файлу:")
                try:
                    cgen = CodeGenerator()
                    print(f"\nСгенерированный код Хаффмана для текстовой информации:\n{cgen.gen_code(pathToFile)}")
                except FileNotFoundError:
                    print("Ошибка! Указанный файл не найден."); continue
            elif (choice == 2):
                exit()
            else: print("Введённый код действия не существует."); continue
        elif (choice == 2):
            exit()
        else: print("Введённый код действия не существует."); continue

funcMenu()