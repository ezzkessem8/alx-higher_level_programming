#include <stdio.h>
#include <Python.h>

/**
 * print_python_bytes - Prints bytes information
 * @p: Python Object
 * Return: void
 */
void print_python_bytes(PyObject *p) {
    char *string;
    Py_ssize_t size, limit, i;

    setbuf(stdout, NULL);

    printf("[.] bytes object info\n");
    if (!PyBytes_Check(p)) {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    size = ((PyVarObject *)p)->ob_size;
    string = ((PyBytesObject *)p)->ob_sval;

    printf("  size: %ld\n", size);
    printf("  trying string: %s\n", string);

    limit = (size > 10) ? 10 : size;

    printf("  first %ld bytes:", size);

    for (i = 0; i < limit; i++) {
        printf(" %02hhx", string[i]);
    }
    printf("\n");
}

/**
 * print_python_float - Prints float information
 * @p: Python Object
 * Return: void
 */
void print_python_float(PyObject *p) {
    double val;
    char *nf;

    setbuf(stdout, NULL);
    printf("[.] float object info\n");

    if (!PyFloat_Check(p)) {
        printf("  [ERROR] Invalid Float Object\n");
        return;
    }

    val = ((PyFloatObject *)p)->ob_fval;
    nf = PyOS_double_to_string(val, 'r', 0, Py_DTSF_ADD_DOT_0, Py_DTST_FINITE);

    printf("  value: %s\n", nf);
}

/**
 * print_python_list - Prints list information
 * @p: Python Object
 * Return: void
 */
void print_python_list(PyObject *p) {
    Py_ssize_t size, i;
    PyObject *item;

    setbuf(stdout, NULL);
    printf("[*] Python list info\n");

    if (!PyList_Check(p)) {
        printf("  [ERROR] Invalid List Object\n");
        return;
    }

    size = ((PyVarObject *)p)->ob_size;

    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

    for (i = 0; i < size; i++) {
        item = PyList_GetItem(p, i);
        printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);

        if (PyBytes_Check(item)) {
            print_python_bytes(item);
        } else if (PyFloat_Check(item)) {
            print_python_float(item);
        }
    }
}

