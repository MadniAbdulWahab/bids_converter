import os
import logging
from config import CONFIG, BEH_JSON_CONTENT, JSON_STRUCTURE, EYE1_JSON_CONTENT, EYE2_JSON_CONTENT
from logger import setup_logging
from file_utils import create_output_directories, get_output_directory, create_root_files, create_participant_files
from data_conversion import convert_to_json, convert_to_tsv, convert_asc_to_tsv

def process_files_in_subfolders(base_folder, new_base_folder):
    """
    Walk through the base folder, process files, and convert them as specified.
    :param base_folder: The base folder to search for files.
    :param new_base_folder: The base folder for the new structure.
    """
    logging.info(f"Processing files in {base_folder}")
    for root, _, files in os.walk(base_folder):
        for filename in files:
            if CONFIG['csv_extension'] in filename and ('task-acquisition' in filename or 'task-extinction' in filename):
                file_path = os.path.join(root, filename)
                parts = filename.split(CONFIG['subject_session_delimiter'])
                if len(parts) < 2:
                    logging.warning(f"Filename {filename} does not contain enough parts to extract subject and session information.")
                    continue
                subject, session = parts[0], parts[1].split('.')[0]  # Remove extension from session part

                task_type = 'acquisition' if 'task-acquisition' in filename else 'extinction'
                output_dir = get_output_directory(new_base_folder, subject, session)
                os.makedirs(output_dir, exist_ok=True)

                output_filename_base = f"{subject}_{session}_task-DelayFearConditioning_{task_type}_events"

                # Create JSON file for events
                json_output_path = os.path.join(output_dir, f"{output_filename_base}{CONFIG['output_json_extension']}")
                convert_to_json(json_output_path, JSON_STRUCTURE)

                # Create TSV file
                tsv_output_path = os.path.join(output_dir, f"{output_filename_base}{CONFIG['output_tsv_extension']}")
                convert_to_tsv(file_path, tsv_output_path)

                # Create JSON file for behavior
                beh_json_output_path = os.path.join(output_dir, f"{subject}_{session}_task-DelayFearConditioning_beh{CONFIG['output_json_extension']}")
                convert_to_json(beh_json_output_path, BEH_JSON_CONTENT)

                # Create JSON file for eye1 physio
                eye1_json_output_path = os.path.join(output_dir, f"{subject}_{session}_task-DelayFearConditioning_recording-eye1_physio{CONFIG['output_json_extension']}")
                convert_to_json(eye1_json_output_path, EYE1_JSON_CONTENT)

                # Create JSON file for eye2 physio
                eye2_json_output_path = os.path.join(output_dir, f"{subject}_{session}_task-DelayFearConditioning_recording-eye2_physio{CONFIG['output_json_extension']}")
                convert_to_json(eye2_json_output_path, EYE2_JSON_CONTENT)

                # Create participant files in the phenotype folder
                create_participant_files(os.path.join(new_base_folder, subject))

            elif CONFIG['asc_extension'] in filename:
                file_path = os.path.join(root, filename)
                parts = filename.split(CONFIG['subject_session_delimiter'])
                if len(parts) < 2:
                    logging.warning(f"Filename {filename} does not contain enough parts to extract subject and session information.")
                    continue
                subject, session = parts[0], parts[1].split('.')[0]  # Remove extension from session part

                output_dir = get_output_directory(new_base_folder, subject, session)
                os.makedirs(output_dir, exist_ok=True)

                # Create TSV files for eye1 and eye2 recordings
                eye1_tsv_output_path = os.path.join(output_dir, f"{subject}_{session}_task-DelayFearConditioning_recording-eye1_physio{CONFIG['output_tsv_extension']}")
                eye2_tsv_output_path = os.path.join(output_dir, f"{subject}_{session}_task-DelayFearConditioning_recording-eye2_physio{CONFIG['output_tsv_extension']}")
                convert_asc_to_tsv(file_path, eye1_tsv_output_path, eye2_tsv_output_path)

                # Create participant files in the phenotype folder
                create_participant_files(os.path.join(new_base_folder, subject))

if __name__ == '__main__':
    setup_logging()
    script_dir = os.path.dirname(os.path.abspath(__file__))  # Directory where the script is located
    base_folder = os.path.join(script_dir, CONFIG['base_folder'])
    new_base_folder = os.path.join(script_dir, CONFIG['output_base_folder'])  # Folder to create the new structure
    os.makedirs(new_base_folder, exist_ok=True)
    logging.info(f"Created base output directory {new_base_folder}")
    create_output_directories(base_folder, new_base_folder)
    create_root_files(new_base_folder)
    process_files_in_subfolders(base_folder, new_base_folder)
