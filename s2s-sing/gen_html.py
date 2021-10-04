import os
import sys
import fnmatch


def find_files(directory, pattern='*.wav'):
  '''Recursively finds all files matching the pattern.'''
  files = []
  for root, dirnames, filenames in os.walk(directory):
    for filename in fnmatch.filter(filenames, pattern):
        files.append(os.path.join(root, filename))
  return files


audio_files = find_files('audio/gt/', "*.wav")

for audio_name in audio_files:
    head = '<tbody>\n\t<tr>\n'
    body = ''
    for dname in ['gt','pho', 'pho-gau', 'state3-gau', 'state5-gau', 'state7-gau', 'fastspeech']:
        body += '\t<td><audio controls="" preload="auto"><source src="audio/%s/%s"></audio></td>\n' % (dname, os.path.basename(audio_name))
    tail = '\t<tr>\n</tbody>\n'

    print(head + body + tail)
