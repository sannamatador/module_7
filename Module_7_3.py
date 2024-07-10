

def custom_write(file_name, strings):
    strings_position = {}
    i = 0
    file = open(file_name, 'w', encoding='utf-8')
    for string in strings:
        i += 1
        key = (i, file.tell())
        value = string
        strings_position[key] = value
        file.write(string)
        file.write('\n')
    file.close()
    return strings_position


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)