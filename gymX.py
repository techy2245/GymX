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
    
