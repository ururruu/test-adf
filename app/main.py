import os
import subprocess
import csv
import random


def main(filename: str):
    with open(f'files/{filename}', 'r') as file:
        print(file.read())

    # List of sample patient names and test results
    patients = ['John Doe', 'Jane Smith', 'Alice Brown', 'Bob Johnson', 'Emma Davis']
    test_types = ['Blood Test', 'X-Ray', 'MRI', 'CT Scan', 'ECG']
    statuses = ['Normal', 'Critical', 'Elevated', 'Low']

    # Create a CSV file with random patient data
    with open('files/patient_test_data.csv', 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        # Write header
        writer.writerow(['Patient Name', 'Test Type', 'Test Status', 'Result Value'])

        # Generate random data for 10 patients
        for _ in range(10):
            name = random.choice(patients)
            test = random.choice(test_types)
            status = random.choice(statuses)
            result = round(random.uniform(0, 100), 2)  # Generate a random test result value
            # Write a row of patient test data
            writer.writerow([name, test, status, result])


if __name__ == "__main__":
    print('Logging test')
    result = subprocess.run(['find', '.'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    print(result.stdout)
    filename = os.environ['input_file']
    main(filename)
    result = subprocess.run(['find', '.'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
