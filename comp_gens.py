def decorator(func):
    def inner():
        print('running inner()')
    return inner

#decorator(target())
@decorator
def target()∏
    print('runing target()')

target()