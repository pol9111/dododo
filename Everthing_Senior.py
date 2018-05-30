import os


def list_all(path): # Incoming a path
    print(path) # Print a directory
    for f in os.listdir(path): # Traverse this directory
        abs_path = os.path.join(path, f) # Splicing all absolute paths
        if os.path.isdir(abs_path): # If is a folder
            list_all(abs_path) # Do it again
        else:
            print(abs_path) # Print a file


list_all('E:')



