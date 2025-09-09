import os
from constants import IMAGE_EXTENSIONS

from logger_functions import get_logger

logger = get_logger(__name__)

def allow_extension(file_name):
    """ To check if the file is an image based on its extension. """
    return os.path.splitext(file_name)[1].lower() in IMAGE_EXTENSIONS

def scan_directory(folder_path, task):
    '''
    Since I recently did a lot of DSA work, I thought of utilising my newly found knowledge
    and traverse all directories and subdirectories using an iterative approach with a stack
    and DFS (Depth-First Search) to avoid recursion.
    '''
    folders = 0
    files = 0
    folder_stack = [folder_path]
    while folder_stack:
        current_folder = folder_stack.pop()
        folders += 1
        logger.debug(f"Scanning directory: {current_folder}")
        logger.debug("-" * 80)
        try:
            with os.scandir(current_folder) as it:
                for entry in it:
                    if entry.is_dir(follow_symlinks=False):
                        folder_stack.append(entry.path)
                    elif entry.is_file(follow_symlinks=False) and allow_extension(entry.name):
                        logger.debug(f"Found {entry.name} at {current_folder}")
                        exif = task(entry.path)
                        files += 1
                        logger.debug(f"Metadata: {exif if exif else 'No metadata'}")
                        logger.debug("-" * 40)
        except PermissionError:
            logger.error(f"Permission denied: {current_folder}")
            continue
    logger.debug("-" * 80)
    logger.debug(f"{folders} folders scanned and {files} files found.")