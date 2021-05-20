import hw1


def test_output1():
    inputs = ['/test/train/001.jpeg', '/test/val/001.JPEG', '/test/train/002.bmp', '/test/val/002.png']
    targets = ['/test/train/001.png', '/test/val/001.png', '/test/train/002.png', '/test/val/002.png']
    assert hw1.replace_filename_extension(inputs) == targets
