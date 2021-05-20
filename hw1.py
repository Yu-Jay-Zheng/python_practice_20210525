# Author: Eugene
# https://sites.google.com/view/smartrobot/lab

# 題目說明:
# 1. 完成函數replace_filename_extension，變更參數images_path內所有檔案的副檔名，新的副檔名定義在參數new_extension。
# 2. 參數images_path: 可接受list和tuple兩種資料型別，參數images_path儲存完整的檔案路徑，檔案數目可能是零個或多個。
# 3. 參數new_extension: 新的副檔名，可能是任何合法的副檔名。
# 4. 回傳值: 變更副檔名後的完整的檔案路徑。images_path是list型別，回傳值就必須是list型別；images_path是tuple型別，回傳值就必須是tuple型別。
# 5. 注意: 目錄也是一種檔案，但目錄沒有副檔名，不需要變更副檔名。


def replace_filename_extension(images_path, new_extension='.png'):
    pass


def main():
    testing_argument = ['/home/eugene/dataset/train/cat.jpeg', '/home/eugene/dataset/val/dog.bmp']
    results = replace_filename_extension(testing_argument)


if __name__ == '__main__':
    main()
