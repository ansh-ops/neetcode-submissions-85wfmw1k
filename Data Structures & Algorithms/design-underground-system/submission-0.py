class UndergroundSystem:
    def __init__(self):
        self.active = {}
        self.routes = {}
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.active[id] = (stationName, t)
    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start, time = self.active.pop(id)
        key = (start, stationName)
        total, count = self.routes.get(key,(0,0))
        self.routes[key] = (total + t - time, count + 1)
        
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total, count = self.routes[(startStation,endStation)]
        return total/count
        
