


class Rocket:

    def __init__(self, location, origin, velocity, evalFunc):
        self.loc = location
        self.origin = origin
        self.velocity = velocity
        self.pbest = list(origin)
        self.evalFunc = evalFunc

    def launch(self, num_steps):
        best = self.evaluate(evalFunc)


    def evaluate(self, evalFunc):
        if evalFunc == 

