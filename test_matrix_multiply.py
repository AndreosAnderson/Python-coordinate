import numpy as np
import pytest
from matrix_operations import track_memory, track_cpu, matrix_multiply,convertToCOO


@pytest.fixture
def setup_matrices():
    size = 1024
    A = np.random.rand(size, size)
    B = np.random.rand(size, size)
    cooA = convertToCOO(A, size)
    cooB = convertToCOO(B, size)
    return cooA, cooB


@pytest.mark.benchmark(min_rounds=5)
def test_matrix_multiply(benchmark, setup_matrices):
    A, B = setup_matrices

    result = benchmark(matrix_multiply, A, B)

    track_memory(matrix_multiply, A, B)
    track_cpu(matrix_multiply, A, B)

    assert result is not None
