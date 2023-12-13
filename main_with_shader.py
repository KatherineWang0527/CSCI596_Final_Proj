from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Vertex shader
vertex_shader = """
#version 120
varying vec3 normal;
varying vec3 fragPosition;

void main() {
    fragPosition = vec3(gl_ModelViewMatrix * gl_Vertex);
    normal = gl_NormalMatrix * gl_Normal;
    gl_Position = gl_ModelViewProjectionMatrix * gl_Vertex;
}
"""

# Fragment shader
fragment_shader = """
#version 120
varying vec3 normal;
varying vec3 fragPosition;

void main() {
    vec3 lightPos = vec3(5.0, 5.0, 5.0);
    vec3 lightColor = vec3(1.0, 1.0, 1.0);
    vec3 objectColor = vec3(1.0, 0.0, 0.0); // Red color

    // Ambient lighting
    float ambientStrength = 0.1;
    vec3 ambient = ambientStrength * lightColor;

    // Diffuse lighting
    vec3 norm = normalize(normal);
    vec3 lightDir = normalize(lightPos - fragPosition);
    float diff = max(dot(norm, lightDir), 0.0);
    vec3 diffuse = diff * lightColor;

    // Combine results
    vec3 result = (ambient + diffuse) * objectColor;
    gl_FragColor = vec4(result, 1.0);
}
"""

def compile_shader(source, shader_type):
    shader = glCreateShader(shader_type)
    glShaderSource(shader, source)
    glCompileShader(shader)
    if glGetShaderiv(shader, GL_COMPILE_STATUS) != GL_TRUE:
        raise RuntimeError(glGetShaderInfoLog(shader))
    return shader

# def compile_shader(source, shader_type):
#     shader = glCreateShader(shader_type)
#     glShaderSource(shader, source)
#     glCompileShader(shader)
#     if glGetShaderiv(shader, GL_COMPILE_STATUS) != GL_TRUE:
#         raise RuntimeError(glGetShaderInfoLog(shader))
#     return shader

def setup_shader_program():
    global shader_program
    shader_program = glCreateProgram()
    vertex = compile_shader(vertex_shader, GL_VERTEX_SHADER)
    fragment = compile_shader(fragment_shader, GL_FRAGMENT_SHADER)
    glAttachShader(shader_program, vertex)
    glAttachShader(shader_program, fragment)
    glLinkProgram(shader_program)
    if glGetProgramiv(shader_program, GL_LINK_STATUS) != GL_TRUE:
        raise RuntimeError(glGetProgramInfoLog(shader_program))

def draw_scene():
    global shader_program
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    # Simple camera setup
    gluLookAt(0.0, 0.0, 3.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)

    glUseProgram(shader_program)

    # Draw the teapot
    glutSolidTeapot(1.0)

    glutSwapBuffers()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(640, 480)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"OpenGL Teapot")

    glEnable(GL_DEPTH_TEST)
    glClearColor(0.1, 0.1, 0.1, 1.0)

    setup_shader_program()
    glutDisplayFunc(draw_scene)

    glMatrixMode(GL_PROJECTION)
    gluPerspective(45, 640/480, 0.1, 50.0)
    glMatrixMode(GL_MODELVIEW)

    glutMainLoop()

if __name__ == "__main__":
    main()
