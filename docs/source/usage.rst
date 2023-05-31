Usage
=====

When running the program for the first time please follow the :ref:`installation <installation>` section first.

To run the Scheduler, execute the main.py file

To run unit tests, 
Ensure you're in the project directory, then enter into terminal 'pytest'

.. _installation:

Installation
------------

1. Make sure you are running python 3.11.3 use the windows x86 executable installer in vs code. 

https://www.python.org/downloads/release/python-3113/

In the bottom corner of vs code it should say the python version of your interpreter. if it's incorrect select a different interpreter using ctrl + shift + p -> select interpreter.

create a venv using ctrl + shift + p then create environment and select the interpreter

2. Run the following commands in the integrated terminal at the bottom of vs code:
* python -m pip install --upgrade pip
* python -m pip install -r requirements.txt

test by running main.py in the terminal.
The program should now be running

.. _units:

Unit testing
------------

Ensure you have pytest installed, follow the instructions above (already included in requirements.txt) or enter into terminal:

pip install -U pytest

To run pytest, ensure you're in the project directory and enter into terminal 'pytest'
