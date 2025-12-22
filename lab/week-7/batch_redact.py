import os
import datetime
import pypdf

def pdf_files(directory: str) -> list:
  """
  Returns a list of all files ending in '.pdf'
   in a given directory.

  Required argument:
      directory -- A directory presumably containing PDF
       files, e.g., 'documents'.

  Returns:
      an alphabetically-sorted list of all files
       ending in '.pdf' within directory, e.g.,
       ['document_a.pdf', 'document_b.pdf',
        'some_other_document.pdf']
  """

  docs = os.listdir(directory)

  pdfs_only = []

  for doc in docs:
    if doc.endswith('pdf'):
      pdfs_only.append(doc)

  return sorted(pdfs_only)


def pdf_to_string(file_location: str) -> str:
  
  """
  Converts a PDF, including a multi-page PDF,
    into a string, using the pypdf library.

  Required argument: 
      file_location -- The location of the PDF file to be
        converted, e.g., 'important_doc.pdf' or
        'some_folder/important_doc.pdf'

  Return:
      a string containing the text content of the
        PDF, including all pages
  """

  pdf_reader = pypdf.PdfReader(file_location)

  content = ''
  for page in pdf_reader.pages:
    content += page.extract_text()
    
  return content


def redact(text: str,
           text_to_redact: str,
           placeholder: str = 'REDACTED') -> tuple[str, int]:
  """
  Redact a string, replacing all instances
   of a substring with some placeholder string.

  Required arguments:
      text -- The string that you would like to process.
      text_to_redact -- The substring that you would
       like to search for and replace.

  Optional keyword argument:
      placeholder -- The placeholder that you would like to
       use to replace all instances of text_to_redact. Defaults to 'REDACTED'.

  Returns:
      tuple(redacted_text, n_redactions), where redacted_text
       is the redacted version of the text argument, and n_redactions 
       is the number of times that text_to_redact
       was found and replaced with placeholder.
  """


  n_redactions = text.count(text_to_redact)
  return text.replace(text_to_redact, placeholder), n_redactions

