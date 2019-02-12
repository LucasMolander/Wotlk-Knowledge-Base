#
# Contains useful helper functions for files.
#
import json


class FileUtil(object):

  @staticmethod
  def getJSONContents(filePath):
    try:
      with open(filePath, 'rb') as f:
        return json.loads(f.read())
    except Exception as e:
      print('Failed to read JSON contents of %s: %s' % (filePath, e))
      return None


  @staticmethod
  def write(filePath, contents):
    try:
      with open(filePath, 'w') as f:
        f.write(contents)
      return True
    except Exception as e:
      print('Failed to write contents to %s: %s' % (filePath, e))
      return False


  @staticmethod
  def stripEnding(theString, ending):
    if (theString == ending):
      print('theString == ending')
      return None

    idx = theString.rfind(ending)
    if (idx < 0):
      print('ending not found in theString')
      return None

    return theString[0 : idx]
