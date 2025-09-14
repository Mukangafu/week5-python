# Parent class
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def device_info(self):
        return f"{self.brand} {self.model}"

# Child class: Smartphone inherits from Device
class Smartphone(Device):
    def __init__(self, brand, model, storage, battery):
        super().__init__(brand, model)  # Call parent constructor
        self.storage = storage
        self.battery = battery

    def make_call(self, number):
        return f"Calling {number} from {self.brand} {self.model}..."
    
    def charge_battery(self):
        self.battery = 100
        return f"{self.brand} {self.model} is now fully charged!"

# Create objects
phone1 = Smartphone("Apple", "iPhone 15", "256GB", 85)
phone2 = Smartphone("Samsung", "Galaxy S24", "512GB", 60)

# Test methods
print(phone1.device_info())
print(phone1.make_call("0722-123456"))
print(phone2.charge_battery())
