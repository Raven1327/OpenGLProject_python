import openmesh as om
import numpy as np
import cv2.cv2 as cv

mesh = om.TriMesh()
rgbImg = cv.imread('rgb.png')
dImg = cv.imread('d.png')

imgWidth = rgbImg.shape[0]
imgHeight = rgbImg.shape[1]

for i in range(0, imgWidth):
    for j in range(0, imgHeight):
        if dImg[i, j][0] > 0:
            x = j
            y = -i
            z = dImg[i, j][0] * 2.3
            vh = mesh.add_vertex([x, y, z])

            g = rgbImg[i, j][0] / 255
            b = rgbImg[i, j][1] / 255
            r = rgbImg[i, j][2] / 255
            mesh.set_color(vh, [r, g, b, 0])

om.write_mesh('PointCloud.ply', mesh, vertex_color=True)