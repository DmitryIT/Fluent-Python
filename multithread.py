import time

def do_something(instance):
    print('running instance: ', instance)
    time.sleep(5)
    return instance

def main():
    do_something(1)

if __name__ == "__main__":
    main()