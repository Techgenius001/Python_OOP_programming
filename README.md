# Python OOP and File Handling Projects

This repository contains two Python projects demonstrating core Object-Oriented Programming (OOP) concepts including class design, inheritance, encapsulation, and polymorphism.

---

## Project 1: Smartphone Class Design (`smartphone.py`)

### Overview
This project involves designing a `Smartphone` class to represent a generic smartphone with attributes like brand, model, storage, and power status. It demonstrates:

- Use of constructors (`__init__`) to initialize objects with unique values.
- Encapsulation of data and behavior within the class.
- Methods to turn the phone on/off and display phone details.
- Inheritance by creating a `GamingPhone` subclass that extends `Smartphone` with additional attributes and methods.

### Features
- Ability to create smartphone objects with custom details.
- `turn_on()` and `turn_off()` methods to control the phone's power state.
- Overriding methods to customize subclass behavior.
- An example of activating a cooling system unique to gaming phones.

### How to Run
1. Open `smartphone.py` in your Python environment.
2. Uncomment the example usage at the bottom to test the classes.
3. Run the script to see class functionality in action.

---

## Project 2: Polymorphism Challenge with Vehicles (`vehicles.py`)

### Overview
This project demonstrates polymorphism by creating a base class `Vehicle` with a method `move()`, which is implemented differently in multiple subclasses:

- `Car`: Implements `move()` by printing "Driving".
- `Plane`: Implements `move()` by printing "Flying".
- `Boat`: Implements `move()` by printing "Sailing".

### Features
- Base class enforcing subclass implementation of key behavior.
- Polymorphic behavior where the same method name `move()` results in different outputs depending on the subclass.
- Clean demonstration of code reuse and dynamic method resolution.

### How to Run
1. Open `vehicles.py` in your Python environment.
2. Uncomment the example usage at the bottom.
3. Run the script to see polymorphism in action.

---

## Summary

Both projects showcase fundamental OOP principles in Python, including:

- Class creation and object instantiation
- Constructors and instance attributes
- Inheritance and method overriding
- Polymorphism through method redefinition

These projects provide a solid foundation for understanding how to design flexible and reusable code using Python classes.

---

## Author

Samuel (Sam)

---

## License

This is an educational project. Feel free to use and modify it for learning purposes.
