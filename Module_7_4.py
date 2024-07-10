class WordsFinder:
    def __init__(self,*files):
        self.file_names = []
        for i in files:
            self.file_names.append(i)

    def get_all_words(self):
        self.all_words = {}
        for x in self.file_names:
            with open(x, encoding='utf-8') as file:
                for line in file:
                    print(line.lower)



finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())

"""print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего
"""