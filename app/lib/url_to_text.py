import requests
from bs4 import BeautifulSoup
import sys

def url_to_text(url):

  response = requests.get(url)
  soup = BeautifulSoup(response.text, "html.parser")
  return soup.get_text()

if __name__ == "__main__":

  if len(sys.argv) < 2:
    raise ValueError("You must pass in a URL to this script.")

  url = sys.argv[1]
  print("Crawling and cleaning ", sys.argv[1], "...", file=sys.stderr)
  print(url_to_text(url))
