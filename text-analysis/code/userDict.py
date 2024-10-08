'''
用户字典，地名
'''
placenames = []
with open('../data/placenames.txt', 'r', encoding='utf-8') as f:
    txt = f.read()

placenames = txt.split('\n')
print('用户地名库收录了{}个地名'.format(len(placenames)))

def is_placename(placename):
    '''
    判断是否是地名
    :param placename:
    :return:
    '''
    if placename in placenames:
        return True
    else:
        return False




'''
提取地方名
'''
import jieba
jieba.load_userdict("../data/placenames.txt") # 用户字典
# 解决jieba分词 load_userdict 加载自定义词库太慢的问题 https://blog.csdn.net/qq_29202513/article/details/85236995
text = "清趙世震修，汪澤延纂。世震遼東人，康熙間漢陰知縣。澤延漢陰縣人，貢生。考漢陰縣志創於成化十六年知縣張大綸，萬歷四十七年知縣張啟蒙，崇禎十五年知縣張鵬翱，皆有重修。此志為續崇禎十五年後之事而重纂，其志總分輿地、建置、田賦、官師、人物、藝文六門，子目凡三十一，附目七，體例尚為簡核。按輿地沿革謂：「漢陰為漢時安陽縣地，晉改曰安康；北魏改寧都，隋複改安康，唐始名漢陰。」所敘沿革，徵引傍考，不著出處，殊難使信。卷前有八景，首列鳳山疊翠，鳳山即鳳凰山，在縣南若列屏然；東西綿亙二百餘里，宛有鳳翔千仞之勢。輿地山川謂，鳳凰山在縣南二十五里，有峰如鳳因名；山頂有鳳凰池、仙女池。藝文志載陳典《鳳凰山紀》，稱此山上有萬仞芙蓉，朵朵活潑，直逼青天；下有漢水紆迥，淙淙泉石。茲觀此志八景鳳山之圖，及陳典形容之辭，則鳳凰山果不愧為漢陰之名勝也。"
words = [item for item in jieba.cut(text)]
places = [p for p in words if is_placename(p)]
print(places)
setPlaces = set(places)
print(setPlaces)