# First of all that is the first task in python,
# that we're going to do!

# Global Variables

def menu():
  # variables
  menu_argument = int(
    input(
      "Select on of the options bellow:\n1 - IMC \n2 - Log out \n"
    )
  )

  print("clicked {}".format(menu_argument))

  # functions
  def imc_project():
    # function
    def calc_imc(width, height):
      # rules: (width / height ** 2)
      return round(float(width / height ** 2), 2)
    
    def check_user_imc(imc):
      if imc < 16.00:
        return 1
      elif imc >= 16.00 and imc <= 16.99:
        return 2
      elif imc >= 17.00 and imc <= 18.49:
        return 3
      elif imc >= 18.50 and imc <= 24.99:
        return 4
      elif imc >= 25.00 and imc <= 29.99:
        return 5
      elif imc >= 30.00 and imc <= 34.99:
        return 6
      elif imc >= 35.00 and imc <= 39.99:
        return 7
      elif imc >= 40.00:
        return 8 

    print("\n###### Hey user, you selected IMC project ###### \n")
    
    # variables
    width = float(input("\nFirst of all insert your width:\n"))
    height = float(input("\nNow insert your height:\n"))
    imc_switcher = {
      1: "Grade III low weight",
      2: "Grade II low weight",
      3: "Grade I low weight",
      4: "Ideal Weight",
      5: "Overweight",
      6: "Obesity Grade I",
      7: "Obesity Grade II",
      8: "Obesity Grade III",
    }
    imc_result = calc_imc(width, height)
    
    print("\nYour IMC Definition is: {}".format(imc_switcher.get(check_user_imc(imc_result), "No tracking IMC")))

    print("\n")
    print("###### ------------------------------- ###### \n")
    menu()

  if menu_argument == 2:
    print("\n\nThanks For everything, see you soon!")
    exit()
  else:
    imc_project()

def init():
  print("###### Welcome to Health Track Project ###### \n")
  menu()
  print("###### ------------------------------- ###### \n")

# Project init
init()
