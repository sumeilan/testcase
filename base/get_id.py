import re,requests

def get_comic_id(datas):
    comic_pattern = r'\'type\': \'4\', \'obj_id\': \'\d+\''  # 模式字符串
    match = re.findall(comic_pattern, str(datas), re.I)  # 匹配字符串不区分大小
    if match:
        data = '{' + str(match[0]) + '}'
        comic_obj = eval(data)
        return comic_obj['obj_id']

def get_adventure_id(datas):
    comic_pattern = r'\'type\': \'2\', \'obj_id\': \'[0-9_]+\''  # 模式字符串
    match = re.findall(comic_pattern, str(datas), re.I)  # 匹配字符串不区分大小
    if match:
        data = '{' + str(match[0]) + '}'
        adv_obj = eval(data)
        return adv_obj['obj_id']

def get_external_picture_id(datas):
    for data in datas:
        type_pattern = r'\'type\': \'9\''  # 模式字符串
        id_pattern = r'\'obj_id\': \'\d+\''
        type_match = re.findall(type_pattern, str(data), re.I)  # 匹配字符串不区分大小
        id_match = re.findall(id_pattern, str(data), re.I)
        if type_match:
            data = '{' + str(id_match[0]) + '}'
            obj_id = eval(data)
            return obj_id['obj_id']

def get_external_video_id(datas):
    for data in datas:
        type_pattern = r'\'type\': \'10\''  # 模式字符串
        id_pattern = r'\'obj_id\': \'\d+\''
        type_match = re.findall(type_pattern, str(data), re.I)  # 匹配字符串不区分大小
        id_match = re.findall(id_pattern, str(data), re.I)
        if type_match:
            data = '{' + str(id_match[0]) + '}'
            obj_id = eval(data)
            return obj_id['obj_id']


if __name__ == '__main__':
    url = 'http://lemondream.chumanapp.com/api/recommend/get_recommend_content_list'
    data  = [{'obj_id': '1579118817004111', 'title': None, 'content': '蓝家人酒量真差', 'like_num': 1858, 'has_like': 0, 'tags': '',
      'author_id': 6, 'type': '9'},
     {'obj_id': '1579077610004767', 'title': None, 'content': '我以为你不要我了，', 'like_num': 1639, 'type': '10'}]
    p = get_external_picture_id(data)
    print('p',p)
    v = get_external_video_id(data)
    print('v',v)