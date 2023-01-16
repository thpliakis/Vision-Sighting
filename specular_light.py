import numpy as np

def specular_light(P, N, color, cam_pos, ks , n, light_positions, light_intensities):

    l = np.subtract(light_positions,P)
    L = l/np.linalg.norm(l)
    v = np.subtract(cam_pos,P)
    V = v/np.linalg.norm(v)
    I = np.multiply(light_intensities,color)*ks*np.power(np.dot(np.subtract(2*N*np.dot(L,N),L),V),n)
    return I