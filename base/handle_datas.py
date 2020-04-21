from base import file_operation,HmacSHA256,readConfig
from operation_data  import get_data
import time,json

class handleDatas:
    def __init__(self):
        self.datas = get_data.getData(0)

    #获取接口依赖的字段
    def get_request_depend_data(self,index):
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
            return depend_data
        else:
            return None

    # 获取接口请求的参数
    def get_request_parameter(self,index):
        depend_data = handleDatas.get_request_depend_data(self,index)
        if depend_data:
            if ('timestamp' in depend_data.keys()):
                timestamp = depend_data['timestamp']
            if ('access_token' in depend_data.keys()):
                access_token = depend_data['access_token']

        if len(self.datas.get_request_parameter(index)) == 0:
            body = {'': ''}
        else:
            body = eval(self.datas.get_request_parameter(index))
        return body

    def get_request_headers(self,index,body):
        Authorization = HmacSHA256.sh258(json.dumps(body))  # 请求头需要Authorization
        biData = str(file_operation.read_file('biD.json'))
        XToken = file_operation.read_file('token.json')['X-Token']
        versionCode = readConfig.ReadConfig.get_http('versionCode')
        headers = eval(self.datas.get_request_headers(index))
        return headers

    def get_data_from_response(self,index,datas):
        if self.datas.get_data_from_response(index) is not None:
            response_data = self.datas.get_data_from_response(index)
            if datas[response_data]:
                XToken = {'X-Token': datas[response_data]}
                file_operation.zhui_write_file(XToken, 'token.json')
            return response_data
        else:
            return None

if __name__ == '__main__':
    # dd = getRequestData().get_request_depend_data(1)
    # getRequestData().get_request_parameter(2)
    datas = {'data': {'guest_id': '4b594c5b034a'}}
    print(handleDatas().get_data_from_response(1,datas))



