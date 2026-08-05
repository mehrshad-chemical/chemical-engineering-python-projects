class CentrifugalPump:
    def __init__(self,pump_id,max_flow_rate):
        self.pump_id = pump_id
        self.max_flow_rate = max_flow_rate
        self.__is_running = False
        self.__flow_rate = 0.0

    def start(self):
        self.__is_running = True
        print("PUMP IS TURN ON")
        print("_" * 40)

    def stop(self):
        self.__is_running = False
        self.__flow_rate = 0.0
        print("PUMP IS TURN OFF")
        print("_" * 40)

    def get_flow_rate(self):
        return self.__flow_rate

    def is_running(self):
        return self.__is_running

    def set_flow_rate(self,new_flow):
        if not self.__is_running:
            print("Safety error: Pump is off! Turn on the pump first.")
            return

        if new_flow < 0:
            print("Value error: Flow rate cannot be a negative number.")
            return

        if new_flow > self.max_flow_rate:
            print(f"Safety error: The proposed flow rate ({new_flow} L/min) exceeds the maximum permissible flow rate ({self.max_flow_rate} L/min)!")
            return

        self.__flow_rate = new_flow
        print(f"The flow rate change was successful. Current flow rate: {self.__flow_rate} L/min")

    def get_status(self) :
        if self.__is_running:
            status_str = "ON"
        else:
            status_str = "OFF"

        return (
            f"=== Pump {self.pump_id} Status ===\n"
            f"Operational status: {status_str}\n"
            f"Current flow rate: {self.__flow_rate} L/min\n"
            f"Maximum permissible flow rate: {self.max_flow_rate} L/min\n"
            f"================================="
        )


pump = CentrifugalPump("PUMP-202", max_flow_rate=500.0)
print("--- starting pump safety system test ---")

pump.set_flow_rate(150)
pump.start()
print(pump.get_status())
print("_" * 40)


pump.set_flow_rate(300)
print(pump.get_status())
print("_" * 40)

pump.set_flow_rate(650)
print(pump.get_status())
print("_" * 40)

pump.stop()
print(pump.get_status())
