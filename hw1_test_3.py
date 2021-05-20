import hw1


def test_extension():
    inputs = ['/test/train/001.jpeg', '/dictionary/folder1', '/test/train/002.bmp', '/test/val/002.png']
    targets = ['/test/train/001.jpg', '/dictionary/folder1', '/test/train/002.jpg', '/test/val/002.jpg']
    assert hw1.replace_filename_extension(inputs, new_extension='.jpg') == targets

