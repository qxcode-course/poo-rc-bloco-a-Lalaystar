class Animal:
    def __init__(self, specie:str, sound:str): #aq o construtor bixa
        self.specie: str=specie
        self.sound: str=sound
        self.age: int=0

    def __str__(self) -> str: #aq o toString bixa
        return f"{self.specie}:{self.age}:{self.sound}"
    
    def ageBy(self, increment:int)->None:
        if self.age==4:
            print(f"warning: {self.specie} morreu")
            return 
        self.age+=increment
        if self.age>=4:
            self.age=4
            print(f"warning: {self.specie} morreu")
    
    def makeSound(self)->str: #type:ignore 
        if self.age==0:
            return "---"
        if self.age==1:
            return self.sound
        if self.age==2:
            return self.sound
        if self.age==3:
            return self.sound
        if self.age==4:
            return "RIP"
        
def main(): #aq acontece a interaçao com o código
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
            specie:str=args[1]
            sound:str=args[2]
            animal=Animal(specie,sound)
        if args[0]=="grow":
            increment: int=int(args[1])
            animal.ageBy(increment)
        if args[0]=="noise":
            print(animal.makeSound())
main()