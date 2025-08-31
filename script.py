import os
import json

def fix_notebook(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            nb = json.load(f)

        # Check if metadata.widgets exists
        if "widgets" in nb.get("metadata", {}):
            widgets = nb["metadata"]["widgets"]
            
            # If 'state' key missing, add empty dict
            if "state" not in widgets:
                widgets["state"] = {}
                print(f"Fixed missing 'state' in: {path}")

            # (Optional) If you want to just remove widgets entirely:
            # nb["metadata"].pop("widgets")

        # Save notebook back
        with open(path, "w", encoding="utf-8") as f:
            json.dump(nb, f, indent=2)

    except Exception as e:
        print(f"❌ Error fixing {path}: {e}")

# Walk through all folders from current dir
for root, dirs, files in os.walk("."):
    for file in files:
        if file.endswith(".ipynb"):
            fix_notebook(os.path.join(root, file))
