class Crispy_fuzzy: # class

      def __init__(self,n): # constructor
            
            self.n = n # instance reference variable of class
            self.fuzzy : dict = {} # instance reference variable type is dict init by empty dict.

      def crate_fuzzy_set(self)->None:
            
            for i in range(self.n): # its a for loop help of this loop we can  store elment & membership value.  
                  ele : str = input("Enter the element:")# insert element
                  membership : float = float(input("Enter the membership value:"))  # insert membership

                  if 0<= membership <=1: # here we check the the membership value is between 0 - 1
                        self.fuzzy.update({ele:membership}) # here we use the update method for insert the key and value in the dict
                  else:
                        print("invalid membership!!")   # for in valid entry like more than 1 or -ve vale or special char or alpha

            return self.fuzzy     
                  
            
      def crispy_fuzzy(self)->None:
            
            self.result : dict = {} # here we init a empty dict for store the membership value which more than 0
            for key, value in self.fuzzy.items(): # .items() is method help of this method we can fetch the key and value of the dict via help of for loop
                  
                  if value > 0: # this line or snipet check the membership value is greater then 0 or not if > 0 then we insert it in dict.
                        self.result.update({key:value}) # store the value in the dict using .update() method of dict class.
                  
            
      def display(self):
            print("Fuzzy set:") # fust print the statment inside the " "
            print("{",end="")
            for key, value in self.fuzzy.items(): # help for loop we print the key and value of dict of fuzzy
                  print(f"{key} : {value}".format(key,value),end=",")

            print("}")

            print("Support crispy fuzzy set:")
            print("{")
            for key, value in self.result.items(): # here we print crisply fuzzzy
                  print(f"{key} : {value}".format(key,value),end=",")

            print("}")
      
def main():
      total_ele : int = int(input("Enter the total number of elements")) # insert the number of element taken in the set
      obj : Crispy_fuzzy = Crispy_fuzzy(total_ele) # create the instance init by the constructor that is parameterise and take one int value.
      obj.crate_fuzzy_set() # call the method of crispy_fuzzy class for create a fuzzy set.
      obj.crispy_fuzzy() # call the method of crispy_fuzzy class for create a support crispy fuzzy set.
      obj.display() # # call the method of crispy_fuzzy class for display the sets.



main() # here we call the main function