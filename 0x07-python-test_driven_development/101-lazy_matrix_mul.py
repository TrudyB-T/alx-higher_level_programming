#!/usr/bin/python3.5
"""

function that multiplies 2 matrices

"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """multiplies 2 matrices

    Arguments:
             m_a: matrix a
             m_b: matrix b

    """

    return (np.matmul(m_a, m_b))
