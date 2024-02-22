from ctypes import Structure, wintypes, POINTER, windll, pointer, WinError
import time

import tinytuya

import tkinter
from tkinter import messagebox

def batteryCharge():
   """ АККУМУЛЯТОРНАЯ ФУНКЦИЯ """
   class SYSTEM_POWER_STATUS(Structure):
       _fields_ = [
           ("ACLineStatus",       wintypes.BYTE),
           ("BatteryFlag",        wintypes.BYTE),
           ("BatteryLifePercent", wintypes.BYTE),
           ]

   SYSTEM_POWER_STATUS_P = POINTER(SYSTEM_POWER_STATUS)

   GetSystemPowerStatus          = windll.kernel32.GetSystemPowerStatus
   GetSystemPowerStatus.argtypes = [SYSTEM_POWER_STATUS_P]
   GetSystemPowerStatus.restype  = wintypes.BOOL

   status = SYSTEM_POWER_STATUS()
   if not GetSystemPowerStatus(pointer(status)):
      raise WinError()

   charging, charge = status.ACLineStatus, status.BatteryLifePercent
   return (charging, charge)

device = tinytuya.OutletDevice("bf4a73ac7d64bb3cbfh7f5", "Auto", "8*mf8_v{j)Q00~Nj")

def batteryStatus():
   """ СТАТУС ФУНКЦИЯ """
   chargingCharge = batteryCharge()
   charging       = chargingCharge[0]
   charge         = chargingCharge[1]

   if charging == 0:
      if charge <= 40:
         device.turn_on()
   elif charging == 1:
      if charge >= 70:
         device.turn_off()
   else:
      print("\nЭта система работает только на ноутбуках.")


#root = tkinter.Tk()
#messagebox.showinfo("Информация","Полезная информация")

# ФУНКЦИЯ ВЫЗОВА
while True:
  batteryStatus()
  time.sleep(6)