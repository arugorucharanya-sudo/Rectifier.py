 calculation_of_rectifier.py

import math

print("RECTIFIER CALCULATOR")
print("--------------------")

Vm = float(input("Enter peak input voltage (V): "))

print("\n1. Half-Wave Rectifier")
print("2. Full-Wave Rectifier")

choice = int(input("Enter your choice: "))

if choice == 1:
    # Half-wave rectifier
    Vdc = Vm / math.pi
    Vrms = Vm / 2
    ripple_factor = 1.21

    print("\nHalf-Wave Rectifier")
    print("DC Output Voltage =", round(Vdc, 2), "V")
    print("RMS Output Voltage =", round(Vrms, 2), "V")
    print("Ripple Factor =", ripple_factor)

elif choice == 2:
    # Full-wave rectifier
    Vdc = (2 * Vm) / math.pi
    Vrms = Vm / math.sqrt(2)
    ripple_factor = 0.482

    print("\nFull-Wave Rectifier")
    print("DC Output Voltage =", round(Vdc, 2), "V")
    print("RMS Output Voltage =", round(Vrms, 2), "V")
    print("Ripple Factor =", ripple_factor)

else:
    print("Invalid choice!")
