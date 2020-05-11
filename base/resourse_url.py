import json
from base import file_operation, readConfig


def uesr_release_picture_list():
    url = readConfig.ReadConfig.get_http('baseurl')
    use_id = file_operation.read_file('ids.json')['uid']
    if url == 'http://lemondream.chumanapp.com':
        purl = "http://demo.lemondream.cn/"
        pic = "/image/545b73c361554230b98c89d4eeb02b77.jpg"  # demo
        pic_url = purl + 'user/' + str(use_id) + pic
        img = {"u": pic_url, "w": 500, "h": 500}
    else:
        purl = "http://qnc.lemondream.cn/"
        pic = "/image/245b41bc840a4dddb4a8fdc5eebbe31e.jpg"  # api2、api
        pic_url = purl + 'user/' + str(use_id) + pic
        img = {"u": pic_url, "w": 1042, "h": 1449}

    img_list = []
    img_list.append(img)

    return img_list


def user_third_login():
    url = readConfig.ReadConfig.get_http('baseurl')
    if url == "http://lemondream.chumanapp.com":
        openid = "AFE501C1F573379B4AE9D33BFD0784BA"
    else:
        openid = "B39DC109BE7BEA6EB958FE43244CE6CB"

    return openid

if __name__ == '__main__':
    user_third_login()
