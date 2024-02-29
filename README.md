# AirBnB Clone - The Console
![65f4a1dd9c51265f49d0](https://github.com/alfredgibeau-ahoussinou/holbertonschool-AirBnB_clone/assets/146840606/e13fb4b1-a83a-4663-8f7e-75029d3e1acc)

[![Project Badge](https://img.shields.io/badge/Project-AirBnB%20Clone-blue)](https://github.com/your-username/your-repo)

Novice | By: Guillaume | Weight: 5

Project to be done in teams of 2 people (your team: Othman and Samy)

Your score will be updated once you launch the project review.

Manual QA review must be done (request it when you are done with the project)

## Concepts

For this project, we expect you to look at these concepts:

- Python packages
- AirBnB clone

## Background Context

Welcome to the AirBnB clone project! Before starting, please read the AirBnB concept page.

## First Step: Write a Command Interpreter

This is the first step towards building your first full web application: the AirBnB clone. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration...

Each task is linked and will help you to:

- Put in place a parent class (called BaseModel) to take care of the initialization, serialization, and deserialization of your future instances
- Create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
- Create all classes used for AirBnB (User, State, City, Place...) that inherit from BaseModel
- Create the first abstracted storage engine of the project: File storage
- Create all unittests to validate all our classes and storage engine

## What's a Command Interpreter?

Do you remember the Shell? It's exactly the same but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:

- Create a new object (e.g., a new User or a new Place)
- Retrieve an object from a file, a database, etc.
- Do operations on objects (count, compute stats, etc.)
- Update attributes of an object
- Destroy an object

## Resources

Read or watch:

- [cmd module](https://docs.python.org/3/library/cmd.html)
- [packages concept page](https://docs.python.org/3/tutorial/modules.html#packages)
- [uuid module](https://docs.python.org/3/library/uuid.html)
- [datetime](https://docs.python.org/3/library/datetime.html)
- [unittest module](https://docs.python.org/3/library/unittest.html)
- [args/kwargs](https://docs.python.org/3/tutorial/controlflow.html#more-on-defining-functions)
- [Python test cheatsheet](https://www.pythonsheets.com/notes/python-tests.html)

## Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

- How to create a Python package
- How to create a command interpreter in Python using the cmd module
- What is Unit testing and how to implement it in a large project
- How to serialize and deserialize a Class
- How to write and read a JSON file
- How to manage datetime
- What is an UUID
- What is *args and how to use it
- What is **kwargs and how to use it
- How to handle named arguments in a function

## Requirements

### Python Scripts

- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle (version 2.7.*)
- All your files must be executable
- The length of your files will be tested using wc
- All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All your classes should have a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
- All your functions (inside and outside a class) should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
- A documentation is not a simple word, it's a real sentence explaining what's the purpose of the module, class, or method (the length of it will be verified)

### Python Unit Tests

- Allowed editors: vi, vim, emacs
- All your files should end with a new line
- All your test files should be inside a folder `tests`
- You have to use the `unittest` module
- All your test files should be python files (extension: `.py`)
- All your test files and folders should start by `test_`
- Your file organization in the `tests` folder should be the same as your project
  - e.g., For `models/base_model.py`, unit tests must be in: `tests/test_models/test_base_model.py`
  - e.g., For `models/user.py`, unit tests must be in: `tests/test_models/test_user.py`
- All your tests should be executed by using this command: `python3 -m unittest discover tests`
- You can also test file by file by using this command: `python3 -m unittest tests/test_models/test_base_model.py`
- All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All your classes should have a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
- All your functions (inside and outside a class) should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
- We strongly encourage you to work together on test cases so that you don't miss any edge case

## Execution

Your shell should work like this in interactive mode:
![image](https://github.com/alfredgibeau-ahoussinou/holbertonschool-AirBnB_clone/assets/146840606/c7e5b60a-deaf-447f-a8ad-24c06904920e)
