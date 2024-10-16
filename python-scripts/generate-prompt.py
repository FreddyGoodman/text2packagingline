import os
import glob
import datetime

levels = ["0-convert-to-call", "1-compute-robots", "2-compute-machines", "3-structure-line"]
prompt_types = ["0-specific-instruction", "1-general-instruction"]
# Define which language to use
lang = "en"
level = 3
prompt_type = 0

# Define the source folders
folders = [f"./prompts/{lang}/{levels[level]}/{prompt_types[prompt_type]}/", "./functions-json/", "./types-json/", "./world-knowledge"]

# Get the newest file from each folder
newest_files = []
for folder in folders:
    files = glob.glob(os.path.join(folder, "*"))
    newest_file = max(files, key=os.path.getctime)
    newest_files.append(newest_file)

# Combine the contents of the newest files
combined_content = ""
for i, file in enumerate(newest_files):
    with open(file, "r") as f:
        content = f.read()
        if i == 1:
            combined_content = combined_content.replace("[functions]", content)
        elif i == 2:
            combined_content = combined_content.replace("[types]", content)
        elif i == 3:
            combined_content = combined_content.replace("[world-knowledge]", content)
        else:
            combined_content += content

# Define the destination folder
destination_folder = f"./prompts/generated/{lang}/"
os.makedirs(destination_folder, exist_ok=True)

# Save the combined content to the destination folder with the current date in the file name
current_date = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
file_name = f"{current_date}-{levels[level]}-{prompt_types [prompt_type]}.txt"

with open(os.path.join(destination_folder, file_name), "w") as f:
    f.write(combined_content)

print("Files combined and saved successfully!")
