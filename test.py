from pyecharts.charts import Bar
from pyecharts import options as opts

# 示例数据
cate = ['Apple', 'Huawei', 'Xiaomi', 'Oppo', 'Vivo', 'Meizu']
data1 = [123, 153, 89, 107, 98, 23]
data2 = [56, 77, 93, 68, 45, 67]


def main():
    """
        主函数
    """
    bar = (Bar()
           .add_xaxis(cate)
           .add_yaxis('电商渠道', data1)
           .add_yaxis('门店', data2)
           .set_global_opts(title_opts=opts.TitleOpts(title="XY轴翻转-基本示例", subtitle="我是副标题"))
           .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
           .reversal_axis()
          )

    bar.render_notebook()


if __name__ == '__main__':
    main()