""" 
In the 20×20 grid below, four numbers along a diagonal line have been marked in 
red.

The product of these numbers is 26 × 63 × 78 × 14 = 1788696.

What is the greatest product of four adjacent numbers in the same direction 
(up, down, left, right, or diagonally) in the 20×20 grid?
"""

import numpy as np

grid = np.loadtxt('problem11.txt')

def greatest_product(grid, nlen=4):
    """function to find the greatest product of nlen numbers in any direction
    in a grid.

    Args:
        grid (np.array): the grid in a 2D numpy array of shape (N, N)
        nlen (int, optional): amount of numbers to look for. Defaults to 4.

    Returns:
        float: the greatest product
    """
    products = []
    for i in range(grid.shape[0]): # all elements in one axis
        for j in range(grid.shape[0]): # all elements in other axis
            if j < grid.shape[0]-nlen+1: # ensure to not go out of bounds
                # all horizontal products
                products.append(np.prod(grid[i,j:j+nlen]))
                # all vertical products
                products.append(np.prod(grid[j:j+nlen,i]))
                if i < grid.shape[0]-nlen+1: # ensure to not go out of bounds
                    product_diag = 1
                    for k in range(nlen):
                        # all diagonal products from upper left to lower right
                        product_diag *= grid[i+k,j+k]
                    products.append(product_diag)
                if i > 2:
                    product_diag = 1
                    for k in range(nlen):
                        # all diagonal products from upper right to lower left
                        product_diag *= grid[j+k,i-k]
                    products.append(product_diag)
    return np.max(products)

print(greatest_product(grid))