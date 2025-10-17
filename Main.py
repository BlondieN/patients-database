
from multiprocessing.spawn import set_executable

class Tests:
    def __init__(self, patient_id, anemia, diabetes, high_blood_pressure, platelets, creatinine, sodium):
        self.patient_id = patient_id
        self.anemia = anemia
        self.diabetes = diabetes
        self.high_blood_pressure = high_blood_pressure
        self.platelets = platelets
        self.creatinine = creatinine
        self.sodium = sodium

    def printResults(self):
        print("Test Results for Patient ID:", self.patient_id)
        print("Anemia:", self.anemia)
        print("Diabetes:", self.diabetes)
        print("High Blood Pressure:", self.high_blood_pressure)
        print("Platelets:", self.platelets)
        print("Creatinine:", self.creatinine)
        print("Sodium:", self.sodium)

# Patient information
class Patient:
    def __init__(self, patient_id, dob, sex, smoker, test_results):
        self.patient_id = patient_id
        self.characteristics = (dob, sex, smoker)
        self.test_results = test_results

    def printRecord(self):
        print("Patient ID:", self.patient_id)
        print("Characteristics:", self.characteristics)
        self.test_results.printResults()


# Importing from other modules
from database import read_database, add_patient, del_patient,modify_test_result
from display import print_all_records,print_patient_record, print_spec_test_result
from statistics import calculate_gender_stats

def main():
    patients = read_database("patients-database-tab.txt")

    while True:
        print("Enter 1 to add patient in the database")
        print(" 2 to delete a patient from the database")
        print(" 3 to modify a patient's test result")
        print(" 4 to print all patients' records")
        print(" 5 to print a patient's entire record")
        print(" 6 to print a patient's specific test result")
        print(" 7 to calculate statistics")
        print(" 8 to exit the program")

        choice = input("Enter your choice: ")

        if choice == '1':
            patient_id = int(input("Enter patient ID: "))
            dob = int(input("Enter date of birth (YYYY): "))
            sex = int(input("Enter sex (1 for M, 0 for F): "))
            smoker = int(input("Is the patient a smoker? (1 for yes,0 for no): "))
            print("Enter Test Results")
            anemia = int(input("Anemia (1 for YES, 0 for NO): "))
            diabetes = int(input("Diabetes (1 for Yes, 0 for NO): "))
            high_blood_pressure = int(input("High Blood Pressure(1 for YES, 0 for NO): "))
            platelets = int(input("Platelet level: "))
            creatinine = float(input("Creatinine level: "))
            sodium = int(input("Sodium level: "))

            test_results = Tests(patient_id, anemia, diabetes, high_blood_pressure, platelets, creatinine, sodium)
            new_patient = Patient(patient_id, dob, sex, smoker, test_results)


            patients[patient_id] = new_patient
            print("Patient added successfully.")
            continue

        elif choice == '2':
            patient_id = int(input("Enter the ID of the patient you would like to delete from the Database: "))
            del_patient(patients, patient_id)

        elif choice == '3':
            # Logic to modify patient's test result
            patient_id = int(input("Enter the ID of the patient: "))
            test_results = input("Enter test type to modify (anemia, diabetes, etc.): ")
            new_value = input("Enter the new value: ")
            modify_test_result(patients,patient_id, test_results, new_value)

        elif choice == '4':
            print_all_records(patients)

        elif choice == '5':
            patient_id = int(input("Please enter the id of the patient whose record you would like to see: "))
            print_patient_record(patients,patient_id)

        elif choice == '6':
            patient_id = int(input("Please enter the id of the patient you are treating: "))
            test_results = input("Enter test type to view (anemia, diabetes, high_blood_pressure, platelets, creatinine, sodium): ")
            print_spec_test_result(patients, patient_id, test_results)

        elif choice == '7':
            stats = calculate_gender_stats(patients)
            print(f"The percentage of women who have anemia is {stats['female_anemia_percentage']:.2f}%")
            print(f"The percentage of men who have anemia is {stats['male_anemia_percentage']:.2f}%")
            print(f"The percentage of women who have diabetes is {stats['female_diabetes_percentage']:.2f}%")
            print(f"The percentage of men who have diabetes is {stats['male_diabetes_percentage']:.2f}%")

        elif choice == '8':
            break

if __name__ == "__main__":
    main()



