print("🔒 Password Strength Checker")

password = input("Enter your password: ")

# Initial flags
has_digit = False
has_upper = False
has_lower = False
has_special = False

special_chars = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/"

# Rule 1: Length
if len(password) < 8:
    print("❌ Weak: Password must be at least 8 characters long.")
else:
    # Scan characters
    for char in password:
        if char.isdigit():
            has_digit = True
        elif char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char in special_chars:
            has_special = True

    # Strength Check
    if has_digit and has_upper and has_lower and has_special:
        print("✅ Strong Password")
    elif (has_digit and has_upper) or (has_lower and has_special):
        print("⚠️ Medium Password: Add more variety for strength.")
    else:
        print("❌ Weak Password: Missing important character types.")
