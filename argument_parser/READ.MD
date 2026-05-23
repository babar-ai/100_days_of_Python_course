argparse is a built-in Python library used to create command-line interfaces (CLI).
It allows your Python script to accept parameters from the terminal when you run it.

Instead of editing the code every time, you can pass values directly when executing the script.

What is argparse?

argparse lets a program read arguments provided in the command line.

Example command:

python train_model.py --epochs 50 --batch_size 32

Here:

--epochs

--batch_size

are arguments, and argparse reads them inside Python.

So argparse acts like a bridge between the terminal and your Python code.
------------------------------------------------------------------------------------------

Why We Need argparse?

Without argparse, parameters are usually hardcoded.

Example without argparse:

epochs = 50
batch_size = 32

If you want to change them, you must:

open the code

modify values

run again

This is inefficient.

With argparse, you can run:

python train_model.py --epochs 100

and change parameters without touching the code.