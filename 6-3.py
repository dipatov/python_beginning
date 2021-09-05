class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {
            'wage': wage,
            'bonus': bonus,
        }


class Position(Worker):
    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']


teacher = Position('Иван', 'Иванов', 'Учитель', 60000, 10000)
print(teacher.get_full_name())
print(teacher.position)
print(teacher.get_total_income())

developer = Position('Петр', 'Петров', 'Разработчик', 110000, 20000)
print(developer.get_full_name())
print(developer.position)
print(developer.get_total_income())
