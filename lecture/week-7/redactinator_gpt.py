# autocompleted with copilot in class


import pypdf
import os
import datetime


def save_string_to_file(text: str, file_location: str) -> None:
  """
  Save a string to a text file.

  Required arguments:
      text -- The string you would like to save.
      file_location -- The location of the
       text file to be output. E.g., 'output.txt'
       or 'some_folder/output.txt'.

  This function only saves the file; it
    does not return any output besides None.
  """

    # Create the directory if it doesn't exist
  os.makedirs(os.path.dirname(file_location), exist_ok=True)
  
  # Open the file in write mode and save the text
  with open(file_location, 'w', encoding='utf-8') as f:
      f.write(text)
      print(f"Saved text to {file_location}")