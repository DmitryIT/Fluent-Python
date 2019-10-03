import time
from concurrent import futures

import sha256

MAX_WORKERS = 4
PATH = './data'

def calc_checksum_parallel(file_list):
    workers = min( len(file_list), MAX_WORKERS )
    to_do = []
    with futures.ProcessPoolExecutor(workers) as executor:
        for file in file_list:
            future = executor.submit(sha256.calc_one_checksum, file)
            to_do.append(future)
            msg = 'Scheduled for {}:{}'
            print(msg.format(file, future))

        for future in futures.as_completed(to_do):
            res = future.result()
            msg = '{} result: {}'
            print(msg.format(future, res))

def main():
    t0 = time.time()
    file_list = sha256.file_list(PATH)
    calc_checksum_parallel(file_list)
    elapsed = time.time() - t0
    msg = '{} files processed in {:.2f}s'
    print(msg.format(len(file_list), elapsed ))

if __name__ == "__main__":
    main()