from itertools import cycle
from time import sleep


class TrafficLight:
    __color = cycle(['красный', 'желтый', 'зеленый', 'желтый'])

    def running(self):
        times = {
            'красный': 7,
            'желтый': 2,
            'зеленый': 8,
        }
        while True:
            c = next(TrafficLight.__color)
            print(c)
            sleep(times[c])


traffic_light = TrafficLight()
traffic_light.running()
