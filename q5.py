import os
import hashlib
import shutil


def calculate_hash(filepath):

    sha256 = hashlib.sha256()

    with open(filepath, "rb") as f:

        while True:

            chunk = f.read(4096)

            if not chunk:
                break

            sha256.update(chunk)

    return sha256.hexdigest()


def find_duplicates(directory):

    hashes = {}

    duplicates = []

    files = os.listdir(directory)

    for file in files:

        path = os.path.join(directory, file)

        if not os.path.isfile(path):
            continue

        file_hash = calculate_hash(path)

        if file_hash in hashes:

            duplicates.append(path)

        else:

            hashes[file_hash] = path

    return duplicates


def handle_duplicates(duplicates):

    if not duplicates:

        print("No duplicate files found")

        return

    print("\nDuplicate Files:\n")

    for i, file in enumerate(duplicates):

        print(f"{i+1}. {file}")

    print("\n1 Delete duplicates")
    print("2 Move duplicates")

    choice = input("\nChoose option: ")

    if choice == "1":

        for file in duplicates:

            os.remove(file)

            print(f"Deleted {file}")

    elif choice == "2":

        folder = input("Enter folder to move duplicates: ")

        os.makedirs(folder, exist_ok=True)

        for file in duplicates:

            shutil.move(file, folder)

            print(f"Moved {file} → {folder}")


def create_report(duplicates):

    with open("duplicate_report.txt", "w") as f:

        for file in duplicates:

            f.write(file + "\n")


def main():

    directory = input("Enter directory path: ")

    duplicates = find_duplicates(directory)

    handle_duplicates(duplicates)

    create_report(duplicates)

    print("\nReport saved as duplicate_report.txt")


if __name__ == "__main__":

    main()