import hw1


def test_output2():
    inputs = ['/test/train/001.jpeg', '/dictionary/folder1', '/test/train/002.bmp', '/test/val/002.png']
    targets = ['/test/train/001.png', '/dictionary/folder1', '/test/train/002.png', '/test/val/002.png']
    assert hw1.replace_filename_extension(inputs) == targets
