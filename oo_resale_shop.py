from typing import List
from computer import Computer

class ResaleShop:
    # Using a list for simplicity
    def __init__(self):
        self.inventory: List[Computer] = []

    # Method to buy (add) a computer to the inventory
    def buy(self, computer: Computer):
        self.inventory.append(computer)
        print(f"Computer added to inventory with ID {len(self.inventory) - 1}.")

    # Method to sell (remove) a computer from the inventory by ID
    def sell(self, computer_id: int):
        if 0 <= computer_id < len(self.inventory):
            removed_computer = self.inventory.pop(computer_id)
            print(f"Computer '{removed_computer.description}' with ID {computer_id} sold.")
        else:
            print(f"Computer with ID {computer_id} not found.")

    # method to print the current inventory
    def print_inventory(self):
        if not self.inventory:
            print("The inventory is empty.")
        else:
            for idx, computer in enumerate(self.inventory):
                print(f"ID: {idx}, Description: {computer.description}, Year Made: {computer.year_made}, Price: ${computer.price}, OS: {computer.operating_system}")
    
    # Method to refurbish a computer, optionally updating its OS and price
    def refurbish(self, computer_id: int, new_os: str = None):
        if 0 <= computer_id < len(self.inventory):
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