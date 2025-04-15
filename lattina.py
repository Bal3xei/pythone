import math

class SodaCan :
    def __init__(self,alzezza, raggio):
        self._altezza = alzezza
        self._raggio = raggio

    def getSurfaceArea(self):
        area= (2*math.pi*self._raggio)+(2*math.pi*(self._raggio**2))
        return area
        
    def getVolume (self):
        volume = math.pi*(self._raggio**2)*self._altezza
        return volume

mini_lattina= SodaCan(8,2)
lattina= SodaCan(9.24, 3.37)

print(mini_lattina.getSurfaceArea())
print(mini_lattina.getVolume())
print("")
print(lattina.getSurfaceArea())
print(lattina.getVolume())