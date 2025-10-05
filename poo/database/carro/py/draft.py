class Car:
    def __init__(self):
        self.gas:int=0
        self.km:int=0
        self.pas:int=0

    def __str__(self)->str:
        return (f"pass: {self.pas}, gas: {self.gas}, km: {self.km}")

    def Enter(self):
        #if self.pas>=2:
            self.pas+=1
            

def main():
    car:Car=Car()
    while True:
        line:str=input()
        print("$"+line)
        args:list[str]=line.split(" ")

        if args[0]=="end":
            break
        if args[0]=="show":
            print(car)
        if args[0]=="enter":

main()  


