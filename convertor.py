import os
import pandas as pd

def convert_csv_to_tsv(file_path, output_path):
    df = pd.read_csv(file_path)
    df.to_csv(output_path, sep='\t', index=False)

def convert_xlsx_to_tsv(file_path, output_path):
    df = pd.read_excel(file_path)
    df.to_csv(output_path, sep='\t', index=False)

def process_files_in_subfolders(base_folder, new_base_folder):
    for root, dirs, files in os.walk(base_folder):
        for filename in files:
            if filename.endswith('.csv') or filename.endswith('.xlsx'):
                # Extract subject and session information from filename
                parts = filename.split('_')
                subject = parts[0]
                session = parts[1]

                # Create subject directory in the new base folder if it doesn't exist
                subject_folder = os.path.join(new_base_folder, subject)
                if not os.path.exists(subject_folder):
                    os.makedirs(subject_folder)

                # Create session directory inside the subject directory if it doesn't exist
                session_folder = os.path.join(subject_folder, session)
                if not os.path.exists(session_folder):
                    os.makedirs(session_folder)

                # Define input and output file paths
                file_path = os.path.join(root, filename)
                new_filename = filename.replace('.csv', '.tsv').replace('.xlsx', '.tsv')
                if 'task' in filename:
                    new_filename = new_filename.replace('.tsv', '_events.tsv')
                output_path = os.path.join(session_folder, new_filename)

                # Convert files to TSV format
                if filename.endswith('.csv'):
                    convert_csv_to_tsv(file_path, output_path)
                elif filename.endswith('.xlsx'):
                    convert_xlsx_to_tsv(file_path, output_path)

if __name__ == '__main__':
    script_dir = os.path.dirname(__file__)  # Directory where the script is located
    folder_name = 'Leuven'
    base_folder = os.path.join(script_dir, folder_name) 
    new_base_folder = os.path.join(script_dir, 'converted_folder')   # Folder to create the new structure

    # Create the new base folder if it doesn't exist
    if not os.path.exists(new_base_folder):
        os.makedirs(new_base_folder)

    process_files_in_subfolders(base_folder, new_base_folder)