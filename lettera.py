class Letter:
    def __init__ (self, letterFrom , letterTo):
        self._letterFrom = letterFrom
        self._letterTo = letterTo
    
    def addLine(self,line):
        self._line = line

    
    def getText(self):

        return(f"Dear {self._letterTo} :, f"{self._line}", "Sincerely, , f"{self._letterFrom}")


john = Letter("Mary","John")
john.addLine("I am sorry we must part.")
john.addLine("I wish you all the best.")

print(john.getText())
