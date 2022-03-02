from vector_func import CVector, apply_calc
import functools
import time
from random import shuffle
import math 
def time_this(func):
    @functools.wraps(func)  # preserves metadata of original func
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        func_run_time = end_time - start_time
        print(f"Finished {func.__name__!r} in {func_run_time:.5f} secs")
        return (value, func_run_time)
    return wrapper_timer
@time_this
def vector_init(p_list):
    return CVector(p_list)
@time_this
def py_listcomp_init(p_list):
    return p_list
@time_this
def calc_vector(c_obj):
    return apply_calc(c_obj)
@time_this
def calc_listcomp(a):
    mean = sum(a) / len(a)
    return math.sqrt((sum(((x - mean)**2 for x in a)) / len(a)))
    
sizes = [1_000, 10_000, 100_000, 1_000_000, 10_000_000]
print("pyBind11")
for test_case in sizes:
    print("TEST CASE: ", test_case)
    int_list = [x for x in range(test_case)]
    shuffle(int_list)
    CVec = CVector()
    print("===========INIT============")
    cpp_vector, v_init_time = vector_init(int_list)
    listcomp, l_init_time = py_listcomp_init(int_list)
    print("===========================")
    print("===========CALC============")
    cpp_vector, v_calc_time = calc_vector(cpp_vector)
    listcomp, l_calc_time = calc_listcomp(int_list)
    print("CPP METHOD: ", cpp_vector)
    print("LIST COMP : ", listcomp)
    print("===========================")
    print("===========TIME============")
    v_total = v_init_time+v_calc_time
    l_total = l_init_time+l_calc_time
    print("CPP METHOD: ", v_total)
    print("LIST COMP : ", l_total)
    print("CPP FASTER BY: ", l_total/v_total)
    print("===========================\n\n\n")
