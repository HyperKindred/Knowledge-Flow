from bs4 import BeautifulSoup
import json

def parse_html_to_mindmap(html_content, note_name):
    soup = BeautifulSoup(html_content, 'html.parser')
    id_counter = {}

    def create_node(id, topic, children=None):
        if children is None:
            children = []
        return {"id": id, "topic": topic, "children": children}

    def generate_id(tag):
        tag_name = tag.name
        base_id = tag_name + "_" + "_".join(tag.get_text().strip().split()[:4])
        if base_id in id_counter:
            id_counter[base_id] += 1
        else:
            id_counter[base_id] = 1
        return f"{base_id}_{id_counter[base_id]}"

    def get_text_preview(tag):
        text = tag.get_text().strip()
        return text[:20] + ('...' if len(text) > 20 else '')

    def traverse(element):
        stack = []
        nodes = []
        last_level = 0

        while element:
            if element.name and element.name.startswith('h') and element.name[1].isdigit():
                current_level = int(element.name[1])
                node_id = generate_id(element)
                node = create_node(node_id, element.get_text().strip())

                if current_level > last_level:
                    if stack:
                        stack[-1]['children'].append(node)
                    else:
                        nodes.append(node)
                    stack.append(node)
                elif current_level == last_level:
                    if stack:
                        stack.pop()
                    if stack:
                        stack[-1]['children'].append(node)
                    else:
                        nodes.append(node)
                    stack.append(node)
                else:
                    while stack and int(stack[-1]['id'][1]) >= current_level:
                        stack.pop()
                    if stack:
                        stack[-1]['children'].append(node)
                    else:
                        nodes.append(node)
                    stack.append(node)

                last_level = current_level

            elif element.name == 'p':
                node_id = generate_id(element)
                node = create_node(node_id, get_text_preview(element))
                if stack:
                    stack[-1]['children'].append(node)
                else:
                    nodes.append(node)

            elif element.name in ['ul', 'ol']:
                list_items = element.find_all('li', recursive=False)
                for li in list_items:
                    node_id = generate_id(li)
                    node = create_node(node_id, get_text_preview(li))
                    if stack:
                        stack[-1]['children'].append(node)
                    else:
                        nodes.append(node)

            element = element.find_next_sibling()

        return nodes

    root = create_node("root", note_name)
    root['children'] = traverse(soup.find())
    
    return json.dumps(root, indent=4)

