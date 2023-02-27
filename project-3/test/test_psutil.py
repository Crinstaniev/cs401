import psutil


def test_get_process_list():
    for p in psutil.process_iter():
        print(p.name())


