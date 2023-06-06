#include <stdio.h>
#include <Python.h>

void print_python_string(PyObject *p) {
    if (!PyUnicode_Check(p)) {
        fprintf(stderr, "Error: Invalid string object.\n");
        return;
    }

    Py_ssize_t length = PyUnicode_GET_LENGTH(p);
    Py_UNICODE *unicode = PyUnicode_AS_UNICODE(p);

    printf("String information:\n");
    printf("  Length: %zd\n", length);
    printf("  Value: ");
    for (Py_ssize_t i = 0; i < length; i++) {
        Py_UNICODE ch = unicode[i];
        printf("%c", ch);
    }
    printf("\n");
}

