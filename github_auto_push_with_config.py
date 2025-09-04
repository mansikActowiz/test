import os
import subprocess
import datetime
import json

# === Load config ===
with open("config.json", "r") as f:
    config = json.load(f)

repo_path = config["repo_path"]
github_username = config["github_username"]
repo_name = config["repo_name"]
branch_name = config["branch_name"]

repo_url = f"https://github.com/{github_username}/{repo_name}.git"

# === RUN ===
os.chdir(repo_path)

# Clear staged files first (so old junk doesn’t stay)
subprocess.run("git reset", shell=True)

# Stage only .py files (preserve folder structure)
for root, dirs, files in os.walk(repo_path):
    for file in files:
        if file.endswith(".py"):
            rel_path = os.path.relpath(os.path.join(root, file), repo_path)
            subprocess.run(f'git add "{rel_path}"', shell=True)

# Commit with timestamp
commit_message = f"Auto push (only .py files) on {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
subprocess.run(f'git commit -m "{commit_message}"', shell=True)

# Ensure branch + remote
subprocess.run(f"git branch -M {branch_name}", shell=True)
subprocess.run(f"git remote remove origin", shell=True)
subprocess.run(f"git remote add origin {repo_url}", shell=True)

# Pull latest changes
subprocess.run(f"git pull origin {branch_name} --rebase", shell=True)

# Push everything
subprocess.run(f"git push -u origin {branch_name}", shell=True)

























# import os
# import subprocess
# import datetime
# import json
#
# # === Load config ===
# with open("config_final.json", "r") as f:
#     config = json.load(f)
#
# repo_path = config["repo_path"]
# github_username = config["github_username"]
# repo_name = config["repo_name"]
# branch_name = config["branch_name"]
#
# repo_url = f"https://github.com/{github_username}/{repo_name}.git"
#
# # === RUN ===
# os.chdir(repo_path)
#
# # Stage ALL changes (new, modified, deleted files)
# subprocess.run("git add -A", shell=True)
#
# # Commit with timestamp
# commit_message = f"Auto push on {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
# subprocess.run(f'git commit -m "{commit_message}"', shell=True)
#
# # Ensure branch + remote
# subprocess.run(f"git branch -M {branch_name}", shell=True)
# subprocess.run(f"git remote remove origin", shell=True)
# subprocess.run(f"git remote add origin {repo_url}", shell=True)
#
# # Pull latest changes (safer: allow rebase only if clean)
# subprocess.run(f"git pull origin {branch_name} --rebase", shell=True)
#
# # Push everything
# subprocess.run(f"git push -u origin {branch_name}", shell=True)
