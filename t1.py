import time

from tqdm.auto import tqdm

with tqdm(total=10) as t:
    time.sleep(5)
    t.update(5)
    time.sleep(2)
    t.update(2)
    time.sleep(5)
    t.update(3)

