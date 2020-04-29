import json
from base import file_operation,readConfig

def uesr_release_picture_list():
    url = readConfig.ReadConfig.get_http('baseurl')
    use_id = file_operation.read_file('ids.json')['uid']
    if url == 'http://lemondream.chumanapp.com':
        purl = "http://demo.lemondream.cn/"
        pic = "/image/545b73c361554230b98c89d4eeb02b77.jpg"  # demo
        pic_url = purl + 'user/'+  str(use_id) + pic
        img = {"u": pic_url, "w": 500, "h": 500}
    else:
        purl = "http://qnc.lemondream.cn/"
        pic = "/image/245b41bc840a4dddb4a8fdc5eebbe31e.jpg" #api2、api
        pic_url = purl +  'user/'+ str(use_id) + pic
        img = {"u": pic_url, "w": 1042, "h": 1449}

    # img_str = json.dumps(img)
    img_list = []
    img_list.append(img)
    print(pic)

    return img_list

if __name__ == '__main__':
    uesr_release_picture_list()

