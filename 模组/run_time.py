from datetime import datetime


def run_time(func):
    def new_func(*args, **kwargs):
        start_time = datetime.now()
        print(start_time)
		
        func(*args, **kwargs)
		
        end_time =  datetime.now()
        print(end_time)
		
        total_time = end_time - start_time
        print('%s Time Costed:%s' % (func.__name__, total_time))
    return new_func


@run_time
def ss():
    s = 2
    for i in range(2555):
        c = s ** i
    return print(c)
ss()











