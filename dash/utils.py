import random, os, string, time



def signal_handler(signum, frame):
    raise Exception("Timed out!")


class Timeout(Exception):
    pass


def round_off(ele):
    if ele is not None:
        return round(ele, 3)
    else:
        return 0.00


def remove_user_files(slug, exts):
    for ext in exts:
        try:
            os.remove(slug + ext)
        except:
            continue
