import numpy as np
import math 

def affine_transform(cp, theta, u, t):

    # Get the dimensions of the matrix cp
    dims = cp.shape

    # For the Rodrigues' rotation formula
    # u = u / np.linalg.norm(u)
    outer = np.matmul(u , np.transpose(u))
    I = np.identity(3)
    cross = np.array([[0, -u[2,0], u[1,0]],[u[2,0], 0, -u[0,0]],[-u[1,0], u[0,0], 0]])

    # Rodrigues formula in non homogeneouus coordinates
    R = (1 - math.cos(theta)) * outer + math.cos(theta) * I + math.sin(theta) * cross

    # calculate the affine matrix in homogenus coordinates
    Affine = np.zeros((4,4))
    Affine[0:3,0:3] = R
    Affine[0:3,3] = t[:,0]
    Affine[3,3] = 1
    
    # Write cp vector maxtrix with homogeneous coordinates
    homogeneous_coo = np.ones((dims[0]+1,dims[1]))  
    homogeneous_coo[0:3,:] = cp[0:3,:]
    
    # Calculate new coordinates 
    cq = np.matmul(Affine,homogeneous_coo)
    
    return cq[0:3,:]