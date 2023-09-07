# Создайте класс Архив,
# который хранит пару свойств. Например, число и строку.
# При нового экземпляра класса, старые данные из ранее
# созданных экземпляров сохраняются в пару списков-архивов,
# которые также являются свойствами экземпляра.


class Archive:
    """is archive"""
    instance = None
    def __init__(self, text, number):
        self.text = text
        self.number = number
    def __new__(cls, text, numb):
        if cls.instance:
            cls.instance.arch_txt.append(cls.instance.text)
            cls.instance.arch_numb.append(cls.instance.number)
        else:
            cls.instance = super().__new__(cls)
            cls.instance.arch_txt = []
            cls.instance.arch_numb = []
        return cls.instance
    
    def __str__(self):
        return f"Метод класса: Archive, текущий текст: {self.text}, текущее число {self.number}"

    def __repr__(self):
        return f"Archive{self.text, self.number}"
    

a1 = Archive('qwerty', 32)
print(a1.instance.arch_txt, a1.instance.arch_numb)
a2 = Archive('uiop', 23)
print(a2.instance.arch_txt, a2.instance.arch_numb)
a3 = Archive('u', 2)
print(a3.instance.arch_txt, a3.instance.arch_numb)
a4 =Archive('q', 5)
print(a4.instance.arch_txt, a4.instance.arch_numb)
print(Archive.__doc__)
print(a1, repr(a1), sep='\n')