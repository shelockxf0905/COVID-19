"""
@ProjectName: Covid-2019
@FileName: main.py
@Author: xiao-yi.yu
@Date: 2020/04/04
"""
from service.crawler import Crawler
from datetime import date
import requests

import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Bar, Page, Pie, Timeline, Grid, Line


def timeline_bar() -> Timeline:
    x = ['国内', '国外']
    tl = Timeline()
    tl.add_schema(is_auto_play=True,
                  play_interval=5000,
                  is_loop_play=True)
    k = 0

    for j in date:
        bar = (
            Line()
            .add_xaxis(date)
            .add_yaxis("国内", hs(c1, k))
            .add_yaxis("国外", hs(c, k))
            .extend_axis(
                yaxis=opts.AxisOpts()
            ).set_series_opts(
                areastyle_opts=opts.AreaStyleOpts(opacity=0.5),
                label_opts=opts.LabelOpts(is_show=False)
            ).set_global_opts(title_opts=opts.TitleOpts("{}国内外疫情趋势".format(j))))

        k = k + 1
    return tl


def main():
    """
        主函数
    """
    # 全部の歴史データを取得
    data = requests.get('https://lab.isaaclin.cn/nCoV/api/area?latest=0')
    data = data.json()

    print("一共有{0}条记录。", len(data['results']))
    res = data['results']
    df = pd.DataFrame(res)

    for i in range(len(df)):
        df.iloc[i, 16] = time_c(df["updateTime"][0])

    for i in range(len(df)):
        df.iloc[i, 16] = df.iloc[i, 16][5:10]

        # 去重部分代码
        tem = df[df['updateTime'] == '03-02']
        tem = tem.drop_duplicates(['provinceShortName'], keep='last')
        for i in date[1:41]:
            tem1 = df[df['updateTime'] == i]
            tem1 = tem1.drop_duplicates(['provinceName'], keep='last')
            tem = tem.append(tem1)

        tem = tem.reset_index(drop=True)
    timeline_bar().render_notebook()


if __name__ == '__main__':
    crawler = Crawler()
    main()
    # crawler.run()
