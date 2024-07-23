## Overview

This code is designed to process specific CSV and ASC files within a folder structure, converting them into JSON and TSV formats according to predefined rules, effectively transforming the data into the BIDS (Brain Imaging Data Structure) format. The code is divided into multiple Python scripts for better modularity and ease of maintenance.

## File Structure

- `config.py`: Contains configuration settings and constants.
- `logger.py`: Sets up the logging configuration.
- `file_utils.py`: Contains functions for directory creation and file structure handling.
- `data_conversion.py`: Functions for converting data to JSON and TSV.
- `main.py`: The main script that orchestrates the processing and conversion tasks.

## Installation

1. Clone the repository.
2. Navigate to the project directory.
3. Ensure you have Python 3.x installed.
4. Install necessary dependencies (mainly pandas) using:

```bash
pip install pandas
```

## Configuration (`config.py`)

This file contains configuration parameters such as file extensions, keywords and folder paths. It also defines the JSON structure template used for conversion.

## Logging Setup (`logger.py`)

This script sets up the logging configuration to record the progress and errors during execution.

## Directory and File Utilities (`file_utils.py`)

This module contains functions to create necessary directories and handle the file structure:

- create_output_directories(base_folder, new_base_folder): Creates directories in the new structure.
- get_output_directory(base_folder, subject, session): Gets the directory path for subject and session.
- create_root_files(new_base_folder): Creates dataset_description.json and readme.txt.
- create_participant_files(subject_dir): Creates participants.json and participants.tsv in the phenotype folder.


## Data Conversion Functions (`data_conversion.py`)

- convert_to_json(json_path, content): Writes JSON structure to a file.
- convert_to_tsv(file_path, output_path): Converts CSV to TSV.
- convert_asc_to_tsv(file_path, output_path_eye1, output_path_eye2): Converts ASC to TSV.


## Main Script (`main.py`)

This is the entry point of the project. It performs the following tasks:

1. Sets up logging.
2. Defines the base and output directories.
3. Creates output directories and root files.
4. Processes files and converts them.
5. Creates participant files.

### How to Run

1. Ensure all scripts (`config.py`, `logger.py`, `file_utils.py`, `data_conversion.py`, and `main.py`) are in the same directory.
2. Adjust the configuration in `config.py` to match your folder paths and file extensions.
3. Run the main script:

```bash
python main.py
```

The script will create the specified JSON and TSV files in the configured output directory.