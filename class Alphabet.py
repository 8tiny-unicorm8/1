import string
class Alphabet:     #создание класса
    def __init__(self, lang, letters):   #создание метода с двумя динамическими свойствами. Если бы свойства были статичными, то их знаение было бы указано сразу
        self.lang = lang
        self.letters = list(letters)

    def print(self):      #метод, который выведет в консоль буквы алфавита
        print(letters)

    def letters_num(self):     #метод, который вернет количество букв алфавита
        len(self.letters)

class EngAlphabet(Alphabet):   #создание класса-наследника
    def __init__(self):      #создание инит, который унаследовал св-ва родительского инита
        super().__init__('En', string.ascii_uppercase)

        __letters_num = 26  #приватное статическое св-во, которое хранит количество букв алфавита

    def is_en_letter(self, letter):
        if letter in self.letters:  #метод, который принимает букву в качестве параметра и определяет, относится ли она к английскому алфавиту
            return True
        else:
            return False

    def letters_num(self):    #переопределение метода letters_num. Теперь он возвращает значение свойства __letters_num
        return EngAlphabet.__letters_num


    @staticmethod
    def example():  #метод, который показывает пример текста на англ.языке
        print('''The example of the text: "I’m not a smombie, I just wanted to swim."''')


eng_alphabet = EngAlphabet()
eng_alphabet.print()
print(eng_alphabet.letters_num())
print(eng_alphabet.is_en_letter('F'))
print(eng_alphabet.is_en_letter('Щ'))
EngAlphabet.example()

