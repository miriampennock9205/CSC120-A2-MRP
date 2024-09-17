class Computer:

    # What attributes will it need?
    description: str
    processor_type: str
    hard_drive_capacity: int
    memory: int
    operating_system: str
    year_made: int
    price: int
    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, description: str,
                    processor_type: str,
                    hard_drive_capacity: int,
                    memory: int,
                    operating_system: str,
                    year_made: int,
                    price: int):
        self.description = description
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory
        self.operating_system = operating_system
        self.year_made = year_made
        self.price = price    
    # What methods will you need?

    def update_price(self, new_price: int):
        self.price = new_price
        print("Price updated to: ${self.price}")
    
    def update_os(self, new_os:str):
        self.operating_system = new_os
        print("Operating ststem updated to: {self.operating_system}")
    
    def refurbish(self):
        if self.year_made < 2015:
            self.price = 500
        else:
            self.price = 1000
        print("Computer refurbished. New price: ${self.price}")

def main():
    
    # First, let's make a computer
    computer = Computer(
        "Mac Pro (Late 2013)",
        "3.5 GHc 6-Core Intel Xeon E5",
        1024, 64,
        "macOS Big Sur", 2013, 1500
    )

    print(computer.description)

#Only call main() if I am running this program directly
if __name__ == "__main__":
    main()