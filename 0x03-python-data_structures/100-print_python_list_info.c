#include <Python.h>

void print_python_list_info(PyObject *p)
{
	int size = PyList_Size(p);
	int allocated = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", allocated);

	for (int i = 0; i < size; i++)
	{
		PyObject *item = PyList_GetItem(p, i);
		printf("Element %d: %s\n", i, Py_TYPE(item)->tp_name);
	}
}

int main(void)
{
	return 0;
}
