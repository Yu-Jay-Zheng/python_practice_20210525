import hw1


def test_datatype():
    list_images = list()
    tuple_images = tuple()
    assert isinstance(hw1.replace_filename_extension(list_images), list)
    assert isinstance(hw1.replace_filename_extension(tuple_images), tuple)
