import re

# Regular expression matching whitespace:
_whitespace_re = re.compile(r'\s+')

def lowercase(text):
  return text.lower()

def collapse_whitespace(text):
  return re.sub(_whitespace_re, ' ', text)

def basic_cleaners(text):
  '''Basic pipeline that lowercases and collapses whitespace without transliteration.'''
  text = lowercase(text)
  text = collapse_whitespace(text)
  return text