import subprocess
import logging

logging.basicConfig(
    filename="update_log.txt",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)


def check_updates():
    print("\nChecking for available updates...\n")

    result = subprocess.run(
        ["apt", "list", "--upgradable"],
        capture_output=True,
        text=True
    )

    lines = result.stdout.split("\n")

    packages = []

    for line in lines[1:]:
        if line.strip():
            packages.append(line.split("/")[0])

    for i, pkg in enumerate(packages):
        print(f"{i+1}. {pkg}")

    return packages


def update_all():

    print("\nUpdating all packages...\n")

    try:
        subprocess.run(["sudo", "apt", "upgrade", "-y"])
        print("All packages updated successfully.")
        logging.info("All packages updated successfully")

    except Exception as e:
        print("Update failed.")
        logging.error(f"Update failed: {e}")


def update_selected(packages):

    choice = input("\nEnter package index numbers (comma separated): ")

    indices = choice.split(",")

    for i in indices:

        try:

            pkg = packages[int(i)-1]

            print(f"\nUpdating {pkg}...\n")

            subprocess.run(["sudo", "apt", "install", "--only-upgrade", "-y", pkg])

            logging.info(f"{pkg} updated successfully")

        except Exception as e:

            print(f"Failed to update {pkg}")
            logging.error(f"{pkg} update failed: {e}")


def main():

    packages = check_updates()

    if not packages:
        print("No updates available.")
        return

    print("\nOptions:")
    print("1. Update all packages")
    print("2. Update selected packages")

    option = input("\nChoose option: ")

    if option == "1":
        update_all()

    elif option == "2":
        update_selected(packages)

    else:
        print("Invalid option.")


if __name__ == "__main__":
    main()