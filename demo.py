import numpy as np
from affine_transform import affine_transform
from render_object import render_object
import matplotlib.pyplot as plt
import matplotlib

focal = 70 

# Load data
data = np.load("hw3.npy", allow_pickle=True)
verts = data[()]['verts']
verts_colors = data[()]['vertex_colors']
face_indices = data[()]['face_indices']
depth = data[()]['depth']
eye = data[()]['cam_eye']
up = data[()]['cam_up']
lookat = data[()]['cam_lookat']
ka = data[()]['ka']
kd = data[()]['kd']
ks = data[()]['ks']
n = data[()]['n']
light_positions = data[()]['light_positions']
light_intensities = data[()]['light_intensities']
Ia = data[()]['Ia']
M = data[()]['M']
N = data[()]['N']
W = data[()]['W']
H = data[()]['H']
bg_color = data[()]['bg_color']

# Reshape data 
verts = np.transpose(verts)
verts_colors = np.transpose(verts_colors)
face_indices = np.transpose(face_indices)

shader = "gouraud"
I = render_object(shader, focal, eye, lookat, up, bg_color, M, N, H, W, verts, verts_colors, face_indices, ka, kd, ks, n, light_positions, light_intensities, Ia)

for i in range(0,4):
    I[i][I[i]<0]=0
    I[i][I[i]>1]=1

matplotlib.image.imsave('gouraud_ambient.png', I[0])
matplotlib.image.imsave('gouraud_diffuse.png', I[1])
matplotlib.image.imsave('gouraud_specular.png', I[2])
matplotlib.image.imsave('gouraud_all3together.png', I[3])

# Below all the 4 images are plotted together
imgs = np.array([I[0], I[0], I[1], I[2], I[3]])
fig = plt.figure(figsize=(2,2))
for i in range(1,5):
    fig.add_subplot(2,2,i)
    plt.xlim([600, 0])
    plt.ylim([0, 600])
    plt.imshow(imgs[i])
plt.show()

shader = "phong"
I = render_object(shader, focal, eye, lookat, up, bg_color, M, N, H, W, verts, verts_colors, face_indices, ka, kd, ks, n, light_positions, light_intensities, Ia)

for i in range(0,4):
    I[i][I[i]<0]=0
    I[i][I[i]>1]=1
# 
matplotlib.image.imsave('phong_ambient.png', I[0])
matplotlib.image.imsave('phong_diffuse.png', I[1])
matplotlib.image.imsave('phong_specular.png', I[2])
matplotlib.image.imsave('phong_all3together.png', I[3])
# 
# Below all the 4 images are plotted together
imgs = np.array([I[0], I[0], I[1], I[2], I[3]])
fig = plt.figure(figsize=(2,2))
for i in range(1,5):
    fig.add_subplot(2,2,i)
    plt.xlim([600, 0])
    plt.ylim([0, 600])
    plt.imshow(imgs[i])
plt.show()