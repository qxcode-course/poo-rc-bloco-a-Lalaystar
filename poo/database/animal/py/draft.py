class Animal:
    def __init__(self, specie:str, sound:str):
        self.specie: str=specie
        self.sound: str=sound
        self.age: int=0

    def __str__(self) -> str:
        return f"{self.specie}:{self.age}:{self.sound}"
    
    def ageBy(self, amount:int)->None:
        self.age+=amount
        if self.age>=4:
            self.age=4


def main():
    animal: Animal = Animal("","")
    while True:
        line: str=input()
        print("$"+line)
        args:list[str]=line.split(" ")

        if args[0]=="end":
            break
        if args[0]=="show":
            print(animal)
        if args[0]=="init":
            specie: str= args[1]
            sound: str=args[2]
            animal=Animal(specie,sound)
       
main()