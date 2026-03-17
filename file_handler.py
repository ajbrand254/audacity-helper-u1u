import os
import shutil
from datetime import datetime
from filelock import FileLock
from logzero import logger
import zipfile

class FileHandler:
    def __init__(self, project_dir):
        self.project_dir = project_dir
        self.backup_dir = os.path.join(project_dir, 'backups')
        self.ensure_backup_directory()

    def ensure_backup_directory(self):
        """Ensure the backup directory exists."""
        if not os.path.exists(self.backup_dir):
            os.makedirs(self.backup_dir)

    def backup_project(self):
        """Create a backup of the .aup file and associated data."""
        try:
            # Find the .aup file
            aup_file = self.find_aup_file()
            if not aup_file:
                raise FileNotFoundError("No .aup file found in the project directory.")
            
            # Define backup file name
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            backup_file_name = f"{os.path.splitext(os.path.basename(aup_file))[0]}_backup_{timestamp}.aup"
            backup_file_path = os.path.join(self.backup_dir, backup_file_name)

            # Copy the .aup file
            shutil.copy2(aup_file, backup_file_path)
            logger.info(f"Backup created: {backup_file_path}")

            # Backup associated data (e.g., .au files)
            self.backup_associated_data(aup_file)

        except Exception as e:
            logger.error(f"Error during backup: {e}")

    def find_aup_file(self):
        """Find the first .aup file in the project directory."""
        if not os.path.exists(self.project_dir):
            return None
        for file in os.listdir(self.project_dir):
            if file.endswith('.aup'):
                return os.path.join(self.project_dir, file)
        return None

    def backup_associated_data(self, aup_file):
        """Backup associated .au files based on the .aup file."""
        if not os.path.exists(self.project_dir):
            return
        base_name = os.path.splitext(aup_file)[0]
        for file in os.listdir(self.project_dir):
            if file.startswith(base_name) and file.endswith('.au'):
                source_file = os.path.join(self.project_dir, file)
                backup_file_path = os.path.join(self.backup_dir, f"{file}")
                shutil.copy2(source_file, backup_file_path)
                logger.info(f"Associated data backed up: {backup_file_path}")

# TODO: Implement version control in backups to avoid clutter.
# TODO: Add a method to restore from a backup.
# TODO: Consider adding CLI support for user interaction.
