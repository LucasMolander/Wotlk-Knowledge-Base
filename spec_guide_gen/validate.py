#
# This file valides every guide to make sure it matches the schema,
# i.e. which attributes every guide should have.
#
# This is to enforce that every guide has the same attributes, so
# they can all be generated using the same code (see gen.py).
#
from jsonschema import validate

from file_util import FileUtil


def getSchema():
  return {
    'type': 'object',
    'properties': {
      'Spec':            {'type': 'string'},
      'Original Author': {'type': 'string'},
      'Original Link':   {'type': 'string'},
      'Strengths':       {'type': 'array', 'items': {'type': 'string'}},
      'Weaknesses':      {'type': 'array', 'items': {'type': 'string'}}
    }
  }


def validateGuide(filePath):
  schema = getSchema()
  guide = FileUtil.getJSONContents(filePath)
  if (guide == None):
    return False

  validatingStr = 'Validating %s...' % filePath
  print(validatingStr)
  try:
    validate(guide, schema)
    return True
  except Exception as e:
    print('-' * len(validatingStr))
    print('%s\n\n' % e)
    return False


def main():
  guides = FileUtil.getJSONContents('guides.json')
  if (guides == None):
    exit(1)

  validGuides   = []
  invalidGuides = []

  for g in guides:
    if (validateGuide(guides[g])):
      validGuides.append(g)
    else:
      invalidGuides.append(g)
    print()

  if (len(validGuides) > 0):
    print('\n%d valid guide(s):' % len(validGuides))
    for vg in validGuides:
      print('\t%s' % vg)
  else:
    print('0 valid guides')
  print()

  if (len(invalidGuides) > 0):
    print('%d invalid guide(s):' % len(invalidGuides))
    for ivg in invalidGuides:
      print('\t%s' % ivg)
  else:
    print('0 invalid guides')
  print()


if __name__ == '__main__':
  main()
