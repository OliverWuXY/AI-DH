import jieba
# jieba中的paddle模式
# https://blog.csdn.net/nkufang/article/details/129788741
import paddle

paddle.enable_static()
jieba.enable_paddle()# 启动paddle模式。 0.40版之后开始支持，早期版本不支持
strs=["我来到北京师范大学","刀郎的门票卖完了","北京师范大学珠海校区", "清滕天绶纂修天绶辽阳人荫生由广东潮州府同知升汉中府知府"]
for str in strs:
    seg_list = jieba.cut(str,use_paddle=True) # 使用paddle模式
    print("Paddle Mode: " + '/'.join(list(seg_list)))

seg_list = jieba.cut("我来到北京师范大学", cut_all=True)
print("Full Mode: " + "/ ".join(seg_list))  # 全模式

seg_list = jieba.cut("我来到北京师范大学", cut_all=False)
print("Default Mode: " + "/ ".join(seg_list))  # 精确模式

seg_list = jieba.cut("我来到北京师范大学")  # 默认是精确模式
print(", ".join(seg_list))

seg_list = jieba.cut_for_search("小明硕士毕业于北京师范大学文理学院，后在剑桥大学深造")  # 搜索引擎模式
print(", ".join(seg_list))