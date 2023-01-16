import numpy as np
from system_transform import system_transform

def project_cam(f,cv,cx,cy,cz,p):

    # Initialize rotation matrix
    R = np.zeros((3,3))
    R[:,0] = cx
    R[:,1] = cy
    R[:,2] = cz

    # Chage points coordinate system from WCS to the camera's system
    pc = system_transform(p, R, cv)

    # Compute the depth of the points and exclude those outside the camera view
    depth = pc[2,:]
    noview = depth <= 0
    depth = depth[noview==False]
    pc = pc[:,noview==False]

    # Compute the perspective projection of the points
    pc = f*pc
    verts2d = np.zeros((2,4998))
    verts2d[0,:] = np.divide(pc[0,:], depth[:])
    verts2d[1,:] = np.divide(pc[1,:], depth[:])

    return verts2d,depth 