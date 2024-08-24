import os
from random import randint
from datetime import datetime, timedelta

# Hardcoded GitHub username and email
GITHUB_USERNAME = "hmcadet54"
GITHUB_EMAIL = "hmcadet54@gmail.com"

# Hardcoded start and end dates (format: YYYY-MM-DD)
START_DATE = "2023-01-01"
END_DATE = "2023-12-31"

# Configure Git with the hardcoded username and email
os.system(f'git config user.name "{GITHUB_USERNAME}"')
os.system(f'git config user.email "{GITHUB_EMAIL}"')

# Convert string dates to datetime objects
start_date = datetime.strptime(START_DATE, "%Y-%m-%d")
end_date = datetime.strptime(END_DATE, "%Y-%m-%d")

# Calculate the number of days between start and end dates
num_days = (end_date - start_date).days + 1

for i in range(num_days):
    current_date = start_date + timedelta(days=i)
    for j in range(randint(1, 10)):
        commit_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
        with open('file.txt', 'a') as file:
            file.write(f"Commit on {commit_date}\n")
        os.system('git add .')
        os.system(f'git commit --date="{commit_date}" -m "commit"')

# Push to the main branch of the origin remote
os.system('git push -u origin main')