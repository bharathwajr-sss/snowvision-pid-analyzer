"""
file_utils.py

Utility functions for file and directory operations.

Author: SnowVision Project
"""

import json
import shutil
from pathlib import Path
from typing import List


class FileUtils:
    """
    Utility class for common file operations.
    """

    IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".tif", ".tiff", ".bmp"}

    @staticmethod
    def create_directory(directory: Path) -> None:
        """
        Create a directory if it does not exist.
        """
        directory.mkdir(parents=True, exist_ok=True)

    @staticmethod
    def file_exists(file_path: Path) -> bool:
        """
        Check whether a file exists.
        """
        return file_path.exists()

    @staticmethod
    def get_image_files(directory: Path) -> List[Path]:
        """
        Return all supported image files.
        """
        if not directory.exists():
            return []

        return sorted(
            [
                file
                for file in directory.iterdir()
                if file.suffix.lower() in FileUtils.IMAGE_EXTENSIONS
            ]
        )

    @staticmethod
    def write_json(data: dict, output_file: Path) -> None:
        """
        Save dictionary as JSON.
        """
        output_file.parent.mkdir(parents=True, exist_ok=True)

        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

    @staticmethod
    def read_json(input_file: Path) -> dict:
        """
        Read JSON file.
        """
        with open(input_file, "r", encoding="utf-8") as f:
            return json.load(f)

    @staticmethod
    def copy_file(source: Path, destination: Path) -> None:
        """
        Copy file.
        """
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, destination)

    @staticmethod
    def delete_file(file_path: Path) -> None:
        """
        Delete file if it exists.
        """
        if file_path.exists():
            file_path.unlink()