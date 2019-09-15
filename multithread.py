import time
import sys
from concurrent import futures

MAX_WORKERS = 2
instances = [i for i in range(10)]

def show(text):
    print(text)
    sys.stdout.flush()

def do_something(instance):
    time.sleep(5)
    #show('instance:' + str(instance))
    return instance

def do_many(instances):
    workers = min(len(instances), MAX_WORKERS)
    to_do = []
    with futures.ThreadPoolExecutor(workers) as executor:
        for i in instances:
            future = executor.submit(do_something, i)
            to_do.append(future)
            msg = 'Scheduled for {}: {}'
            print(msg.format(i, future))

        for future in futures.as_completed(to_do):
            res = future.result()
            msg = '{} result: {}'
            print(msg.format(future, res))

def main():
    do_many(instances)

if __name__ == "__main__":
    t0 = time.time()
    main()
    elapsed = time.time() - t0
    msg = '{} instances done in {:.2f}s'
    print(msg.format( len(instances), elapsed ))
