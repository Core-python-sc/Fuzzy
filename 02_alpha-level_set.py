class Alpha_cut:

  def __init__(self, n):
    # Constructor to initialize the object with number of elements in the fuzzy set
    self.no: int = n  # Number of elements in the fuzzy set
    self.fuzzy: dict = {}  # Dictionary to store the fuzzy set in the form {element: membership}

  def create_fuzzy(self):
    # Method to create the fuzzy set by taking input from the user
    for i in range(self.no):
      ele: str = input("Enter the element: ")  # Input for element name
      membership: float = float(input("Enter the membership value: "))  # Input for membership value as float

      try:
        if 0 <= membership <= 1:  # Validate that membership value is between 0 and 1
          self.fuzzy[ele] = membership  # Add the element and membership value to the fuzzy set
        else:
          raise ValueError("membership value must be in between 0-1")  # Raise error if membership value is out of range
      except ValueError as e:
        print(e)  # Print the error message if the value is invalid

  def create_alpha_cut(self):
    # Method to create the alpha-cut of the fuzzy set
    self.alpha_cut: dict = {}  # Initialize dictionary for alpha-cut fuzzy set
    self.alpha_value: float = float(input("Enter the alpha value:"))  # Input for the alpha threshold value

    for key, value in self.fuzzy.items():
      # Iterate through the fuzzy set
      if value >= self.alpha_value:
        # If membership value is greater than or equal to alpha, include it in alpha-cut
        self.alpha_cut.update({key: value})

  def display_fuzzy(self):
    # Method to display the fuzzy set

    if not self.fuzzy:
      # If fuzzy set is empty, print a 'No data' message
      print("fuzzy set:")
      print("No data!!")
      return

    print("fuzzy set:")
    print("{", end=" ")
    for key, value in self.fuzzy.items():
      # Iterate through fuzzy set and print its elements and their membership values
      print(f"{key}:{value}".format(key, value), end=" ")
    print("}", end=" ")

  def dispaly_alpha_cut(self):
    # Method to display the alpha-cut fuzzy set
    if not self.alpha_cut:
      # If alpha-cut set is empty, print a 'No data' message
      print("Alpha-cut fuzzy set:")
      print("No data!!")
      return
    print("\nAlpha-cut fuzzy set:")
    print("{", end="")
    for key, value in self.alpha_cut.items():
      # Iterate and print alpha-cut set elements and their membership values
      print(f"{key}:{value},".format(key, value), end=" ")
    print("}", end="")

def main():
  # Main function to execute the code flow

  n: int = int(input("Enter the total number od elements in fuzzy set:"))  # Input for number of elements in fuzzy set
  obj: Alpha_cut = Alpha_cut(n)  # Create an instance of Alpha_cut class with specified number of elements
  obj.create_fuzzy()  # Call method to input and create the fuzzy set
  obj.create_alpha_cut()  # Call method to input alpha and create the alpha cut
  obj.display_fuzzy()  # Display the fuzzy set
  obj.dispaly_alpha_cut()  # Display the alpha cut set

main()  # Call the main function to start the execution