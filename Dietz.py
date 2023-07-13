import xml.etree.ElementTree as ET

class Node:
    def __init__(self, start, end, name):
        self.start = start
        self.end = end
        self.name = name

    def __str__(self):
        mystr = '(' + str(self.start) + ', '
        mystr += str(self.end) + ', '
        mystr += self.name + ')'
        return mystr
    
    def getStart(self):
        return self.start
    
def getStart(node):
    return node.getStart()

# Define a function to assign pre-order and post-order numbers to nodes in an ElementTree object
def assign_node_numbers(node, pre_order, post_order):
    pre_order[node] = len(pre_order)
    for child in node:
        if child.text:
            post_order[child.text] = len(post_order)
        assign_node_numbers(child, pre_order, post_order)
        if child.text:
            pre_order[child.text] = len(pre_order)
        
    post_order[node] = len(post_order)

# Parse the example XML document
tree = ET.parse('smallData.xml')
root = tree.getroot()

# Initialize dictionaries to store pre-order and post-order numbers for each node in the ElementTree object
pre_order = {}
post_order = {}

# Assign pre-order and post-order numbers to nodes in the ElementTree object
assign_node_numbers(root, pre_order, post_order)

listOfNodes = []

# sort pre_order dictionary on the 
sorted_preorder = sorted(pre_order.items(), key=lambda x:x[1])
for item in sorted_preorder:
    if type(item[0]) == ET.Element:
        listOfNodes.append(Node(pre_order[item[0]], post_order[item[0]], item[0].tag))
    elif type(item[0]) == str:
        listOfNodes.append(Node(pre_order[item[0]], post_order[item[0]], item[0]))

for node in listOfNodes:
    print(node)
