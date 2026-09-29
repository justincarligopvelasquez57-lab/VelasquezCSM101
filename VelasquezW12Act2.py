

Velasquez_patient = {
    "Tristhan": (200,180,155,140,120,105,90),
    "Daniel": (240,170,160,150,120,105,90),
    "Alice":(250,180,150,120,110,70,60),
}

highest_patient = ""
highest_reading = 0

for patient, readings_summary in Velasquez_patient.items():
        print(f"{patient}")
        print("Blood Sugar Summary-")

        for reading in readings_summary:
            if reading > 120:
                status = "High"
            else:
                status = "Normal"
            print(f"{reading} {status}")

            if reading > highest_reading:
                highest_reading = reading
                highest_patient = patient
        print()

print(f"The Highest Blood Sugar Test Patient is {highest_patient}.")







