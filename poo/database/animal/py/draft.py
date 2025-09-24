class Animal:
    def __init__(self, specie:str, sound:str):
        self.specie: str=specie
        self.sound: str=sound
        self.age: int=0

    def __str__(self) -> str:
        return f"{self.specie}:{self.age}:{self.sound}"
    

def main():
    animal: Animal = Animal("","")
    while True:
        line: str=input()
        print("$"+line)
        args:list[str]=line.split(" ")

        if args[0]=="end":
            break
        elif args[0]=="show":
            print(animal)
       
main()