# Liabry imports
import os

FOLDER_EXCLUSIONS = ["runs", "archive001", "sample_data", "__pycache__", "COSC428_import", ".ipynb_checkpoints"]      # All folders in cwd that are not imported datasets

def cwd_folders() -> list:
    """ Rerurns a list of all of all folders in the cwd"""
    current_directory = os.getcwd()

    # List all folders in the current directory
    folders = [folder for folder in os.listdir(current_directory) if os.path.isdir(os.path.join(current_directory, folder))]
    return folders


def get_data_set_folders():
    """ Returns a list of all data set folders"""
    folders = cwd_folders()
    dataset_folders = [folder for folder in folders if folder not in FOLDER_EXCLUSIONS]

    return dataset_folders


def print_dataset_folders(dataset_folders):
    """ Prints the dataset folders"""

    print("Dataset folders found")
    for folder in dataset_folders:
        print(f" - {folder}")


def get_user_wd():
    """ """
    dataset_folders = get_data_set_folders()

    print_dataset_folders(dataset_folders)

    while True:
        user_choice = str(input("Please type the folder you would like to use for the training model: "))

        if user_choice not in dataset_folders:
            print("That is not a valid folder\nPlease see above for the options")

        elif user_choice in dataset_folders:
            print(f"\nSelected folder {user_choice}")
            return user_choice
        

        # return f"error"




    
