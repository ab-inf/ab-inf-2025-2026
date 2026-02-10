# main.py

import subprocess
import argparse
from pathlib import Path


def main(dirs):
    theme_path = "../../theme.css"
    for dir_name in dirs:
        lesson_path = Path("lessons") / dir_name
        if not lesson_path.is_dir():
            continue
        print(f"Processing {lesson_path}")
        for md_file in lesson_path.glob("*.md"):
            print(f"  - Generating HTML and PPTX for {md_file.name}")
            commands = [
                ["npx", "@marp-team/marp-cli@latest", str(md_file), "-o", str(md_file.with_suffix(".html")), "--theme", theme_path],
                ["npx", "@marp-team/marp-cli@latest", str(md_file), "-o", str(md_file.with_suffix(".pptx")), "--theme", theme_path, "--allow-local-files"]
            ]
            for cmd in commands:
                subprocess.run(cmd, check=True)
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generates HTML/PPTX files from Markdown files using Marp.")
    parser.add_argument("folders", nargs="+", help="Subfolder names inside 'lessons' (e.g. 01 02 03...)")
    args = parser.parse_args()
    main(args.folders)
