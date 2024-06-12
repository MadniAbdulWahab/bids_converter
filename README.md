# BIDS Converter
This script converts and reorganizes files into the Brain Imaging Data Structure (BIDS) format. The script is designed to handle files in various formats, convert them to TSV format if necessary, and place them in a structured directory hierarchy based on subject and session identifiers.
## Features
Converts CSV and XLSX files to TSV format.
Organizes files into subject and session folders.
Detects and creates specific directories (e.g., `func`, `dwi`, `fmap`, etc.) if they exist in the original structure.
Moves session-specific files into their corresponding session folders.
## Installation
To use this script, you need to have Python installed along with the following packages:
`pandas`
You can install the required packages using pip:
```sh
pip install pandas
```
## Usage
Clone the repository:
```sh
git clone https://github.com/MadniAbdulWahab/bids_converter.git
```
Place your data in a folder and update the `CONFIG` dictionary in the script to point to your data folder.
Run the script:
```sh
python converter.py
```
## Logging
The script uses Python's built-in logging module to provide information about its progress and any issues encountered. Logs will be displayed in the console.
