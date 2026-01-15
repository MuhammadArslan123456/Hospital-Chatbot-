import re
symptoms_info = {
    "Flu": {
        "symptoms": ["fever", "body pain", "cough", "sore throat"],
        "Recommanded_medicines": ["Paracetamol", "Vitamin C", "Cough Syrup"],
        "Docter_advice": "Drink warm water, rest well, avoid cold drinks and crowded places."
    },
    "Fever": {
        "symptoms": ["high temperature", "weakness", "chills"],
        "Recommanded_medicines": ["Panadol", "Brufan"],
        "Docter_advice": "Drink plenty of water, take rest, and monitor temperature regularly."
    },
    "Cold": {
        "symptoms": ["runny nose", "sneezing", "blocked nose"],
        "Recommanded_medicines": ["Antihistamines", "Nasal Spray"],
        "Docter_advice": "Stay hydrated, keep yourself warm, and take proper rest."
    },
    "Stress": {
        "symptoms": ["anxiety", "headache", "sleep problem", "tension"],
        "Recommanded_medicines": ["Doctor consultation recommended"],
        "Docter_advice": "Exercise daily, practice deep breathing, and maintain good sleep."
    }
}

print("\nWelcome to the Hospital Reception\n")

name = input("Enter patient name: ")
age = input("Enter patient age: ")


while True:
    number = input("Enter your 11-digit contact number: ")
    if number.isdigit() and len(number) == 11:
        break
    else:
        print("Invalid number. Please try again.")


while True:
    email = input("Enter your email address: ")
    if re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email):
        break
    else:
        print("Invalid email. Please try again.")


user_symptoms = input("\nEnter your symptoms : ").lower()
user_symptoms_list = [s.strip() for s in user_symptoms.split(",")]

found = False

for disease, data in symptoms_info.items():
    for symptom in user_symptoms_list:
        if symptom in data["symptoms"]:
            print(f"\n--- Possible Disease: {disease} ---")
            print("Recommended Medicines:", ", ".join(data["Recommanded_medicines"]))
            print("Doctor Advice:", data["Docter_advice"])
            found = True
            break
    if found:
        break

if not found:
    print("\nSorry! No matching disease found.")
    print("Please consult a doctor for proper diagnosis.")
