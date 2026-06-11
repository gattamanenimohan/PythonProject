# Abstraction :
#  it gives access on the functionality but hiding the  implementation

from abc import ABC,abstractmethod
class vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

# concrate class: the class which is implemented abstract class is called concrate class

class car(vehicle):
    def start(self):
        print("car engine is started on the road")

    def stop(self):
        print("car is stopped on the road")

# creating the object
mc=car()   # this is the  object for the above classes
mc.start()
mc.stop()
