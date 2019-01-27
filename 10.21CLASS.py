class ResonantCircuit:
    def __init__(w, b, k):
        self._w = w
        self._b = b
        self._k = k
        
    def getw():
        return self._w
    
    def setw(w):
        self._w = w
        return self._w
        
    def getb():
        return self._b
    
    def setw(b):
        self._b = b
        return self._b
        
    def getk():
        return self._w
    
    def setk(k):
        self._k = k
        return self._k
        
    def display():
        print()
        
class SeriesResonantCircuit(ResonantCircuit):
    def __init__():
        super()
        
    def Ser_EQN:
        self._R = (1/self._k)
        self._L = (self._R/self._b)
        self._C = (1/((self._w**2)*(self._L)))
        return self._L and self._C
        
    def display():
        print()

class ParallelResonanceCircuit(ResonantCircuit):
    def __init__():
        super()
        
    def Par_EQN:
        self._R = self._k
        self.C = (1/(self._b * self._R))
        #If self._R doesnt work, use self._k
        self._L = (1/((self._w**2)*(self._C)))
        return self._L and self._C
        
        
    def display():
        print()
