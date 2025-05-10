import os

# Path to your assignment repo (adjust if needed)
repo_path = "/Volumes/DevDereks/python-assignments"
dashboard_file = os.path.join(repo_path, "dashboards", "index.html")

# Your GitHub username and repo name
github_user = "dmac90712"
repo_name = "python-assignments"

# Build a list of completed modules
completed_modules = []
for folder in os.listdir(repo_path):
    if folder.startswith("module") and os.path.isdir(os.path.join(repo_path, folder)):
        for file in os.listdir(os.path.join(repo_path, folder)):
            if file.endswith(".ipynb"):
                completed_modules.append((folder, file))
                break

# Generate new HTML content
html_content = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Python Assignment Dashboard</title>
  <style>
    body { font-family: Arial, sans-serif; padding: 2em; background: #f9f9f9; }
    h1 { color: #0066cc; }
    ul { list-style: none; padding: 0; }
    li.assignment { padding: 0.75em; margin: 0.5em 0; background: #fff; border-left: 6px solid #ccc; }
    li.complete { border-left-color: #4caf50; background-color: #e8f5e9; }
    a { text-decoration: none; color: #0066cc; }
  </style>
</head>
<body>
  <h1>Python Assignment Progress</h1>
  <ul>
"""

for folder, notebook in sorted(completed_modules):
    module_label = folder.replace("module", "Module ")
    github_link = f"https://github.com/{github_user}/{repo_name}/blob/main/{folder}/{notebook}"
    html_content += f"""    <li class="assignment complete" id="{folder}">
      ✅ {module_label} – Completed<br>
      <a href="{github_link}" target="_blank">[View Notebook]</a>
    </li>\n"""

html_content += """  </ul>
</body>
</html>"""

# Save the updated dashboard
with open(dashboard_file, "w") as f:
    f.write(html_content)

print(f"✅ Dashboard updated at: {dashboard_file}")
