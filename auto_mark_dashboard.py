import os
import json
from pathlib import Path

# Paths and config
base_path = Path("/Volumes/DevDereks/python-assignments")
modules = [f"module{i}" for i in range(1, 7)]
quiz_file = base_path / "quiz_status.json"
output_html = base_path / "dashboards/index.html"

# Load manual quiz completion
with open(quiz_file, 'r') as f:
    quiz_status = json.load(f)

# HTML content
html_output = [
    "<!DOCTYPE html>",
    "<html>",
    "<head>",
    "<meta charset='UTF-8'>",
    "<title>Python Assignment Progress</title>",
    "<style>body{font-family:sans-serif; padding:20px;} .card{padding:10px;margin:10px 0;border-radius:6px}",
    ".complete{background:#d4edda} .partial{background:#fff3cd} .none{background:#f8d7da}",
    "h2{margin:0} a{font-size:0.9em} code{background:#eee;padding:2px 4px;border-radius:4px;}</style>",
    "</head><body><h1 style='color:#0077cc'>Python Assignment Progress</h1>"
]

# Loop through each module
for module in modules:
    module_path = base_path / module
    assignment_done = False
    assignment_file = ""
    quiz_done = quiz_status.get(module, False)

    print(f"\n🔎 Checking {module}...")

    if module_path.exists() and module_path.is_dir():
        files = os.listdir(module_path)
        for file in files:
            if file.endswith('.ipynb') or file.endswith('.py'):
                assignment_done = True
                assignment_file = file
                print(f"✅ Found assignment: {file}")
                break
        if not assignment_done:
            print("⚠️ No assignment file found.")
    else:
        print("❌ Module folder not found.")

    if quiz_done:
        print("📝 Quiz marked as completed.")
    else:
        print("📌 Quiz not completed.")

    # Determine status
    if assignment_done and quiz_done:
        status = "✅"
        css_class = "complete"
        label = "Assignment + Quiz Completed"
    elif assignment_done or quiz_done:
        status = "🟡"
        css_class = "partial"
        label = "Partially Complete"
    else:
        status = "❌"
        css_class = "none"
        label = "Not Started"

    # Add to HTML
    html_output.append(f"<div class='card {css_class}'>")
    html_output.append(f"<h2>{status} {module.capitalize()} – {label}</h2>")

    if assignment_done:
        rel_path = os.path.join(module, assignment_file)
        html_output.append(f"<p>📄 Assignment: <code>{assignment_file}</code> — <a href='../{rel_path}' target='_blank'>Open</a></p>")
    else:
        html_output.append("<p>📄 Assignment: <em>Not Found</em></p>")

    html_output.append(f"<p>📝 Quiz: {'✅ Completed' if quiz_done else '❌ Not Completed'}</p>")
    html_output.append("</div>")

  # Count completed modules
completed_modules = 0
for module in modules:
    mod_path = base_path / module
    has_assignment = mod_path.exists() and any(
        file.endswith('.py') or file.endswith('.ipynb')
        for file in os.listdir(mod_path)
    ) if mod_path.exists() else False
    has_quiz = quiz_status.get(module, False)
    if has_assignment and has_quiz:
        completed_modules += 1

total_modules = len(modules)
percent_complete = int((completed_modules / total_modules) * 100)

# Progress bar HTML
html_output.append("<h2>Progress</h2>")
html_output.append(f"<div style='background:#eee;border-radius:5px;width:100%;height:24px;margin-bottom:10px;'>")
html_output.append(f"<div style='background:#4caf50;height:100%;width:{percent_complete}%;border-radius:5px;text-align:center;color:white;font-weight:bold;'>")
html_output.append(f"{completed_modules} of {total_modules} complete")
html_output.append("</div></div>")

# Write HTML output
html_output.append("</body></html>")
with open(output_html, 'w') as f:
    f.write('\n'.join(html_output))

print(f"\n✅ Dashboard updated at: {output_html}")