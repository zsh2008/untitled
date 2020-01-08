from copy import deepcopy


class HuntedBus:
    """ A  Bus model hunted by ghost passengers"""
    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = list(passengers)

    def pick(self, name):
        self.passengers.append(name)
    
    def drop(self, name):
        self.passengers.remove(name)



if __name__ == "__main__":
    bus1 = HuntedBus(('Alice', 'Bill'))
    print("bus1's passengers: -->", bus1.passengers)
    bus1.drop('Alice')
    print("bus1 drop Alice passengers: -->", bus1.passengers)
    bus1.pick("Brown")
    print("bus1 pick Brown passengers: -->", bus1.passengers)

    bus2 = HuntedBus()
    bus2.pick("Brown")
    bus3 = HuntedBus()
    print("Bus2 is: -->" + str(bus2) + "Bus3 is: -->"+ str(bus3))
    print(bus3.passengers)
    
    print(dir(HuntedBus.__init__))
    print(HuntedBus.__init__.__defaults__)
    print(HuntedBus.__init__.__defaults__[0] is bus2.passengers)