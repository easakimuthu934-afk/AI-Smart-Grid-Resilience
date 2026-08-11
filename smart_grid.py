import csv

with open("sample_data.csv", "r") as file:
    data = csv.DictReader(file)

    for row in data:
        voltage = float(row["voltage"])
        current = float(row["current"])
        temperature = float(row["temperature"])

        if voltage < 210 or voltage > 250:
            print("⚠️ Abnormal Voltage Detected")
        elif temperature > 50:
            print("⚠️ High Temperature Detected")
        else:
            print("✅ Grid Condition Normal")
