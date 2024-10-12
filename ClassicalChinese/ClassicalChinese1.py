'''
了解ctext库的API
'''
from ctext import *  # This lets us get Chinese texts from http://ctext.org
setapikey("demo")    # This allows us access to the data used in these tutorials

# CTP URNs
# ctp:analects/li-ren    https://ctext.org/analects/li-ren
# ctp:ws832238           https://ctext.org/wiki.pl?if=en&chapter=832238

# analects 论语 ，mengzi 孟子


# titles = gettexttitles()
# print(titles)#所有书 json格式，{{'books': [{'title': '考信編', 'urn': 'ctp:wb7754238'},...]}
# print(str(titles)[0:200])
# # # 思考如知道一共有多少本书？？ json格式是否可以转成表格式格式呢？

# capabilities = getcapabilities()
# print(capabilities)
# {'functions':
# {'getcapabilities': {'description': 'Returns a list of available API functions and list of their parameters.', 'params': {}},
# 'getcharacter': {'description': 'Returns basic data about a character.', 'params': {'char': {'description': 'Character to describe.', 'example': '仁', 'required': 1}}},
# 'getdictionaryheadwords': {'description': 'Returns a complete list of headwords for distinct word senses, names, and places having entries in the CTP dictionary.', 'params': {}},
# 'getdynasties': {'description': 'Returns a list of identifiers, labels, and dates for dynasties used in the Chinese Text Project.', 'params': {}},
# 'getlink': {'description': 'Returns a http://ctext.org URL corresponding to a URN, or alternatively redirects a web browser to that URL if the "redirect" parameter is set to 1. The returned URL does not point to an API function but to a page on http://ctext.org which should be opened directly in a web browser and not fetched by an API client.', 'params': {'redirect': {'description': 'If set to 1, do not return a JSON response, but instead return an HTTP 30x response redirecting to the specified page.'},
#     'search': {'description': "Link to human-readable search results for the phrase 'search' within the specified URN.", 'example': '朋'},
#     'urn': {'description': 'URN specifying the text to return a link to.', 'example': 'ctp:analects/xue-er', 'required': 1}}},
# 'getstats': {'description': 'Machine-readable interface to data available at http://ctext.org/system-statistics', 'params': {}},
# 'getstatus': {'description': 'Returns the status of the current client-server relationship (e.g. whether a user is logged in).', 'params': {}},
# 'gettext': {'description': 'Returns the textual content of a chapter of text.', 'params': {'urn': {'description': 'URN specifying the text to return.', 'example': 'ctp:analects/xue-er', 'required': 1}}},
# 'gettextinfo': {'description': 'Returns metadata about a textual object.', 'params': {'urn': {'description': 'URN specifying the text to describe.', 'example': 'ctp:analects/xue-er', 'required': 1}}},
# 'gettexttitles': {'description': 'Returns a complete list of top-level textual items (typically books) in the textual database and Wiki.', 'params': {}}, 'readlink': {'description': 'Returns a URN corresponding to a http://ctext.org URL.', 'params': {'url': {'description': 'URL specifying a text on http://ctext.org.', 'example': 'http://ctext.org/analects/xue-er/zhs', 'required': 1}}},
# 'searchtexts': {'description': 'Returns a list of items in the textual database and Wiki matching specified parameters.', 'params': {'title': {'description': 'Part or all of the text title.', 'example': '論語', 'required': 1}}}},
# 'globalparams': {
#     'apikey': {'description': 'Optional API key to authenticate an application to the API.'},
#     'if': {'description': "Interface preference. If present, the value of this parameter must be either 'en' (English) or 'zh' (Chinese).", 'example': 'zh'},
#     'remap': {'description': "Remap characters in response. If present, the value of this parameter must be 'gb' (simplified Chinese).", 'example': 'gb'}},
#  'version': '0.9'}
#  格式化json  https://www.sojson.com/

# data = gettextinfo("ctp:analects")
# print(data) #json格式

# data = gettextasobject("ctp:analects")
# print(data) #json格式
#
# string = gettextasstring("ctp:analects/xue-er")
# print(string) #文本格式

# chapters = gettextaschapterlist("ctp:analects")
# print("Total number of chapters: " + str(len(chapters)))
# print("First chapters is: " + chapters[0])
# print("Second chapters is: " + chapters[1])
# print("Last chapters is: " + chapters[-1])
#
passages = gettextasparagrapharray("ctp:analects")  # 论语
print("Total number of passages: " + str(len(passages)))
print("First passage is: " + passages[0])
print("Second passage is: " + passages[1])
print("Last passage is: " + passages[-1])


# passages = gettextasparagrapharray("ctp:mengzi")  # 孟子
#
# print("Total number of passages: " + str(len(passages)))
# print("First passage is: " + passages[0])
# print("Second passage is: " + passages[1])
# print("Last passage is: " + passages[-1])