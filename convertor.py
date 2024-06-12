import os
import pandas as pd
import logging
import shutil
import re
# Configuration parameters
CONFIG = {
    'csv_extension': '.csv',
    'xlsx_extension': '.xlsx',
    'output_extension': '.tsv',
    'events_keyword': 'task',
    'subject_session_delimiter': '_',
    'base_folder': 'Leuven',
    'output_base_folder': 'converted_folder'
}
# List of specific directories to look for
SPECIFIC_DIRS = [
    'func', 'dwi', 'fmap', 'anat', 'perf', 'meg', 'eeg', 'ieeg', 'beh',
    'pet', 'micr', 'nirs', 'motion'
]
# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
def convert_to_tsv(file_path, output_path, read_func):
    """
    Convert a file to TSV format using the provided read function.
    :param file_path: Path to the input file.
    :param output_path: Path to the output TSV file.
    :param read_func: Function to read the input file.
    """
    try:
        df = read_func(file_path)
        df.to_csv(output_path, sep='\t', index=False)
        logging.info(f"Converted {file_path} to {output_path}")
    except Exception as e:
        logging.error(f"Failed to convert {file_path} to TSV: {e}")
def process_file(file_path, output_path, filename):
    """
    Process a single file and convert it to TSV format if applicable.
    :param file_path: Path to the input file.
    :param output_path: Path to the output file.
    :param filename: Name of the input file.
    """
    if filename.endswith(CONFIG['csv_extension']):
        convert_to_tsv(file_path, output_path, pd.read_csv)
    elif filename.endswith(CONFIG['xlsx_extension']):
        convert_to_tsv(file_path, output_path, pd.read_excel)
def create_output_directories(subject, session, sub_dir, new_base_folder):
    """
    Create directories for subject, session, and specific subdirectory if they don't exist.
    :param subject: Subject identifier.
    :param session: Session identifier.
    :param sub_dir: Specific subdirectory (e.g., 'func', 'dwi').
    :param new_base_folder: Base folder for the new structure.
    :return: Path to the specific subdirectory inside the session folder.
    """
    specific_folder = os.path.join(new_base_folder, subject, session, sub_dir) if sub_dir else os.path.join(new_base_folder, subject, session)
    os.makedirs(specific_folder, exist_ok=True)
    return specific_folder
def copy_other_files_to_base(root, filename, new_base_folder):
    """
    Copy other files that are not CSV or XLSX to the new base folder.
    :param root: The root directory where the file is located.
    :param filename: The name of the file.
    :param new_base_folder: The base folder for the new structure.
    """
    source_path = os.path.join(root, filename)
    destination_path = os.path.join(new_base_folder, filename)
    shutil.copy2(source_path, destination_path)
    logging.info(f"Copied {source_path} to {destination_path}")
def move_session_files(new_base_folder):
    """
    Move files that contain ses- and a number to their corresponding session folders.
    :param new_base_folder: The base folder for the new structure.
    """
    for filename in os.listdir(new_base_folder):
        if re.search(r'ses-\d+', filename):
            subject, session = filename.split(CONFIG['subject_session_delimiter'])[0], re.search(r'ses-\d+', filename).group()
            for dir_name in SPECIFIC_DIRS:
                specific_folder_path = os.path.join(new_base_folder, subject, session, dir_name)
                if os.path.exists(specific_folder_path):
                    shutil.move(os.path.join(new_base_folder, filename), os.path.join(specific_folder_path, filename))
                    logging.info(f"Moved {filename} to {specific_folder_path}")
                    break
            else:
                session_folder = create_output_directories(subject, session, '', new_base_folder)
                shutil.move(os.path.join(new_base_folder, filename), os.path.join(session_folder, filename))
                logging.info(f"Moved {filename} to {session_folder}")
def process_files_in_subfolders(base_folder, new_base_folder):
    """
    Walk through the base folder, process files, and convert them to TSV format.
    :param base_folder: The base folder to search for files.
    :param new_base_folder: The base folder for the new structure.
    """
    logging.info(f"Processing files in {base_folder}")
    for root, dirs, files in os.walk(base_folder):
        for filename in files:
            file_path = os.path.join(root, filename)
            if filename.endswith((CONFIG['csv_extension'], CONFIG['xlsx_extension'])):
                parts = filename.split(CONFIG['subject_session_delimiter'])
                if len(parts) < 2:
                    logging.warning(f"Filename {filename} does not contain enough parts to extract subject and session information.")
                    continue
                subject, session = parts[0], parts[1]
                specific_dir = next((d for d in SPECIFIC_DIRS if d in root), '')
                session_folder = create_output_directories(subject, session, specific_dir, new_base_folder)
                new_filename = filename.replace(CONFIG['csv_extension'], CONFIG['output_extension']).replace(CONFIG['xlsx_extension'], CONFIG['output_extension'])
                if CONFIG['events_keyword'] in filename:
                    new_filename = new_filename.replace(CONFIG['output_extension'], f'_events{CONFIG["output_extension"]}')
                output_path = os.path.join(session_folder, new_filename)
                process_file(file_path, output_path, filename)
            else:
                copy_other_files_to_base(root, filename, new_base_folder)
def create_specific_folders(base_folder, new_base_folder):
    """
    Create specific folders in the new structure if they are present in the old structure.
    :param base_folder: The base folder to search for folders.
    :param new_base_folder: The base folder for the new structure.
    """
    specific_folders_to_create = set()
    for root, dirs, _ in os.walk(base_folder):
        for dir_name in dirs:
            if dir_name in SPECIFIC_DIRS:
                relative_path = os.path.relpath(root, base_folder)
                parts = relative_path.split(os.sep)
                if len(parts) >= 2:
                    subject, session = parts[-2], parts[-1]
                    specific_folders_to_create.add((subject, session, dir_name))
                else:
                    logging.warning(f"Unable to determine subject and session from path {relative_path}")
    for subject, session, dir_name in specific_folders_to_create:
        create_output_directories(subject, session, dir_name, new_base_folder)
def move_files_to_specific_folders(new_base_folder):
    """
    Move files to specific folders in the new structure if they are present in the old structure.
    :param new_base_folder: The base folder for the new structure.
    """
    move_session_files(new_base_folder)
if __name__ == '__main__':
    script_dir = os.path.dirname(os.path.abspath(__file__))  # Directory where the script is located
    base_folder = os.path.join(script_dir, CONFIG['base_folder'])
    new_base_folder = os.path.join(script_dir, CONFIG['output_base_folder'])   # Folder to create the new structure
    os.makedirs(new_base_folder, exist_ok=True)
    logging.info(f"Created base output directory {new_base_folder}")
    create_specific_folders(base_folder, new_base_folder)
    process_files_in_subfolders(base_folder, new_base_folder)
    move_files_to_specific_folders(new_base_folder)