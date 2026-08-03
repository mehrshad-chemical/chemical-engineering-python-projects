class Reactor:
    ABSOLUTE_ZERO = -273.15  

    def __init__(self, name, max_temp, initial_temp=25.0):
        self.name = name
        self._max_temp = max_temp
        self.__temperature = 25.0  
        
        
        self.set_temperature(initial_temp)

    def get_temperature(self):
        
        return self.__temperature

    def set_temperature(self, new_temp):
        
        if new_temp < self.ABSOLUTE_ZERO:
            print("Safety warning: The temperature cannot be lower than absolute zero (-273.15°C)!")
            return False

        if new_temp > self._max_temp:
            print(f"Safety warning: Temperature {new_temp}°C exceeds the permissible limit of {self._max_temp}°C!")
            return False

    
        self.__temperature = new_temp
        print(f"Reactor '{self.name}': successfully set to {self.__temperature:.2f}°C.")
        return True

    def get_status(self):
     
        return (
            f"Reactor: {self.name} | "
            f"Current temperature: {self.__temperature:.2f}°C | "
            f"Maximum allowed temperature: {self._max_temp:.2f}°C"
        )



R1 = Reactor("CSTR-101", max_temp=150.0, initial_temp=25.0)
print(R1.get_status())
print("-" * 50)

R1.set_temperature(85.0)
print(R1.get_status())
print("-" * 50)


R1.set_temperature(200.0)
print(R1.get_status())
