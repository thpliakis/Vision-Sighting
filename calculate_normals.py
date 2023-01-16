import numpy as np

def calculate_normals(vertices, face_indices):
    
    Nt = face_indices.shape[1]
    Nu = vertices.shape[1]

    v01 = np.zeros((3,Nt))
    triangle_normals = np.zeros((3,Nt))
    v12 = np.zeros((3,Nt))
    vertices_indicies = np.zeros((Nu,Nt))
    normals = np.zeros((3,Nu))

    v01 = np.subtract(vertices[:,np.transpose(face_indices[1,:])],vertices[:,np.transpose(face_indices[0,:])])
    v12 = np.subtract(vertices[:,np.transpose(face_indices[2,:])],vertices[:,np.transpose(face_indices[1,:])])
    
    # for i in range(0,Nt):
    #     v01[:,i] = v01[:,i]/np.linalg.norm(v01[:,i])
    #     v12[:,i] = v12[:,i]/np.linalg.norm(v12[:,i])

    for i in range(0,Nt):
        triangle_normals[:,i] = np.cross(v01[:,i],v12[:,i])
        triangle_normals[:,i] = triangle_normals[:,i]/np.linalg.norm(triangle_normals[:,i])

    for i in range(0,Nu):
        for j in range(0,Nt):
            if face_indices[0,j] == i or face_indices[1,j] == i or face_indices[2,j] == i:
                vertices_indicies[i,j] = True
            else:
                vertices_indicies[i,j] = False

    for i in range(0,Nu):
        n = 0
        t = np.zeros(3)
        for j in range(0,Nt):
            if vertices_indicies[i,j] == True:
                n += 1
                t += triangle_normals[:,j]
        normals[:,i] = t[:]/n

    return normals