from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import openmesh as om

def drawFunc():
    global mesh
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glPushMatrix()
    glBegin(GL_TRIANGLES)
    for fi in mesh.faces():
        for fvi in mesh.fv(fi):
            glColor4fv(mesh.color(fvi))
            glVertex3fv(mesh.point(fvi))
    glEnd()
    glPopMatrix()
    
    glRotatef(0.1, 0, 1, 0)
    glFlush()

def main():
    global mesh
    mesh = om.read_trimesh('plyFile/cone.ply',vertex_color=True)
    
    # 使用glut初始化OpenGL
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGBA)

    # 建立視窗
    glutInitWindowPosition(0,0)
    glutInitWindowSize(1024, 768)
    glutCreateWindow(b"first")

    # 初始化
    glShadeModel(GL_SMOOTH)
    glClearColor(0.0, 0.0, 0.0, 0.5)
    glClearDepth(1.0)
    glEnable(GL_DEPTH_TEST)
    glDepthFunc(GL_LEQUAL)

    # 視角
    gluPerspective(80, 1024/768, 0.1, 1000)
    gluLookAt(0, 0, 10,             # eye
        0, 0 , 0,                   # center
        0, 1, 0)                    # Top

    # 顯示函數
    glutDisplayFunc(drawFunc)
    glutIdleFunc(drawFunc)
    glutMainLoop()

if __name__ == '__main__':
    main()