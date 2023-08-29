class TV: 
    numTV = 0
    def __init__(self,marca,estado):
        self.__marca = marca 
        self.__estado = estado
        self.__canal = 1
        self.__precio = 500
        self.__volumen = 1
        self.__control = None 
        TV.numTV+=1
    
    def setMarca(self, marca): 
        self.__marca = marca
    
    def getMarca(self):
        return self.__marca 
    
    def setCanal(self, canal):
        if self.__estado and 1 <= canal <= 120:     
            self.__canal = canal
    
    def getCanal(self): 
        return self.__canal

    def setPrecio(self, precio):
        self.__precio = precio

    def getPrecio(self):
        return self.__precio

    def setVolumen(self, volumen): 
        if self.__estado and 0 <= volumen <= 7: 
            self.__volumen = volumen

    def getVolumen(self): 
        return self.__volumen

    def setControl(self, control): 
        self.__control =  control
    
    def getControl(self): 
        return self.__control
    
    @classmethod
    def setNumTV(cls, NumTV):
        cls.numTV = NumTV

    def getNumTV(self): 
        return TV.numTV
    
    def turnOn(self):
        self.__estado = True 

    def turnOff(self):
        self.__estado = False

    def getEstado(self): 
        return self.__estado 

    def canalUp(self):
        if self.__estado and 1 <= self.__canal < 120: 
            self.__canal+=1
        
    def canalDown(self): 
        if self.__estado and 1 < self.__canal <= 120: 
            self.__canal-=1
    
    def volumenUp(self): 
        if self.__estado and 0 <= self.__volumen < 7: 
            self.__volumen+=1 

    def volumenDown(self): 
        if self.__estado and 0 < self.__volumen <= 7: 
            self.__volumen-=1
    

