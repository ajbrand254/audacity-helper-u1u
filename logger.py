import os
import logging
from datetime import datetime

# Set up logging configuration
LOG_FILE = 'backup_operations.log'

def get_logger():
    """Get configured logger instance."""
    logger = logging.getLogger('BackupLogger')
    
    # Avoid adding duplicate handlers
    if not logger.handlers:
        logger.setLevel(logging.DEBUG)
        
        # Create file handler which logs even debug messages
        fh = logging.FileHandler(LOG_FILE)
        fh.setLevel(logging.DEBUG)
        
        # Create formatter and add it to the handler
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        
        # Add the handler to the logger
        logger.addHandler(fh)
    
    return logger

# Get the logger instance
logger = get_logger()

def log_backup_operation(file_path, backup_path):
    """
    Log the details of a backup operation.

    :param file_path: The original file path that is being backed up.
    :param backup_path: The path where the backup is stored.
    """
    if not os.path.isfile(file_path):
        logger.error(f"Backup failed: The file {file_path} does not exist.")
        return

    backup_dir = os.path.dirname(backup_path) or '.'
    if not os.path.isdir(backup_dir):
        logger.error(f"Backup failed: The directory for {backup_path} does not exist.")
        return

    logger.info(f"Backup created from {file_path} to {backup_path}")

def log_error(message):
    """
    Log an error message to the log file.

    :param message: The error message to log.
    """
    logger.error(message)

def log_warning(message):
    """
    Log a warning message to the log file.

    :param message: The warning message to log.
    """
    logger.warning(message)

# TODO: Add log rotation for large log files
# TODO: Implement different logging levels for different components of the application
# TODO: Consider using a logging configuration file for more flexibility

if __name__ == "__main__":
    # Example usage of the logger
    log_backup_operation('example.aup', 'backup/example_backup.aup')  # Change with actual paths for testing
    log_error("This is a test error message.")
    log_warning("This is a test warning message.")
