import re


def check_web_address(text):
  pattern = r"^[\w\.\+-]+\.[a-zA-Z]*$"
  result = re.search(pattern, text)
  return False if result is None else True


if __name__ == "__main__":
    check_web_address
