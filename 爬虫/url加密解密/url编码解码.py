
# import base64
#
# s = 'http%3A%2F%2Fv3.zhiguoer.com%3A8091%2F20180627%2FOb6kyHDi%2Findex.m3u8'
#
# a = base64.urlsafe_b64decode(s)
#
# print(a)
# from urllib.parse import quote, unquote, urlencode
#
# s = 'http://v3.zhiguoer.com:8091/20180627/Ob6kyHDi/index.m3u8'
#
# a = unquote(s)
#
# print(a)

from urllib.parse import quote, unquote, urlencode


def main():
    my_data = '好好学习'

    # url编码
    encode_data = quote(my_data)
    print("encode_data : %s " % encode_data)
    # url解码
    decode_data = unquote(encode_data)
    print("decode_data : %s " % decode_data)

    my_query = {'conent': '天天向上'}
    # url参数编码
    encode_query = urlencode(my_query)
    print("encode_query : %s " % encode_query)
    # url参数解码
    decode_query = unquote(encode_query)
    print("decode_query : %s " % decode_query)
    encode_url = 'http://127.0.0.1?'+encode_query # 加上参数编码后完整的url
    # url解码
    decode_url = unquote(encode_url)
    print("decode_url : %s " % decode_url)


if __name__ == '__main__':
    main()


