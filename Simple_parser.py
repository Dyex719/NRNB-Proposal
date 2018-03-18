from xml.dom import minidom
# This file has been obtained from https://github.com/SynBioDex/SBOL-visual/blob/master/Glyphs/engineered-region/engineered-region-specification.svg
doc = minidom.parse("engineered-region-specification.svg")
path_strings = [path.getAttribute('d') for path in doc.getElementsByTagName('path')]
print(path_strings)
# Outputs: ['m 2.4999973,12.499997 0,20 39.9999997,0 0,-20 z',
# 'm -5.9265904,33.914 c 56.8531754,0 56.8531754,0 56.8531754,0']


# This can also be done using the svgpathtools package
from svgpathtools import svg2paths
paths, attributes = svg2paths('engineered-region-specification.svg')
for k, v in enumerate(attributes):
    print(v['d'])
# Outputs:
# m 2.4999973,12.499997 0,20 39.9999997,0 0,-20 z
# m -5.9265904,33.914 c 56.8531754,0 56.8531754,0 56.8531754,0

# After obtaining the element, the parser would have to modify the elements
# based on user input, thus modifying the file.

doc.unlink()
