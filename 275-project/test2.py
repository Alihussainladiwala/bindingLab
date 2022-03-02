from vector_opaque_list import VectorLL
import functools
import time
from random import shuffle
def time_this(func):
    @functools.wraps(func)  # preserves metadata of original func
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        func_run_time = end_time - start_time
        print(f"Finished {func.__name__!r} in {func_run_time:.5f} secs")
        return value
    return wrapper_timer
@time_this
def vector_init(size):
    vll = VectorLL()
    for _ in range(size): vll.append(0)
    return vll
@time_this
def py_listcomp_init(size):
    l = [0 for _ in range(size)]
    return l
@time_this
def py_list_init(size):
    l = [0]*size
    return l
@time_this
def mod_vector(int_list, cpp_vector):
    for i,val in enumerate(int_list): cpp_vector[i]=val
@time_this
def mod_listcomp(int_list, listcomp):
    for i,val in enumerate(int_list): listcomp[i]=val
@time_this
def mod_listmath(int_list, listmath):
    for i,val in enumerate(int_list): listmath[i]=val
@time_this
def calc_vector(cpp_vector):
    i=0
    while i < len(cpp_vector):
        cpp_vector[i]=cpp_vector[i]*cpp_vector[i]-3
        i+=1
@time_this
def calc_listcomp(listcomp):
    return [(x**2)-3 for x in listcomp]
sizes = [1_000, 10_000, 100_000, 1_000_000, 10_000_000]
for test_case in sizes:
    int_list = [x for x in range(test_case)]
    shuffle(int_list)
    print(test_case)
    print("===========INIT=============")
    cpp_vector = vector_init(test_case)
    listcomp = py_listcomp_init(test_case)
    listmath = py_list_init(test_case)
    print("============================")
    print("============MOD=============")
    mod_vector(int_list, cpp_vector)
    mod_listcomp(int_list, listcomp)
    mod_listmath(int_list, listmath)
    print("===========================")
    print("===========CALC============")
    x = calc_vector(cpp_vector)
    listcomp = calc_listcomp(listcomp)
    print(sum(cpp_vector))
    print(sum(listcomp))
    print("===========================\n\n")
