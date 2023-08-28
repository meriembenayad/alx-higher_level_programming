#include <Python.h>

void print_python_list(PyObject *p)
{
	if (!PyList_Check(p))
	{
		fprintf(stderr, "[ERROR] Invalid Python List\n");
		return;
	}

	Py_ssize_t size = PyList_Size(p);
	Py_ssize_t allocated = ((PyListObject *)p)->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", allocated);

	for (Py_ssize_t i = 0; i < size; ++i)
	{
		PyObject *item = PyList_GetItem(p, i);
		const char *item_type = Py_TYPE(item)->tp_name;
		printf("Element %ld: %s\n", i, item_type);
	}
}

void print_python_bytes(PyObject *p)
{
	if (!PyBytes_Check(p))
	{
		fprintf(stderr, "[ERROR] Invalid Bytes Object\n");
		return;
	}

	Py_ssize_t size = PyBytes_Size(p);
	const char *string_repr = PyBytes_AsString(p);

	printf("[.] bytes object info\n");
	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", string_repr);

	printf("  first %ld bytes:", size > 10 ? 10 : size);
	for (Py_ssize_t i = 0; i < (size > 10 ? 10 : size); ++i)
	{
		printf(" %02x", (unsigned char)string_repr[i]);
	}
	printf("\n");
}
