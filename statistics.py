#statistics file
def calculate_gender_stats(patients):
    male_count = female_count = 0
    male_anemia = female_anemia = 0
    male_diabetes = female_diabetes = 0

    for patient in patients.values():
        sex = patient.characteristics[1]
        if sex == 1:  # Male
            male_count += 1
            male_anemia += patient.test_results.anemia
            male_diabetes += patient.test_results.diabetes
        else:  # Female
            female_count += 1
            female_anemia += patient.test_results.anemia
            female_diabetes += patient.test_results.diabetes

    male_anemia_percentage = (male_anemia / male_count * 100) if male_count else 0
    female_anemia_percentage = (female_anemia / female_count * 100) if female_count else 0
    male_diabetes_percentage = (male_diabetes / male_count * 100) if male_count else 0
    female_diabetes_percentage = (female_diabetes / female_count * 100) if female_count else 0

    print ("Statistics\n")

    return {
            "male_anemia_percentage": male_anemia_percentage,
            "female_anemia_percentage": female_anemia_percentage,
            "male_diabetes_percentage": male_diabetes_percentage,
            "female_diabetes_percentage": female_diabetes_percentage,
        }
