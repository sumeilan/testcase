import re,requests

def get_comic_id(datas):
    comic_pattern = r'\'type\': \'4\', \'obj_id\': \'\d+\''  # 模式字符串
    match = re.findall(comic_pattern, str(datas), re.I)  # 匹配字符串不区分大小
    if len(match)>0 :
        data = '{' + str(match[0]) + '}'
        comic_obj = eval(data)
        return comic_obj['obj_id']

def get_adventure_id(datas):
    comic_pattern = r'\'type\': \'2\', \'obj_id\': \'[0-9_]+\''  # 模式字符串
    match = re.findall(comic_pattern, str(datas), re.I)  # 匹配字符串不区分大小
    if len(match):
        data = '{' + str(match[0]) + '}'
        adv_obj = eval(data)
        return adv_obj['obj_id']

def get_external_picture_id(datas):
    for data in datas:
        type_pattern = r'\'type\': \'9\''  # 模式字符串
        id_pattern = r'\'obj_id\': \'\d+\''
        type_match = re.findall(type_pattern, str(data), re.I)  # 匹配字符串不区分大小
        id_match = re.findall(id_pattern, str(data), re.I)
        if len(id_match)>0 :
            data = '{' + str(id_match[0]) + '}'
            obj_id = eval(data)
            return obj_id['obj_id']

def get_external_video_id(datas):
    for data in datas:
        type_pattern = r'\'type\': \'10\''  # 模式字符串
        id_pattern = r'\'obj_id\': \'\d+\''
        type_match = re.findall(type_pattern, str(data), re.I)  # 匹配字符串不区分大小
        id_match = re.findall(id_pattern, str(data), re.I)
        if len(id_match)>0 :
            data = '{' + str(id_match[0]) + '}'
            obj_id = eval(data)
            return obj_id['obj_id']

def get_release_id(datas):
    for data in datas:
        type_pattern = r'\'type\': 11'  # 模式字符串
        id_pattern1 = r'\'obj_id\': \d+'
        id_pattern2 = r'\'obj_id\': \'\d+\''
        type_match = re.findall(type_pattern, str(data), re.I)  # 匹配字符串不区分大小
        id_match1 = re.findall(id_pattern1, str(data), re.I)
        id_match2 = re.findall(id_pattern2, str(data), re.I)
        if len(id_match1) > 0:
            data = '{' + str(id_match1[0]) + '}'
            obj_id = eval(data)
            return obj_id['obj_id']
        if len(id_match2) > 0:
            data = '{' + str(id_match2[0]) + '}'
            obj_id = eval(data)
            return obj_id['obj_id']


if __name__ == '__main__':
    url = 'http://lemondream.chumanapp.com/api/recommend/get_recommend_content_list'
    data  = "{'obj_id': '2004185', 'title': '1587378243991', 'content': '图片2020', 'like_num': 0, 'has_like': 0, 'tags': '', 'author_id': 83, 'type': 11, 'title_image': 1111"
    r= get_release_id(data)
    print('r',r)