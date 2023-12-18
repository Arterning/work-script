import pandas as pd
from sqlalchemy import create_engine

# 读取Excel文件
excel_file = 'test.xlsx'
df = pd.read_excel(excel_file)

# 重命名列以映射到数据库表字段
column_mapping = {'适种地区': 'region', '省份': 'province'}
df = df.rename(columns=column_mapping)

# 数据库连接配置
db_config = {
    'user': 'root',
    'password': '123456',
    'host': 'localhost',
    'port': 3306,
    'database': 'test'
}

# 创建数据库连接
engine = create_engine(f'mysql+mysqlconnector://{db_config["user"]}:{db_config["password"]}@{db_config["host"]}:{db_config["port"]}/{db_config["database"]}')

# 将数据写入MySQL表
table_name = 'variety_suitable_region'
df.to_sql(name=table_name, con=engine, if_exists='replace', index=False)

# 关闭数据库连接
engine.dispose()

print(f'Data imported to MySQL table {table_name} successfully.')
