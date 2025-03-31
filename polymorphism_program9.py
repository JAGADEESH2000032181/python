"""

"""
class Time:
    def __init__(self,hour,minutes):
        self.hour = hour
        self.minutes = minutes
    def __sub__(self,other):
        if isinstance(other,Time):
            return Time(self.hour-other.hour, self.minutes - other.minutes)
        return NotImplemented
    def __str__(self):
        return f"{self.hour} {self.minutes}"
t1 = Time(2,45)
t2 = Time(1,30)
t3 = t1-t2
print(t3)

        
        