import csv
import json

# 读取CSV文件
csv_file = 'test.csv'
json_file = 'test.json'

data = []
with open(csv_file, 'r', encoding='utf-8') as csvfile:
    csvreader = csv.DictReader(csvfile)
    for row in csvreader:
        data.append(row)

# 写入JSON文件
with open(json_file, 'w', encoding='utf-8') as jsonfile:
    json.dump(data, jsonfile, ensure_ascii=False, indent=4)

print(f'成功将{csv_file}转换为{json_file}')
