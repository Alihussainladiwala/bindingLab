//filename: vector_opaque_list.cpp
#include <vector>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <pybind11/stl_bind.h>
namespace py = pybind11;
PYBIND11_MAKE_OPAQUE(std::vector<long long>);
PYBIND11_MODULE(vector_opaque_list, m) {
    py::bind_vector< std::vector<long long> >(m, "VectorLL");
}
