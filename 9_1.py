from itertools import cycle
from time import sleep


class TrafficLight:
    __colors = ["зеленый", "желтый", "красный", "желтый"]

    def __init__(self, timing):

        self.__color = self.__colors[0]

        self.__iter_light = cycle(zip(self.__colors, timing + [timing[1]]))


    def state(self):
        return self.__color

    def running(self, cycles):
        for i in range(cycles):
            self.__color, duration = next(self.__iter_light)
            print(f"Загорелся {self.state()} - Время: {duration}s - ", end = "")
            sleep(duration)
            print(f"Погас {self.state()}")

    def running2(self):
        while True:
            try:
                self.__color, duration = next(self.__iter_light)
                print(f"Загорелся {self.state()} - Время: {duration}s - ", end = "")
                sleep(duration)
                print(f"Погас {self.state()}")
            except KeyboardInterrupt:
                print("\nРабота светофора  прервана")
                exit(0)



s = TrafficLight([0.1,0.1,0.1])
s.running(8)
s.running2()