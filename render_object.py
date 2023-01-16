from asyncio import FastChildWatcher
from calculate_normals import *
from project_cam_lookat import *
from rasterize import *
from shade_gouraud import *
from shade_phong import *
import numpy as np

def render_object(shader, focal, eye, lookat, up, bg_color, M, N, H, W, verts, verts_colors, face_indices, ka, kd, ks, n, light_position, light_intensities, Ia):

    #1 Calculate normal for each vertice 
    normals = calculate_normals(verts, face_indices)

    #2 Calculate the projection to a surface and the depth of each traingle
    verts2d, depth = project_cam_lookat(focal,eye,lookat,up,verts)

    #3
    # Clipping
    verts_rast = rasterize(verts2d,M,N,H,W)

    # Paint the traingles
    I1 = np.zeros((M,N,3))
    for i in range(0,M):
        for j in range(0,N):
            I1[i,j,:] = bg_color[:]
    
    I2 = I1
    I3 = I1
    I4 = I1

    I = np.array([I1, I2, I3, I4])

    Nt = face_indices.shape[1]

    # Initialize of the matrix I-image 
    Dm = np.zeros(Nt)
    vertsp = np.zeros((2,3))
    vertsn = np.zeros((3,3))
    verts3d = np.zeros((3,3))
    vertsc = np.zeros((3,3))
    # bcoords = np.zeros(3)
    D_sorted = np.zeros(Nt)
    D_order = np.zeros(Nt)

    # Calculation of the average depth of each triangle 
    for i in range(0,Nt):
        for j in range(0,3):
            Dm[i] = depth[face_indices[j,i]]+Dm[i]
        Dm[i] = Dm[i]/3
        
    # Sort of the Dm and the face_indices in descending order 
    # In D_order is the indexes osrted the same way as Dm and face_indices
    D_order  = np.flip(np.argsort(Dm))
    D_sorted = np.flip(np.sort(Dm))
    face_indices = face_indices[:,D_order]
    Dm = D_sorted

    for i in range(0,Nt):
        bcoords = np.zeros(3)
        for j in range(0,3):
            vertsp[:,j] = verts_rast[:,face_indices[j,i]]
            verts3d[:,j] = verts[:,face_indices[j,i]]
            vertsc[:,j] = verts_colors[:,face_indices[j,i]]
            vertsn[:,j] = normals[:,face_indices[j,i]]
        
        for k in range(0,3):
            for l in range(0,3):
                bcoords[k] += verts3d[k,l]
            bcoords[k] = bcoords[k]/3
        
        if shader == 'gouraud':
            I = shade_gouraud(vertsp, vertsn, vertsc, bcoords, eye, ka, kd,ks, n, light_position, light_intensities, Ia,I)
        else:
            I = shade_phong(vertsp, vertsn, vertsc, bcoords, eye, ka, kd, ks, n, light_position, light_intensities, Ia, I)

    return I