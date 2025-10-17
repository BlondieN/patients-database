#Database management file
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

def read_database(file_name):
    with open("patients-database-tab.txt", "r") as file:
        data = file.readlines()
        patients = {}
        for line in data[1:]:
            d = line.strip().split("\t")  #split the line
            patient_id = int(d[0])
            dob = int(d[1])
            sex = int(d[2])
            smoker = int(d[3])
            test_results = Tests (patient_id, int(d[4]), int(d[5]), int(d[6]), int(d[7]), float(d[8]), int(d[9]))
            patients[patient_id] = Patient(patient_id, dob, sex, smoker, test_results)
    return patients

def add_patient(patients, patient):
    patients[patient.patient_id] = patient

    tests = Tests ("anemia", "diabetes", "high_blood_pressure", "platelets", "creatinine", "sodium")

def del_patient(patients, patient_id):
    if patient_id in patients:
        del patients[patient_id]
        print("ID deleted successfully")
    else:
        print ("ID is not found!")

def modify_test_result(patients, patient_id, test_results, new_value):
    patient = patients.get(patient_id)
    if test_results == "anemia":
        patient.test_results.anemia = new_value
    elif test_results == "diabetes":
        patient.test_results.diabetes = new_value
    elif test_results == "high_blood_pressure":
        patient.test_results.high_blood_pressure = new_value
    elif test_results == "platelets":
        patient.test_results.platelets = new_value
    elif test_results == "creatinine":
        patient.test_results.creatinine = new_value
    elif test_results == "sodium":
        patient.test_results.sodium = new_value
    else: print("Test result not found")
    return
    print("Updated Successfully")




