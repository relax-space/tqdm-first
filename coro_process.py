
import time
from multiprocessing import Pool, RLock, freeze_support

import colorama
from tqdm import tqdm


def f_process(d):
    for i in tqdm(range(10), colour='red', desc=f'{d}', position=d, leave=False, bar_format='{l_bar}{bar:5}{r_bar}'):
        if i%4==0:
            print(f'\r{"111111".ljust(150)}\r')
        time.sleep(1)


def main():
    args = [0, 1, 2]
    tqdm.set_lock(RLock())
    with Pool(initializer=tqdm.set_lock, initargs=(tqdm.get_lock(),)) as p:
        r = list(tqdm(p.imap(f_process, args), total=3, colour='green'))
    pass


if __name__ == '__main__':
    # freeze_support()  # for Windows support
    main()
