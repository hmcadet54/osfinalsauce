import os
import subprocess
from datetime import datetime, timedelta

# Hardcoded variables
repo_path = r"D:\All_Repos_by_hmcadet54\osfinalsauce"  # Replace with your actual repo path
start_date = datetime(2023, 8, 1)  # Replace with your desired start date
remote_name = "origin"  # Replace with your remote name if different
branch_name = "main"    # Replace with your branch name if different

# User-specific information
git_user_name = "hmcadet54"
git_user_email = "hmcadet54@gmail.com"  # Replace with the actual email

def setup_git_user():
    subprocess.run(["git", "config", "user.name", git_user_name])
    subprocess.run(["git", "config", "user.email", git_user_email])

def create_commit_and_push(date):
    # Change to the repository directory
    os.chdir(repo_path)
    
    # Create or update a file
    with open("contribution_test.txt", "a") as f:
        f.write(f"Contribution test on {date.strftime('%Y-%m-%d')}\n")
    
    # Stage the file
    subprocess.run(["git", "add", "contribution_test.txt"])
    
    # Create a commit with the specified date
    commit_message = f"Contribution test for {date.strftime('%Y-%m-%d')}"
    subprocess.run([
        "git", "commit", 
        "-m", commit_message,
        "--date", date.isoformat()
    ])
    
    # Push the commit to the remote repository
    subprocess.run(["git", "push", remote_name, branch_name])

# Main execution
if __name__ == "__main__":
    setup_git_user()
    
    current_date = start_date
    today = datetime.now()
    
    while current_date <= today:
        create_commit_and_push(current_date)
        current_date += timedelta(days=1)
    
    print(f"Commits created and pushed from {start_date.strftime('%Y-%m-%d')} to {today.strftime('%Y-%m-%d')} as user {git_user_name}")