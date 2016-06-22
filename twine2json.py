"""
Author: Ben Byford - benbyford.com
"""

# import xml.etree to parse the xml https://docs.python.org/2/library/xml.etree.elementtree.html
import xml.etree.ElementTree as ET
from json import dump

# get html file
tree = ET.parse('example.html')

# find root xml node - this should be w-storydata with no empty attributes
root = tree.getroot()

# file variables
STORY_TAG = "tw-storydata"
PASSAGE_TAG = "tw-passagedata"
OUTPATH = r'example_output.json'


def parse_twine_file(node, data):

    tagname = node.tag
    attributes = node.attrib

    # add text to attributes if text available
    if node.text:
        attributes['text'] = node.text
        data.setdefault(PASSAGE_TAG, [])

        if tagname in data:
            data[tagname].append(attributes)
        else:
            data[tagname] = attributes

    for child in node:
        # data[child.tag] = childNode = dict()
        parse_twine_file(child, data)


# create dictionary for our data
def createJsonObj(root):

    data = dict()
    parse_twine_file(root, data)
    return data

# loop through data
data = createJsonObj(root)

with open(OUTPATH, 'w') as f:
    dump(data, f, indent=4)

print("file created sucessfully")
