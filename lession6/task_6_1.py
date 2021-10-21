import time


class TrafficLight:
    __color = ["Red", "Yellow", "Green"]
    time_delay = [7, 2, 5]
    i = 0

    def running(self):
        print(self.__color[self.i])
        time.sleep(self.time_delay[self.i])
        self.i = (0 if self.i == 2 else self.i + 1)


traffic_light = TrafficLight()

while 1:
    traffic_light.running()
