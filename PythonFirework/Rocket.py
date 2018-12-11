

class Rocket:

    def __init__(self, location, origin, velocity):
        self.loc = location
        self.origin = origin
        self.velocity = velocity
        self.pbest = list(origin)