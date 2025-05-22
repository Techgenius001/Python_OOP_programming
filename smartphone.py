# smartphone.py
# This file contains a Smartphone class and a GamingPhone subclass demonstrating inheritance and encapsulation

class Smartphone:
    """
    Represents a general smartphone with basic attributes and methods.
    """
    def __init__(self, brand, model, storage):
        """
        Initializes the Smartphone object with brand, model, and storage capacity.
        Initially, the phone is turned off.
        """
        self.brand = brand               # Store the phone's brand (e.g., Samsung)
        self.model = model               # Store the phone's model (e.g., Galaxy S21)
        self.storage = storage           # Storage capacity in GB
        self.is_on = False              # Power status; phone starts OFF

    def turn_on(self):
        """Turns the smartphone on."""
        if not self.is_on:               # Check if phone is currently off
            self.is_on = True            # Change state to ON
            print(f"{self.brand} {self.model} is now ON.")  # Confirm action to user
        else:
            print(f"{self.brand} {self.model} is already ON.")  # Phone was already on

    def turn_off(self):
        """Turns the smartphone off."""
        if self.is_on:                  # Check if phone is currently on
            self.is_on = False          # Change state to OFF
            print(f"{self.brand} {self.model} is now OFF.")  # Confirm action
        else:
            print(f"{self.brand} {self.model} is already OFF.")  # Phone was already off

    def show_info(self):
        """Displays information about the smartphone."""
        power_status = "ON" if self.is_on else "OFF"  # Set readable power status string
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Storage: {self.storage}GB")
        print(f"Power Status: {power_status}")

class GamingPhone(Smartphone):
    """
    Represents a specialized smartphone designed for gaming.
    Inherits from Smartphone and adds gaming-related features.
    """
    def __init__(self, brand, model, storage, cooling_system):
        """
        Initializes the GamingPhone with all Smartphone attributes plus cooling system.
        """
        super().__init__(brand, model, storage)  # Initialize parent class attributes
        self.cooling_system = cooling_system     # New attribute unique to gaming phones

    def activate_cooling(self):
        """Activates the gaming phone's cooling system."""
        print(f"Activating {self.cooling_system} cooling system on {self.brand} {self.model}.")

    # Overriding show_info to add cooling system details
    def show_info(self):
        """Displays gaming phone information including cooling system."""
        super().show_info()  # Call the parent method to show common info
        print(f"Cooling System: {self.cooling_system}")  # Add gaming phone-specific info

