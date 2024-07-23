import pandas as pd
import json
import os
import logging
from config import JSON_STRUCTURE, CONFIG, BEH_JSON_CONTENT, EYE1_JSON_CONTENT, EYE2_JSON_CONTENT

def convert_to_json(json_path, content):
    """
    Write the JSON structure to a file.
    :param json_path: Path to the output JSON file.
    :param content: The content to be written to the JSON file.
    """
    try:
        with open(json_path, 'w') as f:
            json.dump(content, f, indent=4)
        logging.info(f"Created JSON file at {json_path}")
    except Exception as e:
        logging.error(f"Failed to create JSON file {json_path}: {e}")

def convert_to_tsv(file_path, output_path):
    """
    Convert specific columns of a CSV file to TSV format.
    :param file_path: Path to the input CSV file.
    :param output_path: Path to the output TSV file.
    """
    try:
        df = pd.read_csv(file_path)
        df = df[['cs_onset', 'cs_dur', 'trial_type', 'us', 'shock_begin', 'shock_dur']]
        df = df.dropna(subset=['us'])  # Skip rows where 'us' is empty

        # Update trial_type values
        df['trial_type'] = df['trial_type'].replace({'CS+': 'CS1p', 'CS-': 'CS2m'})

        # Update stimulus_name values based on trial_type
        df['stimulus_name'] = df['trial_type'].map({'CS1p': 'square', 'CS2m': 'diamond'})

        # Prepare the DataFrame for TSV output
        tsv_rows = []
        for _, row in df.iterrows():
            tsv_rows.append([row['cs_onset'], row['cs_dur'], row['trial_type'], row['stimulus_name']])
            if row['us'] == 1:
                tsv_rows.append([row['shock_begin'], row['shock_dur'], 'US', 'shock'])

        result_df = pd.DataFrame(tsv_rows, columns=['onset', 'duration', 'trial_type', 'stimulus_name'])
        result_df.to_csv(output_path, sep='\t', index=False)
        logging.info(f"Converted {file_path} to {output_path}")
    except Exception as e:
        logging.error(f"Failed to convert {file_path} to TSV: {e}")

def convert_asc_to_tsv(file_path, output_path_eye1, output_path_eye2):
    """
    Convert an .asc file to two TSV files for eye1 and eye2 recordings.
    :param file_path: Path to the input .asc file.
    :param output_path_eye1: Path to the output TSV file for eye1.
    :param output_path_eye2: Path to the output TSV file for eye2.
    """
    try:
        eye1_rows = []
        eye2_rows = []
        with open(file_path, 'r') as file:
            for line in file:
                # Check if the line starts with a numeric timestamp
                if line[0].isdigit():
                    columns = line.split()
                    if len(columns) >= 7:
                        # Extract relevant columns for eye1 and eye2
                        eye1_rows.append([columns[3], columns[1], columns[2]])
                        eye2_rows.append([columns[6], columns[4], columns[5]])

        # Write the data directly to TSV files without headers
        with open(output_path_eye1, 'w') as f:
            for row in eye1_rows:
                f.write('\t'.join(row) + '\n')

        with open(output_path_eye2, 'w') as f:
            for row in eye2_rows:
                f.write('\t'.join(row) + '\n')

        logging.info(f"Converted {file_path} to {output_path_eye1} and {output_path_eye2}")
    except Exception as e:
        logging.error(f"Failed to convert {file_path} to TSV: {e}")

