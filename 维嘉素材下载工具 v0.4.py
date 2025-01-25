import requests
import os

url = "https://sfile.chatglm.cn/api/cogvideo/fd4a2e20-da16-11ef-bc47-f2de561fe732_0.mp4"
url2 = "https://sfile.chatglm.cn/api/cogvideo/32c37644-da38-11ef-be56-1a5b66680e03_0.mp4"
url_jpg = "https://static.wikia.nocookie.net/carambola1437warehouse/images/e/eb/Weijia.jpg/revision/latest?cb=""20240921130335&path-prefix=zh"
local_filename = "维嘉素材\维嘉ai生成视频.mp4"
local_filename2 = "维嘉素材\维嘉ai生成视频2.mp4"
local_filename3 = "维嘉素材\维嘉素材.jpg"

def download_file(url, local_filename):
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    return local_filename

language = input("Please select a language:\n  1.Chinese\n  2.English\nInput: ")

if language == "1":
    languages = ["你要下载的文件是：\n1.维嘉ai生成视频.mp4\n2.维嘉ai生成视频2.mp4\n3.维嘉素材.jpg\nInput: "]
else:
    languages = ["You are downloading: \n1.维嘉ai生成视频.mp4\n2.维嘉ai生成视频2.mp4\n3.维嘉素材.jpg\nInput: "]

if(not os.path.exists("维嘉素材")):
    os.mkdir("维嘉素材")


while True:
    inputTest = int(input(languages[0]))
    if(inputTest == 1):
        print(f"{download_file(url, local_filename)}下载完成")
    elif(inputTest == 2):
        print(f"{download_file(url2, local_filename2)}下载完成")
    elif(inputTest == 3):
        print(f"{download_file(url_jpg, local_filename3)}下载完成")
    else:
        break
print("感谢使用")
os.startfile("维嘉素材")
