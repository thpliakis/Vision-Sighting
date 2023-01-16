import math
import numpy as np

def rasterize(verts2d,imgh,imgw,camh,camw):

    outside = np.zeros(verts2d.shape) 
    #check which points are outside the plane 
    checkX = (verts2d[0,:] <= -camw/2) | (verts2d[0,:] >= camw/2)   
    checkY = (verts2d[1,:] <= -camh/2) | (verts2d[1,:] >= camh/2)   
    outside = checkX | checkY
    # Exclude the points outsidethe projection plane
    verts2d[:,outside[:]] = 0

    #Change the origin of the projection plane to match that of the image
    verts2d[0,:] = verts2d[0,:] + camw/2
    verts2d[1,:] = verts2d[1,:] + camh/2
    
    # Compute pixels coordinates
    n = camw/imgw
    m = camh/imgh

    verts2d[0,:] = verts2d[0,:]/n
    verts2d[1,:] = verts2d[1,:]/m

    vertsrast = np.ceil(verts2d)

    return vertsrast