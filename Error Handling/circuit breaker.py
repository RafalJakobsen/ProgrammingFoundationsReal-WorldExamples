# Overloading a circuit breaker

class CiircuitBreaker:

    def __init__(self, max_amps):
        self.capacity = max_amps  # max capacity in amps
        self.load = 0  # present load in amps

    def connect(self, amps):
        if self.load + amps > self.capacity:
            raise Exception("Connect will exceed capacity")
        elif self.load + amps < 0:
            raise Exception("Connect will cause negative load")
        else:
            self.load += amps


# create a 20A circut breaker
cb = CiircuitBreaker(20)

print(cb.load)

cb.connect(12)
cb.connect(7)

print(cb.load)
