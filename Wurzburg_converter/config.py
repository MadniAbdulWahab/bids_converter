CONFIG = {
    'csv_extension': '.csv',
    'asc_extension': '.asc',
    'output_tsv_extension': '.tsv',
    'output_json_extension': '.json',
    'events_keyword': 'task',
    'subject_session_delimiter': '_',
    'base_folder': 'Wurzburg',
    'output_base_folder': 'converted_folder'
}

JSON_STRUCTURE = {
    "onset": {
        "LongName": "Onset",
        "Description": "Stimulus onset",
        "Units": "second"
    },
    "duration": {
        "LongName": "Duration",
        "Description": "Stimulus duration",
        "Units": "second"
    },
    "trial_type": {
        "LongName": "Trial Type",
        "Description": "Trial type as defined in abstract terms",
        "Levels": {
            "CS+": "Conditioned stimulus coupled with US",
            "CS-": "Conditioned stimulus never coupled with US",
            "US": "Unconditioned stimulus",
            "block_start": "Start of trial block",
            "block_end": "End of trial block"
        }
    },
    "stimulus_name": {
        "LongName": "Identifier",
        "Description": "Stimulus identifier",
        "Levels": {
            "diamond": "A diamond with \u2026 degrees visual angle",
            "square": "A square with \u2026 degrees visual angle",
        }
    }
}

BEH_JSON_CONTENT = {
    "TaskName": "Delay fear conditioning",
    "TaskDescription": "Task Description",
    "Instructions": "Task Instructions",
    "CogAtlasID": "https://www.cognitiveatlas.org/task/id/trm_5023ef8eab626/",
    "CogPOID": "http://wiki.cogpo.org/index.php?title=Classical_Conditioning_Paradigm",
    "InstitutionName": "unknown",
    "InstitutionAddress": "Wurzburg",
    "SOA": 3.5
}

EYE1_JSON_CONTENT = {
  "Columns": [
    "pupil_size",
    "x_coordinate",
    "y_coordinate"
  ],
  "EnvironmentCoordinates": "top-left",
  "Manufacturer": "Eyelink",
  "ManufacturersModelName": "EYELINK II",
  "RecordedEye": "left",
  "SampleCoordinateSystem": "gaze-on-screen",
  "SampleCoordinateUnits": "pixel",
  "SamplingFrequency": 1000,
  "SoftwareVersion": "Eyelink II CL v5.15 Jan 24 2018",
  "ScreenAOIDefinition": [
    "square",
    [
      100,
      150,
      300,
      350
    ]
  ],
  "StimulusPresentation": {
    "ScreenDistance": 0.6,
    "ScreenRefreshRate": [
      1920,
      1080
    ],
  "ScreenResolution": [
      1024,
      768
    ],
    "ScreenSize": [
      350,
      200
    ]
  },
  "pupil_size": {
    "Description": "Pupil diameter",
    "Units": "pixels"
  },
  "MaximalCalibrationError": None,
  "AverageCalibrationError": "0.50 deg",
  "EyetrackingGeometry": {
    "distances": {
      "EyeToCameraX": 495,
      "EyeToCameraY": 50,
      "EyeToCameraZ": 400,
      "EyeToScreenTopLeftX": 700,
      "EyeToScreenTopLeftY": 50,
      "EyeToScreenTopLeftZ": 400
    },
    "distanceUnits": "mm"
  },
  "BestEye": "r",
  "ElclProc": "ellipse",
  "GazeRange": {
    "xmin": 0,
    "ymin": 0,
    "xmax": 1920,
    "ymax": 1080
  },
  "RecordingDuration": 644.491
}

EYE2_JSON_CONTENT = {
  "Columns": [
    "pupil_size",
    "x_coordinate",
    "y_coordinate"
  ],
  "EnvironmentCoordinates": "top-left",
  "Manufacturer": "Eyelink",
  "ManufacturersModelName": "EYELINK II",
  "RecordedEye": "right",
  "SampleCoordinateSystem": "gaze-on-screen",
  "SampleCoordinateUnits": "pixel",
  "SamplingFrequency": 1000,
  "SoftwareVersion": "Eyelink II CL v5.15 Jan 24 2018",
  "ScreenAOIDefinition": [
    "square",
    [
      100,
      150,
      300,
      350
    ]
  ],
  "StimulusPresentation": {
    "ScreenDistance": 0.6,
    "ScreenRefreshRate": [
      1920,
      1080
    ],
    "ScreenResolution": [
      1024,
      768
    ],
    "ScreenSize": [
      350,
      200
    ]
  },
  "pupil_size": {
    "Description": "Pupil diameter",
    "Units": "mm"
  },
  "MaximalCalibrationError": None,
  "AverageCalibrationError": None,
  "EyetrackingGeometry": {
    "distances": {
      "EyeToCameraX": 495,
      "EyeToCameraY": 50,
      "EyeToCameraZ": 400,
      "EyeToScreenTopLeftX": 700,
      "EyeToScreenTopLeftY": 50,
      "EyeToScreenTopLeftZ": 400
    },
    "distanceUnits": "mm"
  },
  "BestEye": "r",
  "ElclProc": "ellipse",
  "GazeRange": {
    "xmin": 0,
    "ymin": 0,
    "xmax": 1151,
    "ymax": 863
  },
  "RecordingDuration": 2237.832
}

DATASET_DESCRIPTION_CONTENT = {
    "Name": "PupilBench",
    "BIDSVersion": "1.9.0"
}

README_CONTENT = "sample readme"

PARTICIPANTS_JSON_CONTENT = {
    "participant_id": {
        "Description": "Unique identifier for each participant"
    },
    "age": {
        "Description": "Age of the participant"
    },
    "sex": {
        "Description": "Sex of the participant"
    }
}

PARTICIPANTS_TSV_CONTENT = """participant_id\tage\tsex
388\t24\tm
"""
