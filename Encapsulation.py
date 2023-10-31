class Santosh:
    def __init__(self,name,mobile_number,sport):
        self.name = name
        self.mobile = mobile_number
        self.sport = sport

    def display(self): 
        print(self.name)
     
    def _mobile(self):
        print(self.mobile)

    def __sport(self):
        print(self.sport)
    
    def sports(self):
        self.__sport()

san = Santosh("Santosh Kuamr",999999,"Foot Ball")
san.display()
san._mobile()
san.sports()