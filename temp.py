from itertools import chain, dropwhile, repeat

def endless_daynames(starting_day):
    daynames = [
        'Monday', 'Tuesday', 'Wednesday', 'Thursday', 
        'Friday', 'Saturday', 'Sunday']
    # get starting day name 
    starting_day_name = daynames[starting_day] 
    # creating an endless iterable from an origin list
    endless_list = chain.from_iterable(repeat(daynames))
    # drop first items before we meet a required one
    shifted_list = dropwhile(lambda x: x != starting_day_name, endless_list)
    # yield values from it
    yield from shifted_list

print(endless_daynames('Tuesday'))


import time
start_time = time.time()
print("--- %s seconds ---" % (time.time() - start_time))  