# import os
# import json

# def load_markdown_files(directory):
#     data = []
#     for filename in os.listdir(directory):
#         if filename.endswith(".md"):
#             filepath = os.path.join(directory, filename)
#             with open(filepath, "r", encoding="utf-8") as f:
#                 content = f.read()
#                 # Split into blocks by double line breaks
#                 blocks = [block.strip() for block in content.split("\n\n") if block.strip()]
#                 for block in blocks:
#                     data.append({
#                         "question": block,
#                         "answer": block,
#                         "source": filename
#                     })
#     return data

# if __name__ == "__main__":
#     md_directory = "knowledge_base"
#     all_data = load_markdown_files(md_directory)

#     print(f"Loaded {len(all_data)} entries from .md files.")

#     with open("database.json", "w", encoding="utf-8") as f:
#         json.dump(all_data, f, indent=2, ensure_ascii=False)
       

# import os
# import json

# def load_markdown_files(directory):
#     data = []
#     for filename in os.listdir(directory):
#         if filename.endswith(".md"):
#             filepath = os.path.join(directory, filename)
#             with open(filepath, "r", encoding="utf-8") as f:
#                 content = f.read().strip()

#                 # Use the first non-empty line as question
#                 lines = content.splitlines()
#                 question = next((line for line in lines if line.strip()), filename.replace(".md", ""))

#                 data.append({
#                     "question": question.strip(),
#                     "answer": content,
#                     "source": filename
#                 })
#     return data

# if __name__ == "__main__":
#     md_directory = "knowledge_base"
#     all_data = load_markdown_files(md_directory)

#     print(f"✅ Loaded {len(all_data)} full-document entries from .md files.")

#     with open("database.json", "w", encoding="utf-8") as f:
#         json.dump(all_data, f, indent=2, ensure_ascii=False)



# import os
# import json

# def load_markdown_files(directory):
#     data = []
#     for filename in os.listdir(directory):
#         if filename.endswith(".md"):
#             filepath = os.path.join(directory, filename)
#             with open(filepath, "r", encoding="utf-8") as f:
#                 content = f.read().strip()

#                 # Split into lines and get the first non-empty line as the question
#                 lines = content.splitlines()
#                 question = next((line.strip() for line in lines if line.strip()), filename.replace(".md", ""))

#                 # Store full content as the answer
#                 data.append({
#                     "question": question,
#                     "answer": content,
#                     "source": filename
#                 })
#     return data

# if __name__ == "__main__":
#     md_directory = "knowledge_base"
#     all_data = load_markdown_files(md_directory)

#     print(f"✅ Loaded {len(all_data)} entries from markdown files.")

#     with open("database.json", "w", encoding="utf-8") as f:
#         json.dump(all_data, f, indent=2, ensure_ascii=False)



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


