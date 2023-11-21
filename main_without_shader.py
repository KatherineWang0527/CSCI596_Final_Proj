from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def draw_scene():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    # Set the camera
    gluLookAt(0.0, 0.0, 5.0,  # Eye position
              0.0, 0.0, 0.0,  # Look at position
              0.0, 1.0, 0.0)  # Up vector

    # Set up light source
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_COLOR_MATERIAL)
    glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)
    glLightfv(GL_LIGHT0, GL_POSITION, [0, 0, 1, 0])
    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, [0.1, 0.1, 0.1, 1])

    # Set material properties for the teapot
    glColor3f(1.0, 0.0, 0.0)  # Red color

    # Draw the teapot
    glutSolidTeapot(1.0)

    # Swap the front and back frame buffers (double buffering)
    glutSwapBuffers()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(640, 480)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"OpenGL Teapot Without Shaders")

    # Lighting and depth test are enabled
    glEnable(GL_DEPTH_TEST)
    glDepthFunc(GL_LEQUAL)
    glClearColor(0.0, 0.0, 0.0, 1.0)

    # Set up the projection matrix
    glMatrixMode(GL_PROJECTION)
    gluPerspective(45, (640/480), 0.1, 50.0)
    glMatrixMode(GL_MODELVIEW)

    # Register the drawing function with GLUT
    glutDisplayFunc(draw_scene)

    # Enter the GLUT event processing loop
    glutMainLoop()

if __name__ == "__main__":
    main()
