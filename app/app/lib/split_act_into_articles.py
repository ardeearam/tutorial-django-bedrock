import re
import sys
import time
import os

def split_document_stream_using_pattern(filepath, pattern):
    buffer = ''
    article_buffer = ''   #Prevent Article from matching again
    with open(filepath, 'r') as file:
        for line in file:
            buffer += line
            matches = re.split(pattern, buffer, maxsplit=1, flags=re.MULTILINE)
            if len(matches) > 1:
              yield article_buffer + "\n" + matches[0].strip()
              article_buffer = matches[1]
              buffer = ''
        if buffer.strip():
            yield buffer.strip()  # Yield the final part if there's leftover content

if __name__ == "__main__":

  source = sys.argv[1]
  output_directory = sys.argv[2]

  # Usage
  pattern = r'(?=\bArticle \d+[.]?)'  # Positive lookahead to retain headings
  for idx, subdoc in enumerate(split_document_stream_using_pattern(source, pattern), start=1):
    print("-" * 30)
    basename, ext = os.path.splitext(os.path.basename(source))
    subdocument_name = f"{basename}-{idx}{ext}"
    subdocument_fullpath = os.path.join(output_directory, subdocument_name)
    print(f"Subdocument {subdocument_fullpath}:\n")
    print(f"{subdoc[:100]}...")

    with open(subdocument_fullpath, 'w') as file:
      file.write(subdoc)

