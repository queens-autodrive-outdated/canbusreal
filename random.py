import ics as icsneo

devices = icsneo.FindNeoDevices()
for device in devices:
    print(device.Name, device.SerialNumber)
