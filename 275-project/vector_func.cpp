//filename: vector_func.cpp
#include <vector>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <pybind11/stl_bind.h>
namespace py = pybind11;
PYBIND11_MAKE_OPAQUE(std::vector<long long>);
double apply_calc(std::vector<long long> &pylist) {
	double mean = 0.0;
	double summ = 0.0;
    for(unsigned long long i=0; i<pylist.size(); i++) {
        //pylist[i] = (pylist[i]*pylist[i])-3;
		mean += pylist[i];
    }
	 
	mean /= pylist.size();
	double diff = 0.0;
	for(unsigned long long i=0; i<pylist.size(); i++) {
        diff = pylist[i] - mean;
		summ += diff * diff;
		
		
    }
	
	double result = py::module::import("math").attr("sqrt")(summ/pylist.size()).cast<double>();
	
	return result;
}
PYBIND11_MODULE(vector_func, m) {
    m.doc() = "x**2 -3 to each element in list"; // optional module docstring
    py::bind_vector< std::vector<long long> >(m, "CVector");
    m.def("apply_calc", &apply_calc, "applies x**2-3 on each element");
}
