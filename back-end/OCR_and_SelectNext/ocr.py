import base64
import urllib
import requests
import json

def ocr(file_path):
    """
    送入图片路径，返回识别出来的文字
    """
    url = "https://aip.baidubce.com/rest/2.0/ocr/v1/handwriting?access_token=" + get_access_token()

    # image 可以通过 get_file_content_as_base64("C:\fakepath\鲍.png",True) 方法获取
    payload = f'image={get_file_content_as_base64(file_path, True)}'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    # print(response.text)
    words = json.loads(response.text)['words_result']
    if len(words) > 0:
        char = words[0]['words'][0]
        # print(f'OCR success! words: {char[0]}')
    else:
        # print(f'OCR fail! words: \'\'')
        char = ''
    return char


def get_file_content_as_base64(path, urlencoded=False):
    """
    获取文件base64编码
    :param path: 文件路径
    :param urlencoded: 是否对结果进行urlencoded 
    :return: base64编码信息
    """
    with open(path, "rb") as f:
        content = base64.b64encode(f.read()).decode("utf8")
        if urlencoded:
            content = urllib.parse.quote_plus(content)
    return content


def get_access_token():
    """
    使用 AK，SK 生成鉴权签名（Access Token）
    :return: access_token，或是None(如果错误)
    """
    url = "https://aip.baidubce.com/oauth/2.0/token"
    API_KEY = "SuEcUP8cnkMH5ao1kVLjtm3w"
    SECRET_KEY = "N5laF0EBPGd6BUgXLo21GDp9ElFNHfUr"
    params = {"grant_type": "client_credentials", "client_id": API_KEY, "client_secret": SECRET_KEY}
    return str(requests.post(url, params=params).json().get("access_token"))


# if __name__ == '__main__':
#     file_path = '/root/autodl-tmp/tempfile_pathset/腑.png'
#     ocr(file_path)
