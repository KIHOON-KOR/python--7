class Dog:
    def __init__(self,name):
        self.name = name
    
    def sound(self):
        return "멍멍"
    
    def dog_info(self):
        return f'이름 : {self.name} , 소리 : {self.sound()}'