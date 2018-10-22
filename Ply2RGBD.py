from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from PIL import Image
import openmesh as om

WINDOW_WIDTH = 1024
WINDOW_HEIGHT = 768
POINT_FARZ = -200
POINT_NEARZ = 500
DRAW_I = 0

def screenshot(name="", format='png'):
    """
    Create a screenshot
    :param format: formats supported by PIL (png, jpeg etc)
    """
    dest = "./"

    x, y, width, height = glGetIntegerv(GL_VIEWPORT)
    print("Screenshot viewport:", x, y, width, height)
    glPixelStorei(GL_PACK_ALIGNMENT, 1)

    data = glReadPixels(x, y, width, height, GL_RGB, GL_UNSIGNED_BYTE)

    image = Image.frombytes("RGB", (width, height), data)
    image = image.transpose(Image.FLIP_TOP_BOTTOM)
    name = "{}.{}".format(name, format)
    image.save(os.path.join(dest, name), format=format) 

def drawFunc():
    global mesh, DRAW_I
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    global POINT_FARZ, POINT_NEARZ, DRAW_I

    # Draw RGB
    if DRAW_I == 0:
        glPushMatrix()
        glBegin(GL_TRIANGLES)
        for fi in mesh.faces():
            for fvi in mesh.fv(fi):
                glColor4fv(mesh.color(fvi))
                glVertex3fv(mesh.point(fvi))
        glEnd()
        glPopMatrix()
        glFlush()

        screenshot(name="RGB")
        DRAW_I += 1
    elif DRAW_I == 1:
        glPushMatrix()
        glBegin(GL_TRIANGLES)
        for fi in mesh.faces():
            for fvi in mesh.fv(fi):
                depthZ = mesh.point(fvi)[2]
                val = (depthZ - POINT_FARZ) / (POINT_NEARZ - POINT_FARZ)
                glColor4fv([val, val, val, 0])
                glVertex3fv(mesh.point(fvi))
        glEnd()
        glPopMatrix()
        glFlush()

        screenshot(name="D")
        exit()

def main():
    global mesh
    mesh = om.read_trimesh('plyFile/face.ply',vertex_color=True)

    global WINDOW_WIDTH, WINDOW_HEIGHT, POINT_FARZ, POINT_NEARZ

    # 使用glut初始化OpenGL
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGBA)

    # 建立視窗
    glutInitWindowPosition(0,0)
    glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)
    glutCreateWindow(b"first")

    # 初始化
    glShadeModel(GL_SMOOTH)
    glClearColor(0.0, 0.0, 0.0, 0.5)
    glClearDepth(1.0)
    glEnable(GL_DEPTH_TEST)
    glDepthFunc(GL_LEQUAL)

    # 視角
    gluPerspective(80, WINDOW_WIDTH/WINDOW_HEIGHT, 0.1, POINT_NEARZ - POINT_FARZ)
    gluLookAt(0, 0, POINT_NEARZ,    # eye
        0, 0 , 0,                   # center
        0, 1, 0)                    # Top

    # 顯示函數
    glutDisplayFunc(drawFunc)
    glutIdleFunc(drawFunc)
    glutMainLoop()

if __name__ == '__main__':
    main()