def chart(list_x_name, list_y_data):
    from pyecharts import options as opts
    from pyecharts.charts import Bar

    for i in list_y_data:
        if len(i) != len(list_x_name):
            return '数据不全'
    bar = (
        Bar(
            # 设置生成图表大小
            init_opts=opts.InitOpts(width='1000px', height='700px'))

            # x轴数据
            .add_xaxis(list_x_name)
            #  指标 以及y轴数据
            .add_yaxis('销售额', list_y_data[0])
            .add_yaxis('可提佣销售额', list_y_data[1])
            .set_colors(["blue", "red"])  # 柱子的颜色

            .set_global_opts(
            # 标题设置
            # legend_opts=opts.LegendOpts(type_="scroll", pos_left="left", orient="vertical"),
            title_opts=opts.TitleOpts(title='运营部销售额',
                                      subtitle='020120902038',
                                      # 标题文字格式
                                      title_textstyle_opts=opts.TextStyleOpts(color='red',
                                                                              font_size=19,
                                                                              font_family='Times New Roman',
                                                                              font_weight='bold'),
                                      # 副标题文字格式
                                      subtitle_textstyle_opts=opts.TextStyleOpts(color='blue',
                                                                                 font_size=12,
                                                                                 font_family='Times New Roman',
                                                                                 font_weight='bold')

                                      ),
            # 显示工具箱
            toolbox_opts=opts.ToolboxOpts(is_show=True)
        )

    )

    bar.render('D:\\重置路径\\ceshi.html')


if __name__ == '__main__':
    list1 = ['运营1', '运营2', '运营3', '运营4', '运营5', 'qqqq', 'wwwww', 'qqqqqqqq', 'dsfvcv', 'cedcervervc', 'recevrecscedce'
        , 'frwececedr', 'recerdc', 'recerv', 'scsdcsdc']
    list3 = [[4, 5, 6, 7, 8, 4, 5, 6, 7, 8, 4, 5, 6, 7, 8], [7, 8, 9, 10, 11, 4, 5, 6, 7, 8, 4, 5, 6, 7, 8]]
    a = chart(list1, list3)

print(a)
