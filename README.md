# Automation with Python

Welcome to the course on Automation with Python! In this course, you will learn how to use Python to automate tasks in your daily life. You will learn how to automate processes and create powerful scripts that can save you time and effort.

Before you start, you must know the absolute basics of Python.

## Read File (notes)

We're going to learn about files with Python.

Python can read a variety of file types, including text files (.txt), comma-separated values (.csv), web pages (.html/.htm), JavaScript Object Notation (.json), Extensible Markup Language (.xml). It can also read data from databases such as SQLite, MySQL, and Oracle. Python can also work with image and audio files, but those are not text-based so we'll not cover those in this video.

### Read File

We'll take a look at reading text files with Python now.

Reading files is a very common task in Python. In order to read a file, we first need to open it. We do this with the `open()` function.

`open()` takes two arguments: the path to the file, and the mode. Mode is optional, but it specifies how the file should be opened. The most common mode is 'r', which stands for read.

```python
f = open("example.txt", "r")
