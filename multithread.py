import time
import sys
from concurrent import futures

MAX_WORKERS = 10
instances = [i for i in range(10)]

def show(text):
    print(text)
    sys.stdout.flush()

def do_something(instance):
    show('instance:' + str(instance))
    time.sleep(1)
    return instance

def do_many(instances):
    workers = min(len(instances), MAX_WORKERS)
    with futures.ThreadPoolExecutor(workers) as executor:
        res = executor.map(do_something, sorted(instances))

def main():
    do_many(instances)

if __name__ == "__main__":
    t0 = time.time()
    main()
    elapsed = time.time() - t0
    msg = '{} instances done in {:.2f}s'
    print(msg.format( len(instances), elapsed ))
