#! /usr/bin/python3

import argparse
import json
import os

try:
    VIRTUAL_ENV = os.environ["VIRTUAL_ENV"]
except KeyError:
    raise Exception("You need a virtual environment to run this script")


HOME = os.path.expanduser("~")
DEFAULT_SUBLIME_PROJECT_DIR = f"{HOME}/projects/sublime/"
DEFAULT_PROJECT_DIR = f"{HOME}/projects/highbiza/"

space = argparse.Namespace()
space.PROJECT_NAME = os.path.basename(VIRTUAL_ENV)


def arguments():
    parser = argparse.ArgumentParser(
        description="Create a Sublime text python project file"
    )
    parser.add_argument(
        "-p",
        "--project",
        nargs="?",
        default=f"{DEFAULT_PROJECT_DIR}{space.PROJECT_NAME}",
        help="Directory where the project resides"
    )
    parser.add_argument(
        "-v",
        "--virtual_env",
        nargs="?",
        default=VIRTUAL_ENV,
        help="Virtual environment location"
    )
    parser.add_argument(
        "-d",
        "--destination",
        nargs="?",
        default=DEFAULT_SUBLIME_PROJECT_DIR,
        help="Sublime project file directory"
    )

    return parser.parse_args()


def project_file_exists():
    if os.path.isfile(space.PROJECT_FILE):
        return True
    return False


def create_project_file():
    project = {
        "folders":
        [
            {
                "path": space.args.project
            }
        ],
        "settings":
        {
            "python_interpreter": f"{space.args.virtual_env}/bin/python"
        }
    }

    with open(space.PROJECT_FILE, "w+") as file:
        file.write(json.dumps(project, indent=4))


def print_args():
    print(f"Project: {space.args.project}")
    print(f"Virtual_env: {space.args.virtual_env}")
    print(f"Destination: {space.args.destination}")


if __name__ == "__main__":
    space.args = arguments()
    space.PROJECT_FILE = f"{space.args.destination}{space.PROJECT_NAME}.sublime-project"
    shell_cmd = f"subl --project {space.PROJECT_FILE}"
    if project_file_exists():
        print(f"Opening: {space.PROJECT_FILE}")
        os.system(shell_cmd)
    else:
        print_args()
        user_input = input("Sublime Project does not exist, do you want to create a new one? \n[y/N]: ")
        if user_input.lower().strip() == "y":
            create_project_file()
            print(f"Creating new sublime project file at: {space.PROJECT_FILE}")
            os.system(shell_cmd)
        else:
            print("Cya")
