class Clock:
    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute
        self.hour += self.minute // 60
        self.minute %= 60
        self.hour %= 24
   

    def __repr__(self):
        return "Clock({}, {})".format(self.hour, self.minute)

    def __str__(self):
        return "{:0>2}:{:0>2}".format(self.hour, self.minute)

    def __eq__(self, other):
        return other.hour == self.hour and other.minute == self.minute

    def __add__(self, minutes):
        hours = minutes // 60
        self.minute = self.minute + minutes%60
        self.hour = (self.hour + hours)%24
        if self.minute >= 60:
            if self.hour+1 == 24:
                self.hour = 0
            else:
                self.hour += 1
            self.minute -= 60
        return self.__str__()

    def __sub__(self, minutes):
        hours = minutes // 60
        self.minute = self.minute - minutes%60
        self.hour = (self.hour - hours)%24
        if self.minute < 0:
            self.minute += 60
            self.hour = (self.hour - 1)%24
        return self.__str__()
    
c = Clock(0,3) - 4