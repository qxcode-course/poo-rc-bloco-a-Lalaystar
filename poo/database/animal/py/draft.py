class animal:
    def __init__(self, specie:str, age:int, sound:str):
        self.specie: str=specie
        self.age:int=0
        self.sound: str=sound
    
    def __str__(self) -> str:
        return f"{self.specie}:{self.age}:{self.sound}"
def main():
    animal: Animal = Animal("",0,"")
    while True:
        line: str=input()
        print("$"+line)
    
main()