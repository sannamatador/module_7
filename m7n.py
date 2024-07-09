from pprint import pprint


class Product:
    def __init__(self, name=str, weight=float, category=str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return str(self.name + ', ' + str(self.weight) + ', ' + self.category)


class Shop:

    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name, 'r')
        return file.read()
        file.close()

    def add(self, *products):
        for i in products:
            y = self.get_products()
            if i.name not in y:
                file = open(self.__file_name, 'a')
                x = str(i)
                file.write('\n')
                file.write(x)
                file.close()
            else:
                print('Продукт {} уже есть в магазине'.format(i.name))


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
