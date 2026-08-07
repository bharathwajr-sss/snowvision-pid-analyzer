from pathlib import Path

from python.utils.file_utils import FileUtils

TEST_DIR = Path("tests/data")
JSON_FILE = TEST_DIR / "sample.json"

# Create test folder
FileUtils.create_directory(TEST_DIR)

# Test JSON Write
sample_data = {
    "project": "SnowVision",
    "version": 1
}

FileUtils.write_json(sample_data, JSON_FILE)

print("JSON written.")

# Test JSON Read
loaded = FileUtils.read_json(JSON_FILE)

print("Loaded JSON:")
print(loaded)

# Test Exists
print("File Exists:", FileUtils.file_exists(JSON_FILE))

# Test Delete
FileUtils.delete_file(JSON_FILE)

print("Deleted:", not FileUtils.file_exists(JSON_FILE))