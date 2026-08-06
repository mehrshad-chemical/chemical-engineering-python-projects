class ProcessEquipment:
    def __init__(self,equipment_id,operational_status = "Idle" ):
        self.equipment_id = equipment_id
        self.operational_status = operational_status

    def turn_on(self):
        self.operational_status = "Active"
        print(f"operational status:{self.operational_status}")

    def turn_off(self):
        self.operational_status = "Idle"
        print(f"operational status:{self.operational_status}")

    def get_details(self):
        return (f"Equipment ID:{self.equipment_id}\n"
                f"Current situation :{self.operational_status}\n"
                )

class DistillationColumn(ProcessEquipment):
    def __init__(self, equipment_id,number_of_trays, operational_status="Idle"):
        super().__init__(equipment_id, operational_status)
        self.number_of_trays = number_of_trays

    def get_details(self):
        return (f"Equipment ID:{self.equipment_id}\n"
                f"Current situation :{self.operational_status}\n"
                f"Number of tower trays:{self.number_of_trays}\n"
                )

class HeatExchanger(ProcessEquipment):
    def __init__(self, equipment_id,heat_transfer_area, operational_status="Idle"):
        super().__init__(equipment_id, operational_status)
        self.heat_transfer_area = heat_transfer_area 

    def get_details(self):
        return (f"Equipment ID:{self.equipment_id}\n"
                f"Current situation :{self.operational_status}\n"
                f"heat transfer area :{self.heat_transfer_area}\n"
                )



column = DistillationColumn("C-301", 30)
heat_exchanger = HeatExchanger("E-101", 120.5)

column.turn_on()
heat_exchanger.turn_on()

print(column.get_details())
print("_" *40)
print(heat_exchanger.get_details())

