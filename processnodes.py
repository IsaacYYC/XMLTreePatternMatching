import xml.etree.ElementTree as ET

xml_data = '''<?xml version="1.0" ?>
<publication>
<journal><title>DBMS</title></journal>
<editor>Jack</editor>
<article>
<title>
Index
</title>
<author>Smith</author>
</article>
<journal>
<title>Algorithm</title>
</journal>
</publication>'''

doc_id = 1
position = 1
level = 0
nodes = []

def process_node(node, doc_id, position, level):
    start = position

    node_info = {
        'tag_or_text': node.tag,
        'start': start,
        'end': -1,
        'level': level,
    }
    nodes.append(node_info)

    if node.text and node.text.strip():
        position += 1
        text_info = {
            'tag_or_text': node.text.strip(),
            'start': position,
            'end': position,
            'level': level + 1,
        }
        nodes.append(text_info)

    level += 1
    for child in node:
        position, _ = process_node(child, doc_id, position + 1, level)

    position += 1
    end = position
    node_info['end'] = end

    return end, level

tree = ET.ElementTree(ET.fromstring(xml_data))
root = tree.getroot()

process_node(root, doc_id, position, level)

for node in nodes:
    print(f"{node['tag_or_text']}\n({doc_id},{node['start']}:{node['end']},{node['level']})")
