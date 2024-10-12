'''
词云和词频
'''
import jieba
from ctext import *  # This lets us get Chinese texts from http://ctext.org
from wordcloud import WordCloud
setapikey("demo")    # This allows us access to the data used in these tutorials


text1 = gettextaschapterlist("ctp:gongyang-zhuan/yin-gong-yuan-nian") # 春秋公羊传,y
# print(len(text1),type(text1))
txt ="".join(text1)
# print("文章内容:\n{}".format(txt))

# https://www.iotword.com/25954.html
wordcloud = WordCloud(font_path="msyh.ttc",width=800,height=700).generate(txt)

wordcloud.to_file('wordcloud1.jpg')
# image = wordcloud.to_image()
# image.show()


# 词频
# words= jieba.lcut(txt) #使用精确模式对文本进行分词
# print("分词后：{}".format(words))
#
# counts = {} #通过键值对的形式存储词语及其出现的次数
#
# for word in words:
#     if len(word) == 1: #单个词语不计算在内
#         continue
#     else:
#         counts[word]= counts.get(word, 0) + 1 #遍历所有词语，每出现一次其对应的值加 1
#
# items= list(counts.items())#将键值对转换成列表
#
# items.sort(key=lambda x: x[1], reverse=True) #根据词语出现的次数进行从大到小排序
# print(items)
# print(len(items))
#
# for i in range(len(items)):
#     word, count= items[i]
#     print("{0:<5}{1:>5}".format(word, count))





