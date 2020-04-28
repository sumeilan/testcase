import json
from base import file_operation,readConfig


# "img_list": "[{\"u\":\"http:\/\/lemondream.chumanapp.com\/user\/1042\/image\/4b3e4bd0835f4158bb252dd818a20210.jpg\",\"w\":500,\"h\":500}]",

def uesr_release_picture_list():
    url = readConfig.ReadConfig.get_http('baseurl')
    use_id = file_operation.read_file('ids.json')['uid']
    pic = "/image/4b3e4bd0835f4158bb252dd818a20210.jpg"   #demo
    pic_url = url +'/' +str(use_id) + pic
    img = [{"u": pic_url, "w": 500, "h": 500}]
    img_str = json.dumps(img)
    img_list = img_str.replace('\"', '\\"')
    # print(img)
    # print(repr(img))
    # print(img_list)

    return img_list

if __name__ == '__main__':
    uesr_release_picture_list()

