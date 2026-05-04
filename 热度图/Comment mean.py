from pyecharts import options as opts
from pyecharts.charts import Map

data = [('北京市',25),('天津市',4),('河北省',21),('山西省',5),('内蒙古自治区',3),('辽宁省',9),('吉林省',5),('黑龙江省',15),
        ('上海市',16),('江苏省',36),('浙江省',42),('安徽省',19),('福建省',21),('江西省',17),('山东省',34),('河南省',28),
        ('湖北省',33),('湖南省',26),('广东省',71),('广西壮族自治区',16),('海南省',2),('重庆市',25),('四川省',47),('贵州省',6),
        ('云南省',9),('西藏自治区',0),('陕西省',20),('甘肃省',2),('青海省',0),('新疆维吾尔自治区',3),('台湾省',2),
        ('宁夏回族自治区',1),('澳门特别行政区',0),('香港特别行政区',0),('南海诸岛',0)]
def map_china() -> Map:
  c = (
      Map(init_opts=opts.InitOpts(width='720px', height='720px'))
    .add(series_name="评论数/条", data_pair=data, maptype="china",zoom = 1,center=[105,38])
    .set_global_opts(
      title_opts=opts.TitleOpts(title=""),
      visualmap_opts=opts.VisualMapOpts(max_=9999,is_piecewise=True,
              pieces=[{"max": 10, "min": 0, "label": "0-10","color":"#F5F5DC"},
                  {"max": 20, "min": 10, "label": "10-20", "color": "#F5DEB3"},
                  {"max": 30, "min": 20, "label": "20-30", "color": "#F4A460"},
                  {"max": 40, "min": 30, "label": "30-40","color":"#EE7942"},
                  {"max": 50, "min": 40, "label": "40-50", "color":"#D2691E"},
                  {"max": 60, "min": 50, "label": "50-60","color":"#B22222"},
                  {"max": 100, "min": 60,"label": ">=60","color":"#8B2323"}]
                       )
    )
  )
  return c
d_map = map_china()
d_map.render("地图降维-求和.html")