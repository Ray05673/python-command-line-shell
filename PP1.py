import os
import shutil

# Keep looping until user types quit
while True:

    # Show current directory name followed by ?>
    current_path = os.getcwd()
    folder_name = os.path.basename(current_path)

    if folder_name == "":
        folder_name = "root"

    command = input(folder_name + "?> ")

    # Split the command into parts
    parts = command.split()

    # If nothing was typed
    if len(parts) == 0:
        continue

    # ---- QUIT ----
    if parts[0] == "quit":
        break

    # ---- PWD ----
    elif parts[0] == "pwd":
        if len(parts) != 1:
            print("Usage: pwd")
        else:
            print(os.getcwd())

    # ---- CD ----
    elif parts[0] == "cd":
        if len(parts) != 2:
            print("Usage: cd /absolute/path/")
        else:
            path = parts[1]

            # Must be absolute path
            if not os.path.isabs(path):
                print("Error: must use absolute path")
            elif not os.path.isdir(path):
                print("Error: directory does not exist")
            else:
                os.chdir(path)

    # ---- LS ----
    elif parts[0] == "ls":
        if len(parts) != 2:
            print("Usage: ls -curr")
        else:
            flag = parts[1]

            if flag == "-curr":
                files = os.listdir(os.getcwd())
                files.sort()
                for file in files:
                    print(file)

            elif flag == "-all":
                print("Note: -all not required for this part.")

            elif flag == "-del":
                print("Note: -del not required for this part.")

            else:
                print("Usage: ls -curr")

    # ---- MKDIR ----
    elif parts[0] == "mkdir":
        if len(parts) != 2:
            print("Usage: mkdir name")
        else:
            name = parts[1]

            if " " in name:
                print("Error: no spaces allowed")
            else:
                try:
                    os.mkdir(name)
                except FileExistsError:
                    print("Error: directory already exists")
                except:
                    print("Error creating directory")

    # ---- DELETE ----
    elif parts[0] == "delete":
        if len(parts) != 2:
            print("Usage: delete name")
        else:
            name = parts[1]

            if " " in name:
                print("Error: no spaces allowed")
            elif not os.path.exists(name):
                print("Error: file/directory not found")
            else:
                try:
                    if os.path.isdir(name):
                        shutil.rmtree(name)
                    else:
                        os.remove(name)
                except:
                    print("Error deleting file")

    # ---- READ ----
    elif parts[0] == "read":
        if len(parts) != 2:
            print("Usage: read filename")
        else:
            filename = parts[1]

            if " " in filename:
                print("Error: no spaces allowed")
            elif not os.path.isfile(filename):
                print("Error: file not found")
            else:
                try:
                    file = open(filename, "r", encoding="utf-8", errors="replace")
                    print(file.read())
                    file.close()
                except:
                    print("Error reading file")

    # ---- UNKNOWN COMMAND ----
    else:
        print("Error: unknown command")
