import re

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

if __name__ == '__main__':
	pass