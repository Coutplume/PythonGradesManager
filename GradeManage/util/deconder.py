import base64
import pandas as pd
from io import BytesIO


def deconder(data: str) -> dict:
    # 将data解码为二进制数据
    excel_data = base64.b64decode(data)
    # 将数据转化为字节流
    excel_file = BytesIO(excel_data)
    # 读取文件对象并转换为 DataFrame 对象
    df = pd.read_excel(excel_file)
    # 将 DataFrame 对象转换为字典的形式
    excel_dict = df.to_dict()
    return excel_dict
