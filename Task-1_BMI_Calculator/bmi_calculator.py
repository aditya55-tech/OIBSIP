# Oasis Infobyte Internship - Python Programming

def calculate_bmi(weight, height):
    return weight / (height ** 2)

def bmi_category_and_tips(bmi):
    if bmi < 18.5:
        return (
            "Underweight",
            "Health Tips:\n"
            "- Increase calorie intake with nutritious foods\n"
            "- Include protein-rich meals\n"
            "- Do strength training exercises\n"
            "- Consult a healthcare professional if needed"
        )
    elif bmi < 25:
        return (
            "Normal",
            "Health Tips:\n"
            "- Maintain a balanced diet\n"
            "- Stay physically active\n"
            "- Drink plenty of water\n"
            "- Get adequate sleep regularly"
        )
    elif bmi < 30:
        return (
            "Overweight",
            "Health Tips:\n"
            "- Reduce sugary and junk foods\n"
            "- Increase daily physical activity\n"
            "- Practice portion control\n"
            "- Monitor your weight regularly"
        )
    else:
        return (
            "Obese",
            "Health Tips:\n"
            "- Follow a structured diet plan\n"
            "- Engage in regular exercise\n"
            "- Avoid processed foods\n"
            "- Seek guidance from a medical professional"
        )

print("===== BMI Calculator with Health Tips =====")

try:
    weight = float(input("Enter your weight in kg: "))
    height = float(input("Enter your height in meters: "))

    if weight <= 0 or height <= 0:
        print("Error: Weight and height must be positive values.")
    else:
        bmi = calculate_bmi(weight, height)
        category, tips = bmi_category_and_tips(bmi)

        print(f"\nYour BMI is: {bmi:.2f}")
        print(f"Health Category: {category}")
        print("\n" + tips)

except ValueError:
    print("Invalid input! Please enter numeric values only.")
