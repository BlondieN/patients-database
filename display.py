#Display patient database
def print_all_records(patients):
    for patient_id, patient in patients.items():
        patient.printRecord()
    else: print("No patients in database\n")

def print_patient_record(patients, patient_id):
    if patient_id in patients:
        patients[patient_id].printRecord()
    else:
        print("Patient not found.")

def print_spec_test_result (patients, patient_id, test_results):
    if patient_id in patients:
        tests = patients[patient_id].test_results
        result = getattr(tests, test_results, None)
        if result is not None:
            print(f"Patient #{patient_id}'s {test_results} level is {result}")
        else:
            print("Test result not found.")
    else:
        print("Patient not found.")
