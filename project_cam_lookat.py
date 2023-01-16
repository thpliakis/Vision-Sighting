import numpy as np
from project_cam import project_cam

def project_cam_lookat(f,corg,clookat,cup,verts3d):
    
    # Compute the basis vectors of the camera
    cz = clookat - corg
    cz = cz/ np.linalg.norm(cz)

    cy = cup - np.matmul(np.transpose(cup),cz)*cz
    cy = cy/np.linalg.norm(cy)
    
    cx = np.cross(cy,cz,axis=0)

    # compute the perspective projection and depth
    verts2d, depth = project_cam(f,corg,cx,cy,cz,verts3d)

    return verts2d, depth