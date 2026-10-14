# python-command-line-shell
A Python command-line program that accepts user commands and performs basic file and directory operations.

## Overview
This project is a simple command-line shell built with Python. It allows users to enter commands to navigate directories and perform basic file management operations.

## Features
- **Quit:** Exit the shell.
- **PWD:** Display the current working directory.
- **CD:** Change the current directory using an absolute path.
- **LS:** List files and folders in the current directory.
- **MKDIR:** Create a new directory.
- **Delete:** Delete a file or directory.
- **Read:** Display the contents of a file.

## Technologies Used
- Python
- `os` module
- `shutil` module

## How to Run
1. Make sure Python is installed on your computer.
2. Clone this repository or download the project files.
3. Open a terminal in the project directory.
4. Run the following command:

```bash
python shell.py
```

Replace `shell.py` with your Python file's name if you used a different one.

## Example Usage

```text
Documents?> pwd
C:\Users\Student\Documents

Documents?> ls -curr
notes.txt
shell.py

Documents?> mkdir homework
```

The output will depend on your current directory and its contents.

## What I Learned
Through this project, I practiced using Python loops, conditional statements, functions, exception handling, and file-system operations. I also learned how to process user input and execute commands based on that input.

## Limitations
- Directory navigation requires absolute paths.
- File and directory names containing spaces are not supported.
- Some commands, such as `ls -all` and `ls -del`, are not implemented.

## Note
This project was created as part of a programming assignment.
