import yaml, os

class Read_Data:

    def __init__(self, file_name):
        # 拼接文件路径
        self.file_path = os.getcwd() + os.sep + "Data" + os.sep + file_name

    def get_test_data(self):
        # 返回文件数据
        with open(self.file_path, "r", encoding="utf-8") as f:
            return yaml.load(f)