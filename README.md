# ROBOTS VS. DINOSAURS PROJECT FRAMEWORK

Introduction

In previous projects, you became adjusted to the practice of creating the flow of your programs by writing function and calling functions – this is an approach known as the “functional programming” paradigm. Now, with Object Oriented Programming, we are taking a different approach: creating classes to represent the unique data structures in our program, creating instances (objects) from those classes, and having those objects interact with each other in order to create the flow of our program. This creates a “Russian Nesting Doll” effect of all your classes nested inside of larger classes that represent the larger units of functionality for the program.

Be sure to read the User Stories document thoroughly to get a clear idea of what features need to be present for this project, and follow the steps below to get started. Good luck!

💡 MAKE SURE YOU HAVE THE UML FOR THIS PROJECT BEFORE STARTING!

Resources

Lectures

· Classes & Objects

· UML (Unified Modeling Language)

Documents

· UML – Robots vs. Dinosaurs

Relevant Projects

· Classes & Objects Lab

Other Resources

· Code Demo – Building Classes from a UML

Tasks

1. Review all necessary materials for getting started

2. Create your project (including setting up your GitHub repository for source control)

3. Create all of the classes for the project based off of the UML

4. Starting with the smallest class, write the methods for your classes.

5. Work through the user stories as you write methods, testing each method before moving on!

Setup Steps

1. Create a folder for your project, then create a GitHub repository for the project.

2. Clone down the repository to your computer and put the invisible .git folder inside your project folder (as well as the .gitignore and README). Make an initial commit.

3. Create a new file for each class on the UML, as well as a main.py file that will serve as the entry point of your application.

4. Begin working on the user stories by filling in your classes from smallest to large. Begin with the Weapon class, then move on to the Robot class, then the Dinosaur class.

5. Once those classes are tested, move on to the Herd and Fleet classes (these will look very similar once they are done!)

6. Finally, fill out the methods for your battle logic in the Battlefield class. You will only need to import the Fleet and Herd classes into the Battlefield class.

End Result

Please see the Project Walkthrough – Robots vs. Dinosaurs video for an idea of how the final product will look!

# UML

![UML](https://files.cdn.thinkific.com/file_uploads/211484/attachments/73f/b40/1f2/robots_vs_dinosaurs_uml.png)

# ROBOTS VS. DINOSAURS (USER STORY)

Using the concepts of OOP by creating classes and using objects (instances of those classes) to interact with each other, create a console application that will have robots and dinosaurs fight in a battle.

Technologies

Python, OOP, Unified Modeling Language (UML)

USER STORY

- As a developer, I want to make at least 7 commits with good, descriptive messages.

- As a developer, I want to make a class for each of the following: Robot, Dinosaur, Fleet, Herd, Weapon, Battlefield.

- As a developer, I want a Robot to have a name, health, and a Weapon (this needs to be its own class and object) with a name (i.e. sword) and attack power.

- As a developer, I want a Dinosaur to have a name, health, and attack power.

- As a developer, I want to instantiate three Robot objects and three Dinosaur objects and assign the appropriate values to all the objects.

- As a developer, I want the created Robot objects to be stored in a Fleet and the created Dinosaur objects to be stored in a Herd (the Fleet and Herd must use a List to store the objects).

- As a developer, I want a Robot to have the ability to attack a Dinosaur and a Dinosaur to have the ability to attack a Robot on a Battlefield.

- As a developer, I want a Robot/Dinosaur to lose health points (loss based on attack power) when another Robot/Dinosaur successfully attacks it.

- As a developer, I want the battle to conclude once either all the robots in the Fleet have their health points reach zero or all of the dinosaurs in the Herd have their health points reach zero.

Bonus
:

- As a developer, I want a Robot to have the ability to choose from a List of different weapons that will be then assigned as its own weapon.

- As a developer, I want a Dinosaur to have the ability to choose its attack name from a tuple of different attack names before attacking a Robot in battle.

- As a developer, I want a Robot to have a power level and a Dinosaur to have an energy, which will decrease by 10 every time they attack.