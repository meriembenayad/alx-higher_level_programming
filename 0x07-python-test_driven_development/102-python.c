#include <Python.h>
#include <stdio.h>

void print_python_string(PyObject *p)
{
	/* Check if p is a valid string object */
	if (!PyUnicode_Check(p))
	{
		printf("[.] string object info\n");
		printf("  [ERROR] Invalid String Object\n");
		return;
	}

	/* Get the string data and length */
	Py_ssize_t length = PyUnicode_GET_LENGTH(p);
	const char *data = PyUnicode_AsUTF8AndSize(p, &length);

	/* Determine the string type */
	const char *type;
	if (PyUnicode_IS_COMPACT_ASCII(p))
		type = "compact ascii";
	else if (PyUnicode_IS_COMPACT(p) && !PyUnicode_IS_ASCII(p))
		type = "compact unicode object";
	else
		type = "unknown";

	/* Print the string information */
	printf("[.] string object info\n");
	printf("  type: %s\n", type);
	printf("  length: %ld\n", length);
	printf("  value: %s\n", data);
}
