"""
Property
"""

class Car(object):
    def __init__(self, model=None):
        self.model = model

    def run(self):
        print('run')

class ToyotaCar(Car):
    def run(self):
        print('fast')

class TeslaCar(Car):
    def __init__(self, model='class S', enable_auto_run=False):
        super().__init__(model)
        self._enable_auto_run = enable_auto_run
        self.__private_enable_auto_run = enable_auto_run
    
    def run(self):
        super().run()
        print('too fast')

    @property
    def enable_auto_run(self):
        return self._enable_auto_run
    
    @enable_auto_run.setter
    def enable_auto_run(self, is_enable):
        self._enable_auto_run = is_enable

    @property
    def private_enable_auto_run(self):
        return self.__private_enable_auto_run
    
    @private_enable_auto_run.setter
    def private_enable_auto_run(self, is_enable):
        self.__private_enable_auto_run = is_enable


car = TeslaCar()
print(car.enable_auto_run)
car.enable_auto_run = True
print(car.enable_auto_run)

print(car.private_enable_auto_run)
car.private_enable_auto_run = True
print(car.private_enable_auto_run)
