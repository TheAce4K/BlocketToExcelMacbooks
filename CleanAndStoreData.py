import json
import re

def read_json(json_file):
    with open(json_file, 'r') as f:
        json_content = json.load(f)
        f.close()
    return json_content


def get_data_from_json(json_content):
    clean_json = []
    for product in json_content:
        title_match = re.search(r'(m1 (pro|max))|(M1 (pro|max))|(M1 (Pro|Max))', product['title'])
        if title_match:
            name = title_match.group(0)
            cpu = [re.search(r'(8|10).?[cC](?![. ]?[Ggm])', product['title']),
                   re.search(r'(8|10).?[cC](?![. ]?[Ggm])', product['description'])]
            if cpu[0]:
                cpu_cores = cpu[0].group(1)
            elif cpu[1]:
                cpu_cores = cpu[1].group(1)
            else:
                cpu_cores = ''
            gpu = [
                re.search(r'(14|16|24|32) ?[cC]?( ?GPU| ?gpu) ?(?![. ]?[cCm])', product['title']),
                re.search(r'(14|16|24|32) ?[cC]?( ?GPU| ?gpu) ?(?![. ]?[cCm])', product['description'])
            ]
            if gpu[0]:
                gpu_cores = gpu[0].group(1)
            elif gpu[1]:
                gpu_cores = gpu[1].group(1)
            else:
                gpu_cores = ''
            ram = [
                re.search(r'(16|32|64) ?(GB|Gb|gb)', product['title']),
                re.search(r'(16|32|64) ?(GB|Gb|gb)', product['description'])
            ]
            if ram[0]:
                ram_memory = ram[0].group(1)
            elif ram[1]:
                ram_memory = ram[1].group(1)
            else:
                ram_memory = ''
            item = {
                'title': product['title'],
                'name': name,
                'cpu_cores': cpu_cores,
                'gpu_cores': gpu_cores,
                'ram_memory': ram_memory,
                'price': product['price'],
                'location': product['location'],
                'link': product['link']
            }
            clean_json.append(item)
    return clean_json



def clean_and_store_data(json_name):
    json_content = read_json(json_name)
    clean_json = get_data_from_json(json_content)
    return clean_json
