import argparse  # from std
import urllib.request  # from std
from bs4 import BeautifulSoup  # from pypi


def Retrive(input_file_path):
    with open(input_file_path, 'r', encoding='UTF-8') as file:
        for url in file:
            print(url)
            # 開啟網頁
            response = urllib.request.urlopen(url)
            # 解析網頁
            soup = BeautifulSoup(response, features="html.parser")
            # 列印網頁標題
            print(soup.title.string)


def main():

    # 準備參數解析
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file_path", help="包含連結網址之文字檔案，各網址獨立一行",
                        type=str, )
    args = parser.parse_args()

    # 執行函數
    ans = add(args.input_file_path)
    print(ans)


if __name__ == "__main__":
    main()
