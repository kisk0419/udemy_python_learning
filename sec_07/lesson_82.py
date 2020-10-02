"""
Override and super phrase
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
        self.enable_auto_run = enable_auto_run
    
    def run(self):
        super().run()
        print('too fast')


car = TeslaCar()
car.run()
print(car.model)