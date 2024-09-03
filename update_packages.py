import subprocess


def get_outdated_packages():
    result = subprocess.run(
        ["pip", "list", "--outdated"], capture_output=True, text=True
    )
    lines = result.stdout.split("\n")
    packages = [line.split()[0] for line in lines[2:] if line]
    return packages


def upgrade_package(package):
    subprocess.run(["pip", "install", "--upgrade", package])


def main():
    packages = get_outdated_packages()
    for package in packages:
        print(f"Upgrading {package}...")
        upgrade_package(package)
    print("All packages are up to date.")


if __name__ == "__main__":
    main()
