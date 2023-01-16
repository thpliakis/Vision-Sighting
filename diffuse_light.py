import numpy as np

def diffuse_light(P ,N ,color ,kd, light_positions, light_intensities):

    l = np.subtract(light_positions,P)
    L = l/np.linalg.norm(l)
    I = np.multiply(light_intensities,color)*kd*np.dot(L,N)
    return I