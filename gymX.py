from dataclasses import dataclass


@dataclass
class UserProfile:
    name: str
    age: int
    nationality: str
    weight: float  # in kg
    height: float  # in cm
    gender: str

    def calculate_bmi(self) -> float:
        """Calculates Body Mass Index (BMI)."""
        height_in_meters = self.height / 100
        return round(self.weight / (height_in_meters**2), 2)

    def display_profile(self) -> None:
        """Prints the formatted user profile."""
        print("\n" + "=" * 30)
        print("        USER PROFILE        ")
        print("=" * 30)
        print(f"Name        : {self.name}")
        print(f"Age         : {self.age} years")
        print(f"Nationality : {self.nationality}")
        print(f"Gender      : {self.gender}")
        print(f"Height      : {self.height} cm")
        print(f"Weight      : {self.weight} kg")
        print(f"BMI         : {self.calculate_bmi()}")
        print("=" * 30)


def get_float_input(prompt: str) -> float:
    """Helper function to enforce positive numerical float inputs."""
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Please enter a positive number greater than 0.")
                continue
            return value
        except ValueError:
            print("Invalid input! Please enter a valid number.")


def get_int_input(prompt: str) -> int:
    """Helper function to enforce positive integer inputs."""
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("Please enter a positive whole number.")
                continue
            return value
        except ValueError:
            print("Invalid input! Please enter a valid whole number.")


def collect_user_data() -> UserProfile:
    """Collects all user information with input validation."""
    print("--- Please Enter Your Details ---")

    name = input("Enter your full name: ").strip().title()
    age = get_int_input("Enter your age: ")
    nationality = input("Enter your nationality: ").strip().title()
    gender = input("Enter your gender (e.g., Male/Female/Other): ").strip().title()
    height = get_float_input("Enter your height (in cm): ")
    weight = get_float_input("Enter your weight (in kg): ")

    return UserProfile(
        name=name,
        age=age,
        nationality=nationality,
        weight=weight,
        height=height,
        gender=gender,
    )


if __name__ == "__main__":
    user = collect_user_data()
    user.display_profile()
    # bmr and maintainance calorie 
    def lbs_to_kg(lbs: float) -> float:
        return lbs * 0.45359237


def inches_to_cm(inches: float) -> float:
    return inches * 2.54


def calculate_bmr(
    weight_kg: float, height_cm: float, age: int, gender: str
) -> float:
    """Calculates Basal Metabolic Rate (BMR) using the Mifflin-St Jeor equation."""
    base_bmr = (10 * weight_kg) + (6.25 * height_cm) - (5 * age)
    if gender in ["male", "m"]:
        return base_bmr + 5
    else:
        return base_bmr - 161


def calculate_maintenance_calories(bmr: float, activity_level: str) -> float:
    """Calculates Total Daily Energy Expenditure (TDEE)."""
    multipliers = {
        "1": 1.2,     # Sedentary
        "2": 1.375,   # Lightly Active
        "3": 1.55,    # Moderately Active
        "4": 1.725,   # Very Active
        "5": 1.9,     # Extra Active
    }
    return bmr * multipliers[activity_level]


def get_float_input(prompt: str) -> float:
    """Helper to ensure valid numeric inputs."""
    while True:
        try:
            val = float(input(prompt))
            if val <= 0:
                print("Please enter a positive number.")
                continue
            return val
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def main():
    print("=========================================")
    print(" BMR & Maintenance Calorie Calculator")
    print("=========================================\n")

    # 1. Choose Unit System
    print("Select Unit System:")
    print("  1. Metric (Kilograms, Centimeters)")
    print("  2. Imperial (Pounds, Feet & Inches)")
    unit_choice = input("Enter choice (1 or 2): ").strip()
    while unit_choice not in ["1", "2"]:
        unit_choice = input("Invalid choice. Enter 1 for Metric or 2 for Imperial: ").strip()

    print("\n--- Personal Information ---")

    # 2. Collect Age & Gender
    while True:
        try:
            age = int(input("Age (years): "))
            if age <= 0:
                print("Please enter a valid age.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a whole number for age.")

    gender = input("Gender (Male/Female): ").strip().lower()
    while gender not in ["male", "m", "female", "f"]:
        gender = input("Invalid input. Enter 'Male' or 'Female': ").strip().lower()

    # 3. Collect Weight and Height based on unit system
    if unit_choice == "1":
        weight_kg = get_float_input("Weight (kg): ")
        height_cm = get_float_input("Height (cm): ")
    else:
        weight_lbs = get_float_input("Weight (lbs): ")
        print("Height:")
        feet = get_float_input("  Feet: ")
        inches = get_float_input("  Inches: ")
        
        # Convert to metric for internal calculations
        total_inches = (feet * 12) + inches
        weight_kg = lbs_to_kg(weight_lbs)
        height_cm = inches_to_cm(total_inches)

    # 4. Activity Level Selection
    print("\nSelect Activity Level:")
    print("  1. Sedentary (Desk job, little/no exercise)")
    print("  2. Lightly Active (Light exercise 1-3 days/week)")
    print("  3. Moderately Active (Moderate exercise 3-5 days/week)")
    print("  4. Very Active (Hard exercise 6-7 days/week)")
    print("  5. Extra Active (Very physical job or training 2x/day)")

    activity_choice = input("Enter choice (1-5): ").strip()
    while activity_choice not in ["1", "2", "3", "4", "5"]:
        activity_choice = input("Invalid choice. Enter a number between 1 and 5: ").strip()

    # 5. Calculations
    bmr = calculate_bmr(weight_kg, height_cm, age, gender)
    tdee = calculate_maintenance_calories(bmr, activity_choice)

    # 6. Display Results
    print("\n=========================================")
    print(" RESULTS")
    print("=========================================")
    print(f" • Basal Metabolic Rate (BMR) : {round(bmr)} kcal/day")
    print(f" • Maintenance Calories (TDEE): {round(tdee)} kcal/day\n")
    print("Calorie Targets for Goals:")
    print(f" • Mild Weight Loss (-0.25 kg / 0.5 lb per wk) : {round(tdee - 250)} kcal/day")
    print(f" • Weight Loss      (-0.50 kg / 1.0 lb per wk) : {round(tdee - 500)} kcal/day")
    print(f" • Mild Weight Gain (+0.25 kg / 0.5 lb per wk) : {round(tdee + 250)} kcal/day")
    print(f" • Weight Gain      (+0.50 kg / 1.0 lb per wk) : {round(tdee + 500)} kcal/day")
    print("=========================================")


if __name__ == "__main__":
    main()
