#importing package
import tinytuya

#setting variable with information about device
d = tinytuya.OutletDevice("your device id here", "device ip adress", "your device localkey here")

#printing info about this device(d)
print(d)

#inserting the value into the "status" variable
print("Write On or Off:")
status = input()

#cheking the "status" variable value and doing function, which depends on its value
if status == "On":
    d.turn_on()
else:
    d.turn_off()
end