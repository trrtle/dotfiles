#! /bin/python3

import argparse
import json
import os

HOME = os.path.expanduser("~")
DEFAULT_VIRTUALENV_LOCATION = f"{HOME}/devel/venv/virtualenvs/"
DEFAULT_PROJECT_DIR = f"{HOME}/devel/projects/sublime/"
CWD = os.getcwd()


def arguments():
    parser = argparse.ArgumentParser(
        description="Create a Sublime text python project file"
    )

    parser.add_argument(
        "project_name",
        action="store",
        help="Name of the project (must be the same as virtual environment)"
    )
    parser.add_argument(
        "-p",
        "--project",
        nargs="?",
        default=CWD,
        help="Directory where your python projects reside"
    )
    parser.add_argument(
        "-d",
        "--destination",
        nargs="?",
        default=DEFAULT_PROJECT_DIR,
        help="Sublime project file directory"
    )
    parser.add_argument(
        "-v",
        "--venv_dir",
        nargs="?",
        default=DEFAULT_VIRTUALENV_LOCATION,
        help="Directory where python virtual environments reside"
    )

    return parser.parse_args()


def create_project_file(args):
    project = {
        "folders":
        [
            {
                "path": args.project
            }
        ],
        "settings":
        {
            "python_interpreter": f"{args.venv_dir}{args.project_name}/bin/python"
        }
    }

    project_file = f"{args.destination}{args.project_name}.sublime-project"

    if os.path.isfile(project_file):
        return False
    else:
        with open(project_file, "w+") as file:
            file.write(json.dumps(project, indent=4))
        return True


if __name__ == "__main__":
    args = arguments()
    file_created = create_project_file(args)
    project_file = f"{args.destination}{args.project_name}.sublime-project"
    if file_created:
        print(f"Creating new sublime project file at: {project_file}")
    else:
        print(f"project already exists at: {project_file}")\

    shell_cmd = f"subl --project {project_file}"
    os.system(shell_cmd)
