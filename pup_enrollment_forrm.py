# ========== PSEUDO CODE ========
# - Printing the 'PUP ENROLLMENT FORM'
# - Ask user's information
# - Displaying the user's inputted information


# ========== PSEUDO CODE ========
# - Printing the 'PUP ENROLLMENT FORM'
print("PUP ENROLLMENT FORM")

print("\n")

# - Ask user's information
ask_user_name = input("Enter Your Name:")
ask_user_age = int(input("Enter Your Age:"))
ask_user_prev_gwa = int(input("Enter Your Previous GWA:"))
ask_user_membership_in_AWS_DCC = input("Are you a member of AWS Cloud Club?(Yes/No):")

# - Determining the Membership of the User in AWS DCC
def if_member(answer):
    if answer == "Yes":
        return True
    else:
        if answer == "No":
            return False
        else: 
            return "Invalid. Please follow the format in inputting you answer. Thank you."

result = if_member(ask_user_membership_in_AWS_DCC)
print(result)

# - Displaying the user's inputted information
print("\n")
print("Your Enrollment Form:")
print("Name:", ask_user_name)
print("Age:", ask_user_age)
print("Previous GWA:", ask_user_prev_gwa)
print("AWStraunot:", result)




