from base import file_operation, HmacSHA256, readConfig, get_id
from operation_data import get_data
import time, json


class handleDatas:
    def __init__(self, sheet_id=None):
        self.datas = get_data.getData(sheet_id)

    # 获取接口依赖的字段
    def get_request_depend_data(self, index):
        depend_data = {}

        if self.datas.get_request_depend_data(index) is not None:
            dd = self.datas.get_request_depend_data(index)
            for i in dd.split(","):
                if i == 'timestamp':
                    timestamp = int(round(time.time() * 1000))
                    depend_data['timestamp'] = timestamp
                if i == 'access_token':
                    access_token = file_operation.read_file('token.json')['access_token']  # 请求的body需要token
                    depend_data['access_token'] = access_token
                if i == 'uid':
                    uid = file_operation.read_file('ids.json')['uid']
                    depend_data['uid'] = uid
                if i == 'release_picture_id':
                    release_picture_id = file_operation.read_file('ids.json')['release_picture_id']
                    depend_data['release_picture_id'] = release_picture_id
                if i == 'release_video_id':
                    release_video_id = file_operation.read_file('ids.json')['release_video_id']
                    depend_data['release_video_id'] = release_video_id
                if i == 'external_picture_id':
                    external_picture_id = file_operation.read_file('ids.json')['external_picture_id']
                    depend_data['external_picture_id'] = external_picture_id
                if i == 'external_video_id':
                    external_video_id = file_operation.read_file('ids.json')['external_video_id']
                    depend_data['external_video_id'] = external_video_id
                if i == 'trace_release_pid':
                    trace_release_pid = file_operation.read_file('ids.json')['trace_release_pid']
                    depend_data['trace_release_pid'] = trace_release_pid
                if i == 'trace_release_vid':
                    trace_release_vid = file_operation.read_file('ids.json')['trace_release_vid']
                    depend_data['trace_release_vid'] = trace_release_vid
            # print('获取接口依赖的字段', self.datas.get_request_depend_data(index),depend_data)
            return depend_data
        else:
            return None

    # 获取接口请求的参数
    def get_request_parameter(self, index):
        depend_data = handleDatas.get_request_depend_data(self, index)
        if depend_data:
            if ('timestamp' in depend_data.keys()):
                timestamp = depend_data['timestamp']
            if ('access_token' in depend_data.keys()):
                access_token = depend_data['access_token']
            if ('uid' in depend_data.keys()):
                uid = depend_data['uid']
            if ('release_picture_id' in depend_data.keys()):
                release_picture_id = depend_data['release_picture_id']
            if ('release_video_id' in depend_data.keys()):
                release_video_id = depend_data['release_video_id']
            if ('external_picture_id' in depend_data.keys()):
                external_picture_id = depend_data['external_picture_id']
            if ('external_video_id' in depend_data.keys()):
                external_video_id = depend_data['external_video_id']
            if ('trace_release_pid' in depend_data.keys()):
                trace_release_pid = depend_data['trace_release_pid']
            if ('trace_release_vid' in depend_data.keys()):
                trace_release_vid = depend_data['trace_release_vid']

        if len(self.datas.get_request_parameter(index)) == 0:
            body = {'': ''}
        else:
            body = eval(self.datas.get_request_parameter(index))
        return body

    # hearder参数
    def get_request_headers(self, index, body):
        Authorization = HmacSHA256.sh258(json.dumps(body))  # 请求头需要Authorization
        biData = str(file_operation.read_file('biD.json'))
        XToken = file_operation.read_file('token.json')['X-Token']
        versionCode = readConfig.ReadConfig.get_http('versionCode')
        accessToken = file_operation.read_file('token.json')['access_token']

        headers = eval(self.datas.get_request_headers(index))

        return headers

    # 需要请返回数据中保存字段
    def get_data_from_response(self, index, datas):
        response_data = self.datas.get_data_from_response(index)

        if response_data is not None:
            if response_data == 'guest_id':
                if datas['data'][response_data]:
                    XToken = {'X-Token': datas['data'][response_data]}
                    file_operation.zhui_write_file(XToken, 'token.json')
                return response_data
            if response_data == 'access_token':
                if datas['data'][response_data]:
                    access_token = {'access_token': datas['data'][response_data]}
                    file_operation.zhui_write_file(access_token, 'token.json')
                return response_data
            if response_data == 'id':
                if datas['data'][response_data]:
                    uid = {'uid': datas['data'][response_data]}
                    file_operation.zhui_write_file(uid, 'ids.json')
                return response_data
            # 爬虫作品id
            if response_data == 'obj_id':
                if get_id.get_external_picture_id(datas['list']):
                    external_picture_id = {'external_picture_id': get_id.get_external_picture_id(datas['list'])}
                    file_operation.zhui_write_file(external_picture_id, 'ids.json')
                if get_id.get_external_video_id(datas['list']):
                    external_video_id = {'external_video_id': get_id.get_external_video_id(datas['list'])}
                    file_operation.zhui_write_file(external_video_id, 'ids.json')
            # 用户发布的作品id
            if response_data == 'release_id':
                if get_id.get_release_picture_id(datas):
                    release_picture_id = {'release_picture_id': get_id.get_release_picture_id(datas)}
                    file_operation.zhui_write_file(release_picture_id, 'ids.json')
                if get_id.get_release_video_id(datas):
                    release_video_id = {'release_video_id': get_id.get_release_video_id(datas)}
                    file_operation.zhui_write_file(release_video_id, 'ids.json')
            if response_data == 'trace_release_id':
                if get_id.get_release_picture_id(datas):
                    trace_release_pid = {'trace_release_pid': get_id.get_release_picture_id(datas)}
                    print('trace_release_pid', trace_release_pid)
                    file_operation.zhui_write_file(trace_release_pid, 'ids.json')
                if get_id.get_release_video_id(datas):
                    trace_release_vid = {'trace_release_vid': get_id.get_release_video_id(datas)}
                    print('trace_release_vid', trace_release_vid)
                    file_operation.zhui_write_file(trace_release_vid, 'ids.json')

        else:
            return None


if __name__ == '__main__':
    dd = handleDatas(4).get_request_depend_data(6)
    # getRequestData().get_request_parameter(2)
    # datas = {'data': {'guest_id': '4b594c5b034a'}}
    # print(handleDatas().get_data_from_response(1,datas))
