import os
import sys
import re


def combine_files(folder_path):
    # Get a list of all files in the specified folder
    files = os.listdir(folder_path)

    # Create a dictionary to store file contents by rank
    file_contents_by_rank = {}

    # Iterate through the files and organize them by rank
    for file_name in files:
        if file_name.startswith("file_rank"):
            match = re.match(r"file_rank(\d+)_(\w+)", file_name)
            if match:
                rank = int(match.group(1))
                
                with open(os.path.join(folder_path, file_name), "r") as file:
                    content = file.read()
                    
                if rank not in file_contents_by_rank:
                    file_contents_by_rank[rank] = []
                file_contents_by_rank[rank].append(content)

    # Create the 'updated_dump_files' folder if it doesn't exist
    updated_folder_path = os.path.join("updated_dump_files")
    os.makedirs(updated_folder_path, exist_ok=True)

    # Combine and save files by rank
    for rank, contents in file_contents_by_rank.items():
        combined_content = "\n".join(contents)
        combined_file_name = f"file_rank{rank}_combine.pt"

        with open(
            os.path.join(updated_folder_path, combined_file_name), "w"
        ) as combined_file:
            combined_file.write(combined_content)


if __name__ == "__main__":
    if len(sys.argv) != 2 or sys.argv[1].lower() != "combine":
        print("Usage: python main.py combine")
    else:
        folder_path = "dump_files"  # Update this with the actual path to your folder
        combine_files(folder_path)
