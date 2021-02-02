#! /usr/bin/python3

import argparse
import json
import os

HOME = os.path.expanduser("~")
DEFAULT_SUBLIME_PROJECT_DIR = f"{HOME}/devel/projects/sublime/"
DEFAULT_PROJECT_DIR = f"{HOME}/devel/projects/highbiza/"

try:
    VIRTUAL_ENV = os.environ["VIRTUAL_ENV"]
except KeyError:
    raise Exception("You need a virtual environment to run this script")

PROJECT_NAME = os.path.basename(VIRTUAL_ENV)


def arguments():
    parser = argparse.ArgumentParser(
        description="Create a Sublime text python project file"
    )
    parser.add_argument(
        "-p",
        "--project",
        nargs="?",
        default=f"{DEFAULT_PROJECT_DIR}{PROJECT_NAME}",
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
    project_file = f"{args.destination}{project_name}.sublime-project"
    if os.path.isfile(project_file):
        return True
    return False


def create_project_file(args):
    project_name = os.path.basename(args.virtual_env)
    project = {
        "folders":
        [
            {
                "path": args.project
            }
        ],
        "settings":
        {
            "python_interpreter": f"{args.virtual_env}/bin/python"
        }
    }

    project_file = f"{args.destination}{project_name}.sublime-project"

    with open(project_file, "w+") as file:
        file.write(json.dumps(project, indent=4))


def print_args(args):
    print(f"Project: {args.project}")
    print(f"Virtual_env: {args.virtual_env}")
    print(f"Destination: {args.destination}")


if __name__ == "__main__":
    args = arguments()
    project_name = os.path.basename(args.virtual_env)
    project_file = f"{args.destination}{project_name}.sublime-project"
    shell_cmd = f"subl --project {project_file}"
    if project_file_exists():
        print(f"Opening: {project_file}")
        os.system(shell_cmd)
    else:
        print_args(args)
        user_input = input("Sublime Project does not exist, do you want to create a new one? \n[y/N]: ")
        if user_input.lower().strip() == "y":
            create_project_file(args)
            print(f"Creating new sublime project file at: {project_file}")
            os.system(shell_cmd)
        else:
            print("Cya")


    
    
