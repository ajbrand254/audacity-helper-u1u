import os
import shutil
import time
import logging
from datetime import datetime

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def create_backup(project_path):
    """
    Create a backup of the Audacity project files.
    
    Args:
        project_path (str): The path to the Audacity project directory.
        
    Returns:
        str: The path to the created backup directory.
    """
    # Check if the project path exists
    if not os.path.exists(project_path):
        logging.error("The specified project path does not exist: %s", project_path)
        return None

    # Create a timestamped backup directory name
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    backup_path = f"{project_path}_backup_{timestamp}"

    try:
        # Copy the project directory to the backup location
        shutil.copytree(project_path, backup_path)
        logging.info("Backup created successfully at: %s", backup_path)
    except Exception as e:
        logging.error("Failed to create backup: %s", e)
        return None

    return backup_path

if __name__ == "__main__":
    # Example usage: Change this to your Audacity project path
    project_directory = "path/to/your/audacity/project"
    
    # Create a backup
    backup_dir = create_backup(project_directory)
    
    if backup_dir:
        logging.info("Backup completed. You can find it at: %s", backup_dir)
    else:
        logging.error("Backup process encountered an error.")
