import os
import json
import re

def load_markdown_files(directory):
    data = []
    for filename in os.listdir(directory):
        if filename.endswith(".md"):
            filepath = os.path.join(directory, filename)
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()

                # Split based on sub-headings (e.g., ## Connect to Google Sheets)
                sections = re.split(r'\n##\s+', content)
                for section in sections:
                    if not section.strip():
                        continue
                    lines = section.strip().split("\n", 1)
                    if len(lines) == 2:
                        heading, body = lines
                    else:
                        heading = "General"
                        body = lines[0]

                    data.append({
                        "question": heading.strip(),
                        "answer": body.strip(),
                        "source": filename 
                    })
    return data

if __name__ == "__main__":
    md_directory = "knowledge_base"
    all_data = load_markdown_files(md_directory)

    print(f"✅ Loaded {len(all_data)} entries from markdown files.")

    with open("database.json", "w", encoding="utf-8") as f:
        json.dump(all_data, f, indent=2, ensure_ascii=False)


