Velasquez_patient = {
    "Ana": (80, 50, 150, 90, 140),
    "Ben": (130, 140, 135, 90, 140),
    "Carlo": (90, 100, 95, 90, 140),}
for patient, readings in Velasquez_patient.items():
    print(f"Patient: {patient}")

    high_count = 0

    for reading in readings:
        if reading > 120:
            status = "High"
            high_count += 1
        else:
            status = "Normal"
        print(f"{reading} - {status}")

print(f"Number of high Readings: {high_count}")
print()