class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print(f'Ручка {self.title} начинает писать')


class Pencil(Stationery):
    def draw(self):
        print(f'Карандаш {self.title} начинает чертить')


class Handle(Stationery):
    def draw(self):
        print(f'Маркер {self.title} отмечает важное в тексте')


stationery = Stationery('Pilot')
stationery.draw()
print(stationery.title)

pen = Pen('Xerox')
pen.draw()

pen = Pencil('Полиграф')
pen.draw()

handle = Handle('КПК')
print(handle.title)
handle.draw()
