import os
import glob
import datetime

# Define which language to use
lang = "en"
promt_type = "zero-shot"

# Define the source folders
folders = [f"./prompts/{lang}/{promt_type}/", "./functions-json/", "./types-json/"]

# Get the newest file from each folder
newest_files = []
for folder in folders:
    files = glob.glob(os.path.join(folder, "*"))
    newest_file = max(files, key=os.path.getctime)
    newest_files.append(newest_file)

# Combine the contents of the newest files
combined_content = ""
for file in newest_files:
    with open(file, "r") as f:
        content = f.read()
        if file.endswith("function-set.json"):
            combined_content = combined_content.replace("[functions]", content)
        elif file.endswith("type-set.json"):
            combined_content = combined_content.replace("[types]", content)
        else:
            combined_content += content

# Define the destination folder
destination_folder = f"./prompts/generated/{lang}/{promt_type}/"
os.makedirs(destination_folder, exist_ok=True)

# Save the combined content to the destination folder with the current date in the file name
current_date = datetime.datetime.now().strftime("%Y-%m-%d")
file_name = f"{current_date}-generated-{promt_type}-prompt.txt"

with open(os.path.join(destination_folder, file_name), "w") as f:
    f.write(combined_content)

print("Files combined and saved successfully!")
