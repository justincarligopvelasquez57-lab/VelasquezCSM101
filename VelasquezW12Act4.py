Velasquez_patient = {
    "Tristhan": (200, 180, 155, 140, 120, 105, 90),
    "Daniel": (240, 170, 160, 150, 120, 105, 90),
    "Alice": (250, 180, 150, 120, 110, 70, 60),
}

highest_patient = ""
highest_reading = 0

for patient, readings_summary in Velasquez_patient.items():
    print(f"{patient}")
    print("Blood Sugar Summary-")

    # Display individual readings and status
    for reading in readings_summary:
        if reading > 120:
            status = "High"
        else:
            status = "Normal"
        print(f"{reading} {status}")


        if reading > highest_reading:
            highest_reading = reading
            highest_patient = patient


    max_val = max(readings_summary)
    min_val = min(readings_summary)
    avg_val = sum(readings_summary) / len(readings_summary)
    diff_val = max_val - min_val

    
    print(f"Max: {max_val}")
    print(f"Min: {min_val}")
    print(f"Average: {avg_val:.2f}")
    print(f"Diff: {diff_val}")
    print()

print(f"The Highest Blood Sugar Test Patient is {highest_patient}.")