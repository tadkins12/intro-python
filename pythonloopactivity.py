passcode = "abc123"  # Replace with your desired passcode
entered_passcode = ""

while entered_passcode != passcode:
    entered_passcode = input("Enter the passcode: ")
    if entered_passcode != passcode:
        print("Incorrect passcode. Please try again.")

print("You have entered the correct passcode. You can now view the website.")
