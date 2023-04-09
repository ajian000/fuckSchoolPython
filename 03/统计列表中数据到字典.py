#导入Counter用于列表数据统计
from collections import Counter

names = ['Li','Zhang','Wang','Zhang','Li','Wang','Li','Wang','Wang']
#实例化一个Counter对象
c = Counter(names)
#转换为字典
result  = {"Li":c["Li"],"Zhang":c["Zhang"],"Wang":c["Wang"]}
#输出结果
print(result)