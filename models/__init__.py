#!/usr/bin/python3
"""Initialize and reload the FileStorage instance."""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
