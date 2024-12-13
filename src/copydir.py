from os import path, listdir, mkdir
from shutil import copy, rmtree

def copy_source_to_dest(source, dest, live_print=False, nested_dest=False):
    # This function should be recursive.
    #
    # The base case will be if the object is a file, in which case it should be copied over.
    #
    # The non-base case will be if the object is a folder, in which case a folder
    # needs to be made in dest, and the source entered recursively.
    #
    # The top-level will have the overall source and dest directories input. Each recursive
    # entering of a folder will replace these source and dest paths with the entered folders.
    #
    # To log the path of each object added to dest, the output of the function should be the
    # paths of the dest of the current object, which should be added to a list.
    # That list can be printed in main.py after the final recursion is done optionally. There
    # should also be a live output option that prints a line to the terminal for each file or
    # folder created.
    
    # Check that the current source and dest folders exist and error otherwise:
    # Source first:
    if not path.exists(source):
        raise Exception(f"Source path \"{source}\" does not exist.")
    # Dest second:
    if not path.exists(dest):
        raise Exception(f"Destination path \"{dest}\" does not exist.")

    # If nested_dest = False, which is the default with no input, then this is treated as
    # the top-level loop of the function and therefore the dest folder contents are deleted,
    # otherwise, do not perform deletion:
    if not nested_dest:
        # Check if the dest folder is already empty:
        dest_contents = listdir(dest)
        if len(dest_contents) > 0:
            # If not empty, delete the current folder and remake it:
            rmtree(dest)
            mkdir(dest)
            # Check that the deletion was successful:
            dest_contents = listdir(dest)
            if len(dest_contents) > 0:
                raise Exception(f"Deletion of contents of destination folder \"{dest}\" unsuccessful.")
    
    # Find all objects in source:
    source_contents = listdir(source)

    # Create a dict to contain paths to objects as keys and objects as values:
    dest_objects = {}

    # For the current source, iterate through each object:
    for object in source_contents:
        # Check the object type (file or dir):
        is_file = path.isfile(path.join(source, object))
        # If that object is a file (base case), copy it:
        if is_file:
            # Copy the file:
            copy(path.join(source, object), dest)
            # Add the object to the dest_objects dictionary:
            dest_objects[path.join(dest, object)] = object
            # Print live info is wanted:
            if live_print:
                print(f"Copied \"{path.join(source, object)}\" to \"{dest}\"")
        # If that object is a folder, create a new folder of the same name in dest and
        # recursively call the function again with this folder as the source and dest:
        else:
            mkdir(path.join(dest, object))
            if live_print:
                print(f"Created dir: \"{path.join(dest, object)}\"")
            # Call the function with the object as the source and dest, and add the
            # returned dest locations to the current list:
            dest_objects[path.join(dest, object)] = copy_source_to_dest(
                path.join(source, object), path.join(dest, object),
                live_print=live_print, nested_dest=True,
                )
    
    # Return the dest objects list:
    return dest_objects
