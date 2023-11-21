# CSCI596_Final_Proj
USC CSCI596 final project in 2023fall 


## A Real openGL Application on shaders

### Objective:

Researching shaders in the context of OpenGL involves exploring and implementing techniques to achieve visual effects that enhance the realism, aesthetics, or specific characteristics of rendered objects or scenes.


1. Teapot shading 
Steps:
Model Preparation:

Create detailed 2D models (in image format, e.g., PNG or JPEG) representing a tower and a house.

Shader Development:

Write fragment shaders to handle texture mapping, coloring, and any additional effects (e.g., shadows, outlines).
Develop vertex shaders to handle transformations, although in a 2D context, these might be minimal.

OpenGL Environment Setup:

Initialize GLFW, create an OpenGL window, and set up a rendering context.

Shader Integration:

Apply shaders to handle texture mapping, color application, and any additional effects to the 2D models.

Model Loading and Rendering:

Load tower and house images as textures into the OpenGL application.
Render the 2D models on the screen by mapping the textures to appropriate geometry (e.g., rectangles).

### Handling Interaction:

Implement user interaction (e.g., mouse or keyboard input) to manipulate or animate the rendered 2D models.

### How to implement: 
I created prog_hdlr handler and linked the source code of shaders: first we read the text files, then we compile it on-the-fly and then link to the program handler.

### Shader Logic:
(1) vec3 l = normalize(gl_LightSource[0].position.xyz);

Firstly, calculates a normalized vector l representing the normalized position of the light source. It uses the position of the first light source available in the scene.

(2) float intensity = .2 + max(dot(l, normalize(n)), 0.0);

the shader calculates the intensity of the light hitting the fragment. It uses the dot product between the normalized light vector (l) and the normalized surface normal vector (n). This value is clamped between 0 and 1 using max(..., 0.0) and adjusted by 0.2 to set a base intensity.

(3) The subsequent if-else statements modify the intensity based on its value range:
if (intensity > 0.95)
        intensity = 1;
    else if (intensity > 0.5)
        intensity = .6;
    else if (intensity > 0.25)
        intensity = .4;
    else
        intensity = .2;

If intensity is greater than 0.95, it's set to 1.
If intensity is between 0.5 and 0.95, it's set to 0.6.
If intensity is between 0.25 and 0.5, it's set to 0.4.
If intensity is below 0.25, it's set to 0.2.

(4) gl_FragColor = gl_Color * intensity;

Finally, sets the color of the fragment (gl_FragColor) by multiplying the base color (gl_Color) by the computed intensity.

Effect:
before:

<img width="338" alt="image" src="https://github.com/KatherineWang0527/CSCI596_Final_Proj/assets/62502208/d3038e54-8777-41f9-b198-250ba3b21208">

 

After:

<img width="341" alt="image" src="https://github.com/KatherineWang0527/CSCI596_Final_Proj/assets/62502208/24d3205a-7083-42dd-a5bb-e0e10cf47661">

 


2. 3D models shadering application

Steps:

### Model Loading:

Utilize a 3D modeling software (Blender, Maya, etc.) to create detailed models of a tower and a house.
Export these models into a format that can be loaded into the OpenGL application (e.g., OBJ, FBX).

### Shader Development:

Write vertex and fragment shaders to handle lighting, materials, and any additional effects (such as reflections or shadows).
Implement shader logic for diffuse lighting, specular highlights, and potentially ambient occlusion or other advanced effects.

### OpenGL Environment Setup:

Initialize GLFW, create an OpenGL window, and set up a rendering context.
Load the tower and house 3D models into the application.

### Shader Integration:

Integrate the shaders into the rendering pipeline, specifying how the shaders interact with the model's geometry and materials.
Apply different shader effects to different parts of the models (e.g., different materials for walls, roofs, windows).

### Camera and View Setup:

Implement a camera system to navigate around the scene and view the tower and house from different angles.
Set up projection and view matrices to control the perspective and view of the models.

### Rendering Loop:

Create a rendering loop to continuously render the scene, updating the camera position and handling user input for interaction.
Optimization and Performance:

Optimize shaders and rendering techniques for smooth performance, especially with complex models and shader effects.


### Challenges:
Shader Complexity: While working in a 2D/3D space, achieving certain effects like shadows or complex lighting might require advanced shader logic.

Texture Handling: Efficiently managing and mapping textures to geometry, especially with large or detailed images.
![image](https://github.com/KatherineWang0527/CSCI596_Final_Proj/assets/62502208/128cab68-ae94-40ca-82ce-c4f48b3ffd6e)
