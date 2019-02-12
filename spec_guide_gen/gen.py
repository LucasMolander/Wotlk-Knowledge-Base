#
# Turns the guides' JSON into HTML.
#
# WARNING
# This file assumes that each guide is valid,
# i.e. `python validate.py` reports "0 invalid guides"
#

from file_util import FileUtil


def getGuideContents(guide):
  out = ''

  #
  # Heading section
  #
  out += '<h1>%s</h1>' % guide['Spec']
  out += '<hr />'
  out += '<p>Original author: %s (<a href="%s">view on Warmane</a>)</p>' % \
    (guide['Original Author'], guide['Original Link'])

  #
  # Strengths and weaknesses
  #
  out += "<h2>Strengths & Weaknesses</h2>"

  out += "<h3>Strengths</h3>"
  if (len(guide['Strengths']) == 0):
    out += '<p>None! Consider playing a different spec, lol</p>'
  else:
    out += '<ul>'
    for s in guide['Strengths']:
      out += '<li>%s</li>' % s
    out += '</ul>'

  out += "<h3>Weaknesses</h3>"
  if (len(guide['Weaknesses']) == 0):
    out += '<p>None! This must be a great class to play :)</p>'
  else:
    out += '<ul>'
    for w in guide['Weaknesses']:
      out += '<li>%s</li>' % w
    out += '</ul>'

  return out



def genGuide(filePath):
  outDir = '../spec_guides'

  noEnding = FileUtil.stripEnding(filePath, '.json')
  if (noEnding == None):
    return False

  outPath = '%s/%s.html' % (outDir, noEnding)

  guide = FileUtil.getJSONContents(filePath)
  if (guide == None):
    return False
  
  generatingStr = 'Generating %s...' % filePath
  print(generatingStr)
  try:
    contents = getGuideContents(guide)
    return FileUtil.write(outPath, contents)
  except Exception as e:
    print('-' * len(generatingStr))
    print('%s\n\n' % e)
    return False


def main():
  guides = FileUtil.getJSONContents('guides.json')
  if (guides == None):
    exit(1)

  successes = []
  failures  = [] # Tag yourself

  for g in guides:
    if (genGuide(guides[g])):
      successes.append(g)
    else:
      failures.append(g)
    print()

  if (len(successes) > 0):
    print('\n%d succssful generation(s):' % len(successes))
    for s in successes:
      print('\t%s' % s)
  else:
    print('0 successful generations')
  print()

  if (len(failures) > 0):
    print('%d failed generation(s):' % len(failures))
    for f in failures:
      print('\t%s' % f)
  else:
    print('0 failed generations')
  print()


if __name__ == '__main__':
  main()
