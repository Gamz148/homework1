class Worker():
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Person(Worker):
    def get_full_name(self):
        return(f"{self.surname} {self.name}")

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]


p = Person("Иван","Сергеевич"," работник",12,10)
print(p.get_full_name())
print(p.get_total_income())