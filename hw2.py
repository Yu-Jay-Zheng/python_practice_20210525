# Author: Eugene
# https://sites.google.com/view/smartrobot/lab


# 題目說明:
# 1. 完成函數calc_precision_and_recall，計算precision和recall。
# 2. 類別ID: 僅有兩類，0表示Negative，1表示Positive。
# 3. 參數prediction: 儲存預測的類別ID, 是一個2維的list，類似於一張圖片的結構，儲存預測的類別ID,每一個數值代表每一個像素的預測類別。
# 4. 參數ground_truth: 儲存實際的類別ID, 是一個2維的list，類似於一張圖片的結構，每一個數值代表每一個像素的實際類別。
# 5. 回傳值: precision和recall。
# 6. Precision = TP / (TP + FP)
# 7. Recall = TP /  (TP + FN)


import pickle


def calc_precision_and_recall(prediction, ground_truth):
    pass


def main():
    with open('hw2_data.01', 'rb') as f:
        data_dict = pickle.load(f)
        if 'prediction' not in data_dict.keys() or 'ground_truth' not in data_dict.keys():
            print('Error in hw2_data')
            return

        prediction = data_dict['prediction']
        ground_truth = data_dict['ground_truth']

        precision, recall = calc_precision_and_recall(prediction, ground_truth)


if __name__ == '__main__':
    main()
