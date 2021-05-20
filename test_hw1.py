import hw1


def test_datatype():
    list_images = list()
    tuple_images = tuple()
    assert isinstance(hw1.replace_filename_extension(list_images), list)
    assert isinstance(hw1.replace_filename_extension(tuple_images), tuple)


def test_output1():
    inputs = ['/test/train/001.jpeg', '/test/val/001.JPEG', '/test/train/002.bmp', '/test/val/002.png']
    targets = ['/test/train/001.png', '/test/val/001.png', '/test/train/002.png', '/test/val/002.png']
    assert hw1.replace_filename_extension(inputs) == targets


def test_output2():
    inputs = ['/test/train/001.jpeg', '/dictionary/folder1', '/test/train/002.bmp', '/test/val/002.png']
    targets = ['/test/train/001.png', '/dictionary/folder1', '/test/train/002.png', '/test/val/002.png']
    assert hw1.replace_filename_extension(inputs) == targets


def test_extension():
    inputs = ['/test/train/001.jpeg', '/dictionary/folder1', '/test/train/002.bmp', '/test/val/002.png']
    targets = ['/test/train/001.jpg', '/dictionary/folder1', '/test/train/002.jpg', '/test/val/002.jpg']
    assert hw1.replace_filename_extension(inputs, new_extension='.jpg'
                                                                '') == targets

