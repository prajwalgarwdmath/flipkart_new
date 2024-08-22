import sys
from SOP import sop_wrapper
from Utilities.utils import delete_directory

def print_usage():
    """Prints usage instructions for the script."""
    print("Usage: python main.py <ARGUMENT>")
    print("Type `python main.py -h` for help!")

def handle_sop(argument):
    """Executes the specified SOP based on the argument.

    Args:
        argument (str): The SOP argument to handle.
    """
    sop_actions = {
        "SOP1": sop_wrapper.execute_SOP1,
        "SOP2": sop_wrapper.execute_SOP2,
        "SOP3": sop_wrapper.execute_SOP3,
        "SUMMARY": sop_wrapper.execute_summarizer,
        "SS": sop_wrapper.execute_soft_skills
    }

    if argument in sop_actions:
        sop_actions[argument]()
    else:
        print("Invalid Argument! Please provide SOP1, SOP2, SOP3, DELETE, SUMMARY or SS as argument")

def handle_delete():
    """Deletes the temp_outputs and results directories."""
    delete_directory("temp_outputs")
    delete_directory("results")

def print_help():
    """Prints help instructions for the script."""
    print_usage()
    print("SOP: SOP1, SOP2, SOP3\nDELETE: To delete the temp_outputs and results directory")
    print("SUMMARY: To summarize the transcripts\nSS: To execute soft skills tasks")
    print("Example: python main.py SOP1")

def main():
    """Main function to handle script arguments and execute corresponding actions."""
    if len(sys.argv) != 2:
        print_usage()
        return

    argument = sys.argv[1]
    
    if argument == "DELETE":
        handle_delete()
    elif argument == "-h":
        print_help()
    else:
        handle_sop(argument)

if __name__ == "__main__":
    main()

"""
*Modular Functions:

   A. print_usage(): Prints the general usage information.
   B. handle_sop(argument): Executes the SOP-related functions based on the argument.
   C. handle_delete(): Handles deletion of directories.
   D. print_help(): Prints detailed help information.

*Mapping Actions:

    Used a dictionary (sop_actions) to map SOP arguments to their respective functions, which simplifies the conditional checks.

*Main Function:

*    The main() function processes command-line arguments and calls appropriate functions.

*Clean Code Practices:

    Added docstrings to functions for clarity.
    Ensured consistency in printing and handling user inputs.

"""