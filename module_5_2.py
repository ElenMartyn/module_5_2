class House:
    def __init__(self, name, number_of_floors):
        self.name = name  # атрибут  имени дома
        self.number_of_floors = number_of_floors  # атрибут количества этажей

    def go_to(self, new_floor):
        if self.number_of_floors < new_floor or new_floor < 1:
            print("Такого этажа не существует")
        else:
            for floor in range(1, new_floor + 1):
                print(floor)

    def __len__(self):
        return self.number_of_floors  # количество этажей

    def __str__(self):
        return f"Название: {self.name}, количество этажей: {self.number_of_floors}"  # информация о доме


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)
h3 = House('ЖК Эрендел', 200)

print(h1)
print(h2)
print(h3)

print('количество этажей')
print(len(h1))  # 10
print(len(h2))
print(len(h3)) # 20