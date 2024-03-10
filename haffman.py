import json
from FileOperation import funcReadFile,funcWriteFile
class CodeGenerator:
    class Node: #Дерево
        def __init__(self, left, right):
            self.left = left
            self.right = right

    def __init__(self):
        pass

    def walk(self,node,path=''): #Проход по веткам сформированного дерева
        if isinstance(node, str): #Сравнение значения с заданным типом (строкой)
            self.code[node] = path
            return
        self.walk(node.left, path + '0')
        self.walk(node.right, path + '1') 

    def gen_code(self,pathFile):
        text = funcReadFile(pathFile) #Получение текстовой информации из файла
        letters = set(text) #Получение "множества" символов
        self.code = {letter: '' for letter in letters} #Предформирование кода Хафмана
        frequences = [] 
        for letter in letters: #Формирование (частота,символ)
            frequences.append((text.count(letter), letter))
        frequences = sorted(frequences, key=lambda x: x[0], reverse=True) #Сортировка по убыванию частоты

        while len(frequences) > 1: #Проход цикла, пока не останется 1 элемент
            frequences = sorted(frequences, key=lambda x: x[0], reverse=True) #Сортировка по убыванию частоты
            first = frequences.pop() #Получение элемента с наименьшей частотой лево
            second = frequences.pop() #Получение элемента с наименьшей частотой право
            freq = first[0]+second[0] #Полученик общей частоты элементов лево + право
            frequences.append((freq, self.Node(first[1], second[1]))) #Формирование дерева
        self.walk(frequences[0][1])
        funcWriteFile(self.code)    
        return json.dumps(self.code, indent=4)