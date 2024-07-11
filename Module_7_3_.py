import re


class WordsFinder:
    def __init__(self,*files):
        self.file_names = []
        for i in files:
            self.file_names.append(i)

    def get_all_words(self):
        self.all_words = {}
        for x in self.file_names:
            with open(x, encoding='utf-8') as file:
                key = x
                value = file.read()
                value = value.lower()
                value = re.sub(r'[^\w\s]', '', value)
                value = value.split()
            self.all_words[key] = value
        return self.all_words

    
    def find(self, word):
        self.word = word
        self.res = {}
        for name, slovo in self.get_all_words().items():
            for index, w in enumerate(slovo):
                if w == self.word.lower():
                    self.res[name] = index + 1
                    break
        return self.res

    
    def count(self, word):
        self.word = word
        self.res = {}
        for name, slovo in self.get_all_words().items():
            self.res[name] = slovo.count(self.word.lower())
        return self.res
            

finder2 = WordsFinder('test_file.txt')

print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего

