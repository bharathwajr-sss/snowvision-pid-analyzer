"""
Global project configuration.
"""

from pathlib import Path

# Root directory of the repository
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Folder locations
SAMPLE_IMAGE_DIR = PROJECT_ROOT / "sample_images"
OUTPUT_IMAGE_DIR = PROJECT_ROOT / "expected_output"

# Snowflake defaults
DATABASE = "PID_AI_DB"
SCHEMA = "PID"
STAGE = "PID_IMAGE_STAGE"

# Image settings
DEFAULT_IMAGE_FORMAT = ".png"
DEFAULT_DPI = 300
