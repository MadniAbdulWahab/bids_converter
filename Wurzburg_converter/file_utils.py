import os
import logging
import json
from config import DATASET_DESCRIPTION_CONTENT, README_CONTENT, PARTICIPANTS_JSON_CONTENT, PARTICIPANTS_TSV_CONTENT

def create_output_directories(base_folder, new_base_folder):
    """
    Create specific folders in the new structure if they are present in the old structure.
    :param base_folder: The base folder to search for folders.
    :param new_base_folder: The base folder for the new structure.
    """
    specific_folders_to_create = set()
    for root, dirs, _ in os.walk(base_folder):
        for dir_name in dirs:
            relative_path = os.path.relpath(root, base_folder)
            parts = relative_path.split(os.sep)
            if len(parts) >= 2:
                subject, session = parts[-2], parts[-1]
                specific_folders_to_create.add((subject, session, dir_name))
            else:
                logging.warning(f"Unable to determine subject and session from path {relative_path}")
    for subject, session, dir_name in specific_folders_to_create:
        specific_folder = os.path.join(new_base_folder, subject, session, 'beh', dir_name)
        os.makedirs(specific_folder, exist_ok=True)

def get_output_directory(base_folder, subject, session):
    """
    Get the directory path for the subject and session in the new structure.
    :param base_folder: The base folder for the new structure.
    :param subject: The subject identifier.
    :param session: The session identifier.
    :return: Path to the specific directory inside the subject and session folder.
    """
    return os.path.join(base_folder, subject, session, 'beh')

def create_root_files(new_base_folder):
    """
    Create the dataset_description.json and readme.txt files in the root directory.
    :param new_base_folder: The base folder for the new structure.
    """
    dataset_description_path = os.path.join(new_base_folder, 'dataset_description.json')
    with open(dataset_description_path, 'w') as f:
        json.dump(DATASET_DESCRIPTION_CONTENT, f, indent=4)
    logging.info(f"Created {dataset_description_path}")

    readme_path = os.path.join(new_base_folder, 'readme.txt')
    with open(readme_path, 'w') as f:
        f.write(README_CONTENT)
    logging.info(f"Created {readme_path}")

def create_participant_files(subject_dir):
    """
    Create the participants.json and participants.tsv files in the phenotype directory.
    :param subject_dir: The subject directory where the phenotype folder will be created.
    """
    phenotype_dir = os.path.join(subject_dir, 'phenotype')
    os.makedirs(phenotype_dir, exist_ok=True)

    participants_json_path = os.path.join(phenotype_dir, 'participants.json')
    with open(participants_json_path, 'w') as f:
        json.dump(PARTICIPANTS_JSON_CONTENT, f, indent=4)
    logging.info(f"Created {participants_json_path}")

    participants_tsv_path = os.path.join(phenotype_dir, 'participants.tsv')
    with open(participants_tsv_path, 'w') as f:
        f.write(PARTICIPANTS_TSV_CONTENT)
    logging.info(f"Created {participants_tsv_path}")
