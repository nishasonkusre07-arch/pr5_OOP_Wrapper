# 🏢 Python OOP Project: Employee Management System

> 🌟 **Project Documentation**  
> A simple Employee Management System created using **Python Object-Oriented Programming (OOP)** concepts.

---

## 🎯 1. Project Overview

This project is a simple **Employee Management System** developed using Python and OOP concepts.

The system manages information about:

- 👤 Person
- 👨‍💼 Employee
- 👩‍💼 Manager
- 👨‍💻 Developer

The project is designed to understand how different OOP concepts work together in a practical application.

---

## 🎯 2. Project Objective

The main objective of this project is to learn and apply important Python OOP concepts.

### The system allows the user to:

1. 👤 Create a Person
2. 👨‍💼 Create an Employee
3. 👩‍💼 Create a Manager
4. 📋 Show Details
5. 🚪 Exit the system

---

# 🧱 3. Classes Used in the Project

## 👤 Person Class

The **Person** class is used to store basic personal information.

### It contains:

- 📝 Name
- 🎂 Age

The class also has a display operation to show the person's details.

---

## 👨‍💼 Employee Class

The **Employee** class stores employee-related information.

### It contains:

- 🆔 Employee ID
- 📝 Name
- 🎂 Age
- 💰 Salary

Employee ID and salary are kept private to demonstrate **Encapsulation**.

Getter and Setter methods are used to access and update these private values.

---

## 👩‍💼 Manager Class

The **Manager** class is derived from the Employee class.

### It contains:

- 📝 Name
- 🎂 Age
- 🆔 Employee ID
- 💰 Salary
- 🏢 Department

The Manager class demonstrates:

- 🔗 Inheritance
- 🔄 Method Overriding
- ⬆️ Use of `super()`

---

## 👨‍💻 Developer Class

The **Developer** class is also derived from the Employee class.

### It contains:

- 📝 Name
- 🎂 Age
- 🆔 Employee ID
- 💰 Salary
- 💻 Programming Language

It demonstrates inheritance and method overriding.

---

# 🧠 4. OOP Concepts Used

## 🔐 Encapsulation

Encapsulation means keeping data protected inside a class.

In this project:

- 🆔 Employee ID is private.
- 💰 Salary is private.

Getter and Setter methods are used to access and update these values.

---

## 📥 Getter

A **Getter** is used to get or read a private value.

This project uses Getter methods for:

- 🆔 Employee ID
- 💰 Salary

### Simple Meaning:

**Getter = Private data ko read/get karne ke liye.**

---

## 📤 Setter

A **Setter** is used to update or change a private value.

The salary Setter also checks that the salary is greater than zero.

### Simple Meaning:

**Setter = Private data ko update/change karne ke liye.**

---

## 🧬 Inheritance

Inheritance allows one class to use the properties and methods of another class.

In this project:

- 👩‍💼 Manager → inherits from Employee
- 👨‍💻 Developer → inherits from Employee

### Simple Meaning:

**Inheritance = Parent class ki properties aur methods ko child class me use karna.**

---

## 🔄 Method Overriding

Method overriding occurs when a child class provides its own version of a method that already exists in the parent class.

In this project, the display operation is customized for:

- 👨‍💼 Employee
- 👩‍💼 Manager
- 👨‍💻 Developer

Each class displays its own relevant information.

---

## 🏗️ Constructor

A constructor is used to initialize object data when an object is created.

The classes use constructors to initialize their required information.

### Simple Meaning:

**Constructor = Object create hote time data initialize karne ke liye.**

---

## ⬆️ `super()` Concept

The `super()` concept is used in the child classes to call the parent class constructor.

Manager and Developer use it to initialize Employee-related information.

### Simple Meaning:

**`super()` = Parent class ke constructor/method ko use karne ke liye.**

---

## 🔎 `issubclass()`

The project uses `issubclass()` to check whether a class is a child class of another class.

It checks:

- 👩‍💼 Manager → Employee
- 👨‍💻 Developer → Employee

Both are subclasses of Employee.

---

# 🗂️ 5. Dictionary

The project also contains a dictionary for storing references related to:

- 👤 Person
- 👨‍💼 Employee
- 👩‍💼 Manager

This demonstrates how a dictionary can be used to organize related information.

---

# 🔁 6. While Loop

The system uses a **while loop** to keep the menu running.

The menu continues to appear until the user chooses the Exit option.

### Simple Meaning:

**While loop = Program ko baar-baar chalane ke liye jab tak condition true ho.**

---

# 📋 7. Menu-Driven System

The project provides a menu where the user can choose an operation.

### Available Operations:

| 🔢 Option | ⚙️ Operation |
|---|---|
| 1️⃣ | Create a Person |
| 2️⃣ | Create an Employee |
| 3️⃣ | Create a Manager |
| 4️⃣ | Show Details |
| 5️⃣ | Exit |

This makes the program interactive and easy to use.

---

# 📊 8. Show Details

The **Show Details** option allows the user to select which object's information they want to see.

### Details available:

- 👤 Person Details
- 👨‍💼 Employee Details
- 👩‍💼 Manager Details

If an object has not been created, the system displays an appropriate message.

---

# ✅ 9. Basic Validation

The project includes basic validation for salary.

💰 Salary should be greater than zero.

If an invalid salary is provided while updating salary, the system displays an **Invalid Salary** message.

The menu also handles invalid choices.

---

# 🔄 10. Project Flow

The project works in the following sequence:

1. 🚀 Start the Employee Management System.
2. 📋 Display the menu.
3. ⌨️ Ask the user to enter a choice.
4. 🏗️ Create the selected object.
5. 💾 Store the object information.
6. 📋 Show details when requested.
7. 🔁 Display the menu again.
8. 🚪 Exit when the user selects Exit.

---

# 📚 11. Concepts Learned

By completing this project, the following concepts are practiced:

- 🧱 Classes
- 🎯 Objects
- 🏗️ Constructors
- 🪪 `self`
- 🔐 Encapsulation
- 🔒 Private Attributes
- 📥 Getter Methods
- 📤 Setter Methods
- 🧬 Inheritance
- 🔄 Method Overriding
- ⬆️ `super()`
- 🔎 `issubclass()`
- 🗂️ Dictionary
- 🔁 While Loop
- ⌨️ User Input
- 📋 Menu-Driven Program
- ✅ Basic Validation

---

# 🌟 12. Why This Project Is Useful

This project helps understand how OOP concepts can be used in a real-world type of application.

Instead of writing everything separately, information and behavior can be organized into different classes.

This makes the program:

- 📖 Easier to understand
- 🔧 Easier to maintain
- ♻️ Reusable
- 🧩 Well organized
- 🚀 Easy to extend

---

# 🏁 13. Conclusion

The **Employee Management System** is a practical Python OOP project that combines multiple important concepts in one application.

Through this project, we learn how **classes, objects, encapsulation, getters, setters, inheritance, method overriding, constructors, `super()`, and `issubclass()`** can work together.

🌟 This project provides a strong foundation for understanding **Object-Oriented Programming in Python**.

---

 # Explanation video :

 

 # connect me : 

 linkedin : www.linkedin.com/in/nisha-sonkusre-283526415
 Gmail : nishasonkusre07@gmail.com

