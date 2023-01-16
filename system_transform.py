import numpy as np

def system_transform(cp, R, c0):

    # Get the dimensions of the matrix cp
    dims = cp.shape

    # Create L matrix
    L = np.zeros((4,4))
    L[0:3,0:3] = np.transpose(R)
    temp = np.matmul(-np.transpose(R),c0)
    L[0:3,3] = temp
    L[3,3] = 1

    # Write cp vector maxtrix with homogeneous coordinates
    homogeneous_coo = np.ones((dims[0]+1,dims[1]))  
    homogeneous_coo[0:3,:] = cp[0:3,:]

    # Calculate coordinates in the new coordinate system
    dp = np.matmul(L,homogeneous_coo)

    return dp[0:3,:]