import grequests


request_list = [
    grequests.get('http://httpbin.org/delay/1', timeout=0.001),
    grequests.get('http://fakedomain/'),
    grequests.get('http://httpbin.org/status/500')
]


# ##### 执行并获取响应列表 #####
# response_list = grequests.map(request_list)
# print(response_list)


##### 执行并获取响应列表（处理异常） #####
def exception_handler(request, exception):
    print(request,exception)
    print("Request failed")

response_list = grequests.map(request_list, exception_handler=exception_handler)
print(response_list)



