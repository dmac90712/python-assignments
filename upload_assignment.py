import os
import shutil
import subprocess

# === SETTINGS ===
module_number = "6"
notebook_name = "derekmccrary_cs82b_loan_default_assignment.ipynb"
local_notebook_path = f"/Volumes/DevDereks/python-assignments/module6/{notebook_name}"
repo_path = os.getcwd()
target_folder = os.path.join(repo_path, f"module{module_number}")
commit_message = f"Add final notebook for Module {module_number}"

# === STEP 1: Ensure target folder exists ===
os.makedirs(target_folder, exist_ok=True)


# === STEP 3: Git add, commit, push ===
subprocess.run(["git", "add", f"module{module_number}/{notebook_name}"])
subprocess.run(["git", "commit", "-m", commit_message])
subprocess.run(["git", "push", "origin", "main"])

print("🚀 Notebook uploaded to GitHub successfully.")