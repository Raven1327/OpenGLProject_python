import openmesh as om
import numpy as np

mesh = om.TriMesh()

# add a a couple of vertices to the mesh
vh0 = mesh.add_vertex([-1, 1, -1])
vh1 = mesh.add_vertex([0, 0, 0])
vh2 = mesh.add_vertex([1, 1, -1])
vh3 = mesh.add_vertex([-1,-1, -1])
vh4 = mesh.add_vertex([1,-1, -1])

# add a couple of faces to the mesh
fh0 = mesh.add_face(vh0, vh1, vh2)
fh1 = mesh.add_face(vh1, vh3, vh4)
fh2 = mesh.add_face(vh0, vh3, vh1)

mesh.set_color(vh0, [1,0,0,0])
mesh.set_color(vh1, [1,1,1,0])
mesh.set_color(vh2, [0,1,0,0])
mesh.set_color(vh3, [0,0,1,0])
mesh.set_color(vh4, [0,0,0,0])

n = [0,0,0,0]
mesh.set_normal(vh0, n)
mesh.set_normal(vh1, n)
mesh.set_normal(vh2, n)
mesh.set_normal(vh3, n)
mesh.set_normal(vh4, n)

# add another face to the mesh, this time using a list
vh_list = [vh2, vh1, vh4]
fh3 = mesh.add_face(vh_list)

#  0 ==== 2
#  |\  0 /|
#  | \  / |
#  |2  1 3|
#  | /  \ |
#  |/  1 \|
#  3 ==== 4

# get the point with vertex handle vh0
point = mesh.point(vh0)

# get all points of the mesh
point_array = mesh.points()

# translate the mesh along the x-axis
# point_array += np.array([1, 0, 0])

# write and read meshes
om.write_mesh('cone.ply', mesh,vertex_normal=True,vertex_color=True)