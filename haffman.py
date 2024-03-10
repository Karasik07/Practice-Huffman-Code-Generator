import json

class Node: #Дерево
    def __init__(self, left, right):
        self.left = left
        self.right = right

class CodeGenerator():
    def __init__(self,text):
        self.text = text
        self.frequences = []
        self.code = ""

    def frequencesGenerator(self):
        letters = set(self.text) #Получение "множества" символов
        self.code = {letter: '' for letter in letters} #Предформирование кода Хафмана
        self.frequences = [] 
        for letter in letters: #Формирование (частота,символ)
            self.frequences.append((self.text.count(letter), letter))
        self.frequences = sorted(self.frequences, key=lambda x: x[0], reverse=True) #Сортировка по убыванию частоты
        print(self.frequences)
    
    def treeGenerator(self):
        while len(self.frequences) > 1: #Проход цикла, пока не останется 1 элемент
            self.frequences = sorted(self.frequences, key=lambda x: x[0], reverse=True) #Сортировка по убыванию частоты
            first = self.frequences.pop() #Получение элемента с наименьшей частотой лево
            second = self.frequences.pop() #Получение элемента с наименьшей частотой право
            freq = first[0]+second[0] #Полученик общей частоты элементов лево + право
            self.frequences.append((freq, Node(first[1], second[1]))) #Формирование дерева
    
    def walk(self,node,path=''): #Проход по веткам сформированного дерева
        if isinstance(node, str): #Сравнение значения с заданным типом (строкой)
            self.code[node] = path
            return
        self.walk(node.left, path + '0')
        self.walk(node.right, path + '1') 

exCodeGen = CodeGenerator("Hello world!")
exCodeGen.frequencesGenerator()
exCodeGen.treeGenerator()
exCodeGen.walk(exCodeGen.frequences[0][1])

print(json.dumps(exCodeGen.code, indent=4))