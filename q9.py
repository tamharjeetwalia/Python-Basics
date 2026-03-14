import os
import shutil
import hashlib
from datetime import datetime


VERSIONS_FOLDER = "versions"


def file_hash(filepath):

    sha = hashlib.sha256()

    with open(filepath, "rb") as f:

        while True:

            chunk = f.read(8192)

            if not chunk:
                break

            sha.update(chunk)

    return sha.hexdigest()


def ensure_version_folder():

    os.makedirs(VERSIONS_FOLDER, exist_ok=True)


def get_version_number(filename):

    name = os.path.basename(filename)

    version = 1

    while True:

        version_file = os.path.join(
            VERSIONS_FOLDER,
            f"{name}_v{version}"
        )

        if not os.path.exists(version_file):
            return version

        version += 1


def save_version(filepath):

    ensure_version_folder()

    version = get_version_number(filepath)

    name = os.path.basename(filepath)

    dest = os.path.join(VERSIONS_FOLDER, f"{name}_v{version}")

    shutil.copy2(filepath, dest)

    print(f"Saved version: {dest}")


def track_directory(directory):

    hashes = {}

    while True:

        for file in os.listdir(directory):

            path = os.path.join(directory, file)

            if not os.path.isfile(path):
                continue

            h = file_hash(path)

            if file not in hashes:

                hashes[file] = h
                save_version(path)

            elif hashes[file] != h:

                hashes[file] = h
                save_version(path)

        input("\nPress ENTER to check again...")


def restore_version():

    versions = os.listdir(VERSIONS_FOLDER)

    if not versions:

        print("No versions available.")
        return

    print("\nAvailable Versions:\n")

    for i, v in enumerate(versions):

        print(f"{i+1}. {v}")

    choice = int(input("\nSelect version to restore: ")) - 1

    version_file = versions[choice]

    original_name = version_file.split("_v")[0]

    src = os.path.join(VERSIONS_FOLDER, version_file)

    shutil.copy2(src, original_name)

    print(f"Restored {original_name}")


def main():

    print("1 Track Directory")
    print("2 Restore File Version")

    choice = input("Choose option: ")

    if choice == "1":

        directory = input("Enter directory path: ")

        track_directory(directory)

    elif choice == "2":

        restore_version()


if __name__ == "__main__":
    main()