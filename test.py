# List of packages to keep
keep_packages = [
    "numpy==1.26.3",
    "pandas==2.2.0",
    "pillow==10.2.0",
    "requests==2.31.0",
    "tqdm==4.66.2",
    "Jinja2==3.1.3",
    "prettytable==3.9.0",
    "pyperclip==1.8.2",
    "python-dateutil==2.8.2",
    "pytz==2023.3.post1",
]

# Read the current requirements file
with open("requirements.txt", "r") as file:
    lines = file.readlines()

# Filter out the packages to keep
lines = [line for line in lines if line.strip() in keep_packages]

# Write the new requirements file
with open("requirements.txt", "w") as file:
    file.writelines(lines)
