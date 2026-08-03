class Stream:
    def __init__(self, name, flow_rate, purity):
        self.name = name
        self.flow_rate = flow_rate
        self.purity = purity

    def calculate_pure_flow(self):
        return self.flow_rate * (self.purity / 100)

    def display_info(self):
        print(f"Flow name: {self.name}")
        print(f"Flow rate: {self.flow_rate} kg/h")
        print(f"Purity: {self.purity}%")
        print("-" * 30)


s1 = Stream("Feed_A", 120, 95)
s2 = Stream("Feed_B", 80, 88)

s1.display_info()
print(f"Pure flow of {s1.name}: {s1.calculate_pure_flow()} kg/h")

s2.display_info()
print(f"Pure flow of {s2.name}: {s2.calculate_pure_flow()} kg/h")
