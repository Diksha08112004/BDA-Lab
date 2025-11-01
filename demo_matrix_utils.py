import matrix_utils as mu
import numpy as np  # For verification of results

def print_matrix(matrix, label=None):
    """Helper function to print a matrix with an optional label"""
    if label:
        print(f"{label}:")
    for row in matrix:
        print("  [" + " ".join(f"{x:3}" for x in row) + "]")
    print()

def main():
    print("=== Matrix Utilities Demo ===\n")
    
    # Test matrices
    A = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    
    B = [
        [9, 8, 7],
        [6, 5, 4],
        [3, 2, 1]
    ]
    
    C = [
        [1, 2],
        [3, 4],
        [5, 6]
    ]
    
    D = [
        [7, 8, 9],
        [10, 11, 12]
    ]
    
    # 1. Matrix Addition
    print("1. Matrix Addition (A + B):")
    try:
        result_add = mu.add_matrices(A, B)
        print_matrix(A, "Matrix A")
        print("  +")
        print_matrix(B, "Matrix B")
        print("  =")
        print_matrix(result_add, "Result")
        
        # Verify with numpy
        np_result = np.add(A, B).tolist()
        assert result_add == np_result, "Addition result doesn't match numpy"
        print("  ✓ Verified with numpy")
    except Exception as e:
        print(f"  Error: {e}")
    
    # 2. Matrix Subtraction
    print("\n2. Matrix Subtraction (A - B):")
    try:
        result_sub = mu.subtract_matrices(A, B)
        print_matrix(A, "Matrix A")
        print("  -")
        print_matrix(B, "Matrix B")
        print("  =")
        print_matrix(result_sub, "Result")
        
        # Verify with numpy
        np_result = np.subtract(A, B).tolist()
        assert result_sub == np_result, "Subtraction result doesn't match numpy"
        print("  ✓ Verified with numpy")
    except Exception as e:
        print(f"  Error: {e}")
    
    # 3. Matrix Transpose
    print("\n3. Matrix Transpose (C^T):")
    try:
        result_transpose = mu.transpose_matrix(C)
        print_matrix(C, "Original Matrix C")
        print("  Transpose:")
        print_matrix(result_transpose, "C^T")
        
        # Verify with numpy
        np_result = np.transpose(C).tolist()
        assert result_transpose == np_result, "Transpose result doesn't match numpy"
        print("  ✓ Verified with numpy")
    except Exception as e:
        print(f"  Error: {e}")
    
    # 4. Matrix Multiplication (using our functions)
    print("\n4. Matrix Multiplication (C × D):")
    try:
        # First, let's implement matrix multiplication using our existing functions
        def matrix_multiply(m1, m2):
            # Transpose the second matrix for easier calculation
            m2_transpose = mu.transpose_matrix(m2)
            # Perform multiplication
            result = []
            for row in m1:
                new_row = []
                for col in m2_transpose:
                    # Dot product of row and column
                    dot_product = sum(a * b for a, b in zip(row, col))
                    new_row.append(dot_product)
                result.append(new_row)
            return result
        
        result_mult = matrix_multiply(C, D)
        print_matrix(C, "Matrix C")
        print("  ×")
        print_matrix(D, "Matrix D")
        print("  =")
        print_matrix(result_mult, "Result")
        
        # Verify with numpy
        np_result = np.matmul(C, D).tolist()
        assert result_mult == np_result, "Multiplication result doesn't match numpy"
        print("  ✓ Verified with numpy")
    except Exception as e:
        print(f"  Error: {e}")
    
    # 5. Edge Cases
    print("\n5. Edge Cases:")
    
    # Empty matrix
    empty = []
    try:
        print("  Transpose of empty matrix:", mu.transpose_matrix(empty))
    except Exception as e:
        print(f"  Error with empty matrix: {e}")
    
    # Single element matrix
    single = [[5]]
    try:
        print("  Transpose of single element matrix:")
        print("  Original:", single)
        print("  Transpose:", mu.transpose_matrix(single))
    except Exception as e:
        print(f"  Error with single element matrix: {e}")
    
    # Non-rectangular matrix (should raise an error)
    non_rect = [
        [1, 2, 3],
        [4, 5],
        [6, 7, 8]
    ]
    
    print("\n6. Non-rectangular matrix test:")
    try:
        print("  Transposing non-rectangular matrix:")
        print("  Original:", non_rect)
        print("  Transpose:", mu.transpose_matrix(non_rect))
    except Exception as e:
        print(f"  ✓ Correctly raised error for non-rectangular matrix: {e}")

if __name__ == "__main__":
    main()
