from shade_triangle import *
from ambient_light import *
from diffuse_light import *
from specular_light import *
import numpy as np

def shade_gouraud(vertsp, vertsn, vertsc, bcoords, cam_pos, ka, kd,ks, n, light_positions, light_intensities, Ia, list):

    # Initalization
    I_ambient  = np.zeros((3,3))
    I_diffuse  = np.zeros((3,3))
    I_specular = np.zeros((3,3))

    for i in range(0,3):
        I_ambient[:,i]  = ambient_light(ka, Ia)
        I_diffuse[:,i]  = diffuse_light(bcoords ,vertsn[:,i] ,vertsc[:,i], kd, light_positions, light_intensities)
        I_specular[:,i] = specular_light(bcoords , vertsn[:,i], vertsc[:,i], cam_pos, ks, n,light_positions, light_intensities)
    
    # The 4 different colors for the 4 images
    vcolors1 = I_ambient
    vcolors2 = I_diffuse
    vcolors3 = I_specular
    vcolors4 = I_ambient + I_diffuse + I_specular

    # Paint a triangle in the 4 different lights
    Y1 = shade_triangle(list[0] ,np.transpose(vertsp), np.transpose(vcolors1), "gouraud")
    Y2 = shade_triangle(list[1] ,np.transpose(vertsp), np.transpose(vcolors2), "gouraud")
    Y3 = shade_triangle(list[2] ,np.transpose(vertsp), np.transpose(vcolors3), "gouraud")
    Y4 = shade_triangle(list[3] ,np.transpose(vertsp), np.transpose(vcolors4), "gouraud")

    return np.array([Y1,Y2,Y3,Y4])