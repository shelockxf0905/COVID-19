"""
@ProjectName: Covid-2019
@FileName: json_info.py
@Author: xiao-yi.yu
@Date: 2020/04/28
"""
import logging


logging.basicConfig(filename='read_json.log',
                    format='%(asctime)s - %(levelname)s -%(module)s:  %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S %p',
                    level=10)


class covid_info:
    # [欧洲-葡萄牙]/[中国-上海]
    name = ''
    # 累计确诊数
    confirmed_count = 0
    # 疑似病例数
    suspected_count = 0
    # 治愈病例数
    cured_count = 0
    # 死亡病例数
    dead_count = 0
    # 死亡率
    dead_rate = 0.0
    # 更新日期
    update_date = ''

    def __init__(self, name, confirmed_count, suspected_count,
                 cured_count, dead_count, dead_rate, update_date):
        self.name = name
        self.confirmed_count = confirmed_count
        self.suspected_count = suspected_count
        self.cured_count = cured_count
        self.dead_count = dead_count
        self.dead_rate = dead_rate
        self.update_date = update_date

    def write_csv_confirmed_count_file(self, file):
        line = self.name + "," + "累计确诊" + "," + str(self.confirmed_count) + "," + self.update_date
        logging.debug(line)
        file.write(line + '\n')
        file.flush()

    def write_csv_suspected_count_file(self, file):
        line = self.name + "," + "疑似病例" + "," + str(self.suspected_count) + "," + self.update_date
        logging.debug(line)
        file.write(line + '\n')
        file.flush()

    def write_csv_cured_count_file(self, file):
        line = self.name + "," + "治愈病例" + "," + str(self.cured_count) + "," + self.update_date
        logging.debug(line)
        file.write(line + '\n')
        file.flush()

    def write_csv_dead_count_file(self, file):
        line = self.name + "," + "死亡病例" + "," + str(self.dead_count) + "," + self.update_date
        logging.debug(line)
        file.write(line + '\n')
        file.flush()

    def write_csv_dead_rate_file(self, file):
        line = self.name + "," + "死亡率" + "," + str(self.dead_rate) + "," + self.update_date
        logging.debug(line)
        file.write(line + '\n')
        file.flush()
