from tv import TV

class Control:
    def __init__(self):
        self.tv = TV

    def turnOn(self): 
        self.tv.turnOn
    
    def turnOff(self): 
        self.tv.turnOff
    
    def canalUp(self): 
        self.tv.canalUp

    def canalDown(self): 
        self.tv.canalDown
    
    def volumenUp(self): 
        self.tv.volumenUp
    
    def volumenDown(self): 
        self.tv.voumenDown
    
    def setCanal(self): 
        self.tv.setCanal 
    
    def setVolumen(self): 
        self.tv.setVolumen
    
    def enlazar(self, tv):
        self.tv.setControl(self)
        self.tv = tv 
    
    def setTv(self, tv): 
        self.tv = tv 
    
    def getTv(self): 
        return self.tv
        

