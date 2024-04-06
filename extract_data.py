import re, json

data = open("wiki.txt", 'r').readlines()

result_data = {
    "1": 0,
    "2": 0,
    "3": 1
}

for line in data:
    line = line.replace("\n","")
    res = re.search(r'(\d+)-(\d+)..(\d+)', str(line))

    start, end, price = res.group(1), res.group(2), res.group(3)

    for i in range(int(start), int(end)+1):
        result_data[i] = int(price)

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(result_data, f, indent=4)