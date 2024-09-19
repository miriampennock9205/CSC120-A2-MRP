from typing import Dict
from computer import Computer

class ResaleShop:
    
    # What attributes will it need?
    # inventory: list
    # How will you set up your constructor?
 # Remember: in python, all constructors have the same name (__init__)
   # def __init__(self):
   #     self.inventory = []
    # goal add c to self.inventory
  #  def add (self, c):
   #     self.inventory.append(c)

    def __init__(self):
        self.inventory: Dict[int, Computer] = {}
        self.next_id: int = 0
    # What methods will you need?

    # Method to buy (add) a computer to the inventory
    def buy(self, computer: Computer):
        self.inventory[self.next_id] = computer
        print(f"Computer with ID {self.next_id} added to inventory.")
        self.next_id += 1

    # Method to sell (remove) a computer from the inventory by ID
    def sell(self, computer_id: int):
        if computer_id in self.inventory:
            removed_computer = self.inventory.pop(computer_id)
            print(f"Computer '{removed_computer.description}' with ID {computer_id} sold.")
        else:
            print(f"Computer with ID {computer_id} not found.")

    # method to print the current inventory
    def print_inventory(self):
        if not self.inventory:
            print("The inventory is empty.")
        else:
            for computer_id, computer in self.inventory.items():
                print(f"ID: {computer_id}, Descriptions: {computer.description}, Year Made: {computer.year_made}, Price: ${computer.price}, OS: {computer.operating_system}")
    
    # Method to refurbish a computer, optionally updating its OS and price
    def refurbish(self, computer_id: int, new_os: str = None):
        if computer_id in self.inventory:
            computer = self.inventory[computer_id]
            if new_os:
                computer.update_os(new_os)
            computer.refurbish()  # Adjust price based on year made
        else:
            print(f"Computer with ID {computer_id} not found.")

def main():
    myShop = ResaleShop()
      # Create a Computer object
    computer = Computer(
        description="Mac Pro (Late 2013)",
        processor_type="3.5 GHz 6-Core Intel Xeon E5",
        hard_drive_capacity=1024,
        memory=64,
        operating_system="macOS Big Sur",
        year_made=2013,
        price=1500
    )

    # Buy the computer and add it to inventory
    myShop.buy(computer)
    print("There are", len(myShop.inventory), "items in stock.")

    # Print the inventory
    myShop.print_inventory()

    # Refurbish the computer with a new OS
    myShop.refurbish(0, new_os="macOS Monterey")
    
    # Print the updated inventory after refurbishing
    myShop.print_inventory()

    # Sell the computer
    myShop.sell(0)
    print("There are", len(myShop.inventory), "items in stock after sale.")
    
    # Print the inventory again after selling
    myShop.print_inventory()
    
if __name__ == "__main__":
    main()