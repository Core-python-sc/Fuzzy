class Fuzzy:
  def __init__(self,n:int):
     self.no : int = n
     self.fuzzy_set : dict = {}

  def create_fuzzy_set(self)->None:
     
     for i in range(self.no):
        ele : str = input("Enter the element:")
        membership : float = float(input("Enter the membership value:"))

        if 0 <= membership <= 1:
           self.fuzzy_set.update({ele:membership})
        else:
           print("Invalid membership!!")
     

  def scaler_cardinality(self)->None:
     
     self.total : float = 0
     for value in self.fuzzy_set.values():
        self.total += value
    
  
  def relative_cardinality(self)->None:
     
     self.rel : float = self.total/self.no
     
  

  def display_fuzzy_set(self)->None:
     print("The fuzzy set is:")
     print("{",end="")
     for key, value in self.fuzzy_set.items():
        print(f"{key}: {value}",end=",")

     print("}",end="")
        
  
  def display_scaler_relative_cardinality(self)->None:
      
      print(f"\nScaler cardinality:{self.total:.2f}")
      print(f"Scalar relative cardinality:{self.rel:.2f}")
  
def main():
   n : int = int(input("Enter the total number of elements:"))
   
   obj : Fuzzy = Fuzzy(n)
   obj.create_fuzzy_set()
   obj.scaler_cardinality()
   obj.relative_cardinality()
   obj.display_fuzzy_set()
   obj.display_scaler_relative_cardinality()


main()
