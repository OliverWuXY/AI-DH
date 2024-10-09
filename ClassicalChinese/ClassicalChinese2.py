'''
两个例子
'''
from ctext import *  # This lets us get Chinese texts from http://ctext.org
setapikey("demo")    # This allows us access to the data used in these tutorials

## 例1：找出最长的段
# paragraphs = gettextasparagrapharray("ctp:analects/ji-shi") #季氏
#
# print("This chapter is made up of " + str(len(paragraphs)) + " paragraphs. These are:")
#
# # For each paragraph of the chapter data that we downloaded, do the following:
# for paragraphnumber in range(0, len(paragraphs)):
#     print(str(paragraphnumber+1) + ". " + paragraphs[paragraphnumber])
#
# longest_paragraph = None # We use this variable to record which of the paragraphs we've looked at is longest
# longest_length = 0       # We use this one to record how long the longest paragraph we've found so far is
#
# for paragraph_number in range(0, len(paragraphs)):
#     paragraph_text = paragraphs[paragraph_number];
#     if len(paragraph_text)>longest_length:
#         longest_paragraph = paragraph_number
#         longest_length = len(paragraph_text)
#
# print("The longest paragraph is paragraph number " + str(longest_paragraph+1) + ", which is " + str(longest_length) + " characters long.")

# 例2：绘制 “矣 ”和 “也 ”这两个字在《论语》章节和《封神演义》章节中的出现频率
import re
import pandas as pd
import matplotlib.pyplot as plt
# %matplotlib inline

def makevector(string, termlist, normalize = False):
    vector = []
    for term in termlist:
        termcount = len(re.findall(term, string))
        if normalize:
            vector.append(termcount/len(string))
        else:
            vector.append(termcount)
    return vector

text1 = gettextaschapterlist("ctp:fengshen-yanyi") # 封神演義
text2 = gettextaschapterlist("ctp:analects") #论语

vectors1 = []
for chapter in text1:
    vectors1.append(makevector(chapter, ["矣", "也"], True))

vectors2 = []
for chapter in text2:
    vectors2.append(makevector(chapter, ["矣", "也"], True))

df1 = pd.DataFrame(vectors1)
df2 = pd.DataFrame(vectors2)

legend1 = plt.scatter(df1.iloc[:,0], df1.iloc[:,1], color="blue", label="Fengshen Yanyi")
legend2 = plt.scatter(df2.iloc[:,0], df2.iloc[:,1], color="red", label="Analects")
plt.legend(handles = [legend1, legend2])
plt.xlabel("Frequency of 'yi'")
plt.ylabel("Frequency of 'ye'")
plt.show()