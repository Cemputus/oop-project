class Device:
    def __init__(self, device_name, status, location):
        self.device_name = device_name
        self.status = status
        self.location = location


class SmartHomeController:
    total_devices = 0

    def __init__(self):
        self.devices = []

    def add_device(self, device_name, location):
        device = Device(device_name, "off", location)
        self.devices.append(device)
        SmartHomeController.total_devices += 1
        print(f"Added {device_name} at {location}.")

    def turn_on_device(self, device_name):
        for device in self.devices:
            if device.device_name == device_name:
                device.status = "on"
                print(f"Turned on {device_name}.")
                return
        print(f"Device {device_name} not found.")

    def turn_off_device(self, device_name):
        for device in self.devices:
            if device.device_name == device_name:
                device.status = "off"
                print(f"Turned off {device_name}.")
                return
        print(f"Device {device_name} not found.")

    def display_all_devices(self):
        print("Devices in the system:")
        for device in self.devices:
            print(f"{device.device_name} - Status: {device.status}, Location: {device.location}")


# Demonstration
controller = SmartHomeController()
controller.add_device("Light", "Living Room")
controller.add_device("Fan", "Bedroom")
controller.add_device("TV", "Lounge")

controller.turn_on_device("Light")
controller.turn_off_device("Fan")
controller.display_all_devices()
