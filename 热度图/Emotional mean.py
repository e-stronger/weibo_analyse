from pyecharts import options as opts
from pyecharts.charts import Map
data = [('北京市',0.1593),('天津市',0.5706),('河北省',0.2626),
        ('山西省',0.3461),('内蒙古自治区',0.0680),('辽宁省',0.2538),
        ('吉林省',0.2060),('黑龙江省',0.1291),
        ('上海市',0.2646),('江苏省',0.2991),
        ('浙江省',0.2745),('安徽省',0.2389),('福建省',0.2200),
        ('江西省',0.2498),('山东省',0.3044),('河南省',0.1467),
        ('湖北省',0.1728),('湖南省',0.2535),('广东省',0.2401),
        ('广西壮族自治区',0.3087),('海南省',0.3912),('重庆市',0.2232),
        ('四川省',0.3601),('贵州省',0.4336),
        ('云南省',0.1567),('西藏自治区',0),
        ('陕西省',0.1748),('甘肃省',0.2952),('青海省',0),
        ('新疆维吾尔自治区',0.2286),('台湾省',0.1740),
        ('宁夏回族自治区',0.0002),('澳门特别行政区',0),('香港特别行政区',0),('南海诸岛',0)]
def map_china() -> Map:
  c = (
    Map(init_opts=opts.InitOpts(width='720px', height='720px'))
    .add(series_name="情感均值", data_pair=data, maptype="china",zoom = 1,center=[105,38])
    .set_global_opts(
      title_opts=opts.TitleOpts(title=""),
      visualmap_opts=opts.VisualMapOpts(max_=9999,is_piecewise=True,
              pieces=[
                  {"max": 0.1, "min": 0, "label": "0-0.1", "color": "#F5F5DC"},
                  {"max": 0.2, "min": 0.1, "label": "0.1-0.2", "color": "#F5DEB3"},
                  {"max": 0.3, "min": 0.2, "label": "0.2-0.3","color":"#F4A460"},
                  {"max": 0.4, "min": 0.3, "label": "0.3-0.4", "color":"#D2691E"},
                  {"max": 0.5, "min": 0.4, "label": "0.4-0.5","color":"#B22222"},
                  {"max": 0.6, "min": 0.5, "label": "0.5-0.6","color":"#8B2323"}]
                       )
    )
  )
  return c
d_map = map_china()
d_map.render("地图情感均值.html")