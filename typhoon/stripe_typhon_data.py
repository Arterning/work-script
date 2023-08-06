# -*- coding: UTF-8 -*-
import datetime

# 读取原始文本数据
with open('taili.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

# 提取表头（列名）
columns = lines[0].split()
columns = ['datetime', 'speed', 'typhoon']

# 初始化 INSERT 语句和值
insert_statement = "INSERT INTO ag_typhoon ({}) VALUES".format(", ".join(columns))
values = []

# 处理每行数据
for line in lines[1:]:
    data = line.split()
    # 时间字段转换为 datetime 格式，假设时间格式为 "0806 17h"
    date_time = "2023-{}-{} {}:00:00".format(data[0][:2], data[0][2:4], data[1][:2])
    # 风速字段转换为整数，保留数字部分
    wind_speed = int(data[2][:-3])
    # 台风名字段
    typhoon_name = "泰利"
    # 构建 VALUES 部分
    values.append("('{}', {}, '{}')".format(date_time, wind_speed, typhoon_name))

# 将 VALUES 部分连接到 INSERT 语句中
insert_statement += ",\n".join(values) + ";"

# 打印 INSERT SQL 语句
print(insert_statement)

# 获取当前时间的时间戳
timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")

# 将 INSERT SQL 语句保存到 SQL 文件中
output_file = 'output_{}.sql'.format(timestamp)

with open(output_file, 'w', encoding='utf-8') as sql_file:
    sql_file.write(insert_statement)

print("INSERT SQL 语句已保存到 {}".format(output_file))
