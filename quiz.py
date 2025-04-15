class Student:
    def __init__(self,nome,cognome):
        self._nome =nome
        self._cognome =cognome
        self._score = 0.0
        self._nOfQuiz = 0

    def getName(self):
        return  f"{self._nome} {self._cognome}"
    
    def addQuiz(self,score):
        self._score += score 
        self._nOfQuiz += 1
        
    def getTotalScore(self):
        return self._score
        
    def getAverageScore(self): 
        return self._score / self._nOfQuiz 
    
eleonora = Student("Eleonora", "Moroni")
davide = Student("Davide", "Sambughi")

davide.addQuiz(19)
davide.addQuiz(18)
davide.addQuiz(17)

print(davide.getAverageScore())