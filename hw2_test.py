import pickle
import hw2


def test_hw2():
    test_data_files = ('hw2_data.01', 'hw2_data.02')
    test_data_truth = {'hw2_data.01': (7062, 8445), 'hw2_data.02': (7381, 8514)}

    for filename in test_data_files:
        with open(filename, 'rb') as f:
            data_dict = pickle.load(f)
            if 'prediction' not in data_dict.keys() or 'ground_truth' not in data_dict.keys():
                return False

            prediction = data_dict['prediction']
            ground_truth = data_dict['ground_truth']

            precision, recall = hw2.calc_precision_and_recall(prediction, ground_truth)
            truth = test_data_truth[filename]

            assert int(precision * 10000) == truth[0]
            assert int(recall * 10000) == truth[1]
