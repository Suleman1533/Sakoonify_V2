class vehicle:
    def __init__(self, make :str , model : str):
        
        self.make = make
        self.model = model
    
    def start_engine(self) ->str :
        return "the engine is starting"

class car(vehicle):
    
    def __init__(self,make :str , model : str ,doors : int):
        super().__init__(make,model)

        self.doors=doors
    
    def start_engine(self) -> str:
        return (f"{self.make} {self.model} says vroom! (with {self.doors} doors) ")
    
class bike (vehicle):
    
    def __init__(self, make :str, model, has_basket : bool):
        super().__init__(make, model)
        self.has_basket = has_basket
        
    
    def start_engine(self) -> str:
            return (f"{self.make} {self.model} says Ring-ring! (Basket: {self.has_basket})")
    
    
    
if __name__ == "__main__":
    my_car = car("Toyota","Corolla", 4)
    my_bike = bike("Honda", "Civic" , True)
    
    print(my_car.start_engine())
    print(my_bike.start_engine())
        
print("================================================================================")
