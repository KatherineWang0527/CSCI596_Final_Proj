# CSCI596_Final_Proj
USC CSCI596 final project in 2023fall 


## A Real openGL Application on shaders

### Objective:

Researching shaders in the context of OpenGL involves exploring and implementing techniques to achieve visual effects that enhance the realism, aesthetics, or specific characteristics of rendered objects or scenes.

We are conducting research on shader-based processing of objects using OpenGL. Our project focuses on shader processing for both 2D and 3D objects, employing a teapot as the subject for 2D and a monkey model for 3D

1. Teapot shading 
Steps:
Model Preparation:

Create detailed 2D models (in image format, e.g., PNG or JPEG) representing a tower and a house.

Shader Development:

Write fragment shaders to handle texture mapping, coloring, and any additional effects (e.g., shadows, outlines).
Develop vertex shaders to handle transformations, although, in a 2D context, these might be minimal.

OpenGL Environment Setup:

Initialize GLFW, create an OpenGL window and set up a rendering context.

Shader Integration:

Apply shaders to handle texture mapping, color application, and any additional effects to the 2D models.

Model Loading and Rendering:

Load tower and house images as textures into the OpenGL application.
Render the 2D models on the screen by mapping the textures to appropriate geometry (e.g., rectangles).

### Handling Interaction:

Implement user interaction (e.g., mouse or keyboard input) to manipulate or animate the rendered 2D models.

### How to implement: 
I created prog_hdlr handler and linked the source code of shaders: first, we read the text files, then we compile it on-the-fly and then link to the program handler.

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

If the intensity is greater than 0.95, it's set to 1.
If the intensity is between 0.5 and 0.95, it's set to 0.6.
If the intensity is between 0.25 and 0.5, it's set to 0.4.
If the intensity is below 0.25, it's set to 0.2.

(4) gl_FragColor = gl_Color * intensity;

Finally, sets the color of the fragment (gl_FragColor) by multiplying the base color (gl_Color) by the computed intensity.

Effect:
before:

![image](https://github.com/KatherineWang0527/CSCI596_Final_Proj/assets/62502208/4e2eb437-00aa-4cce-9019-75c3ac643f03)


After:

![image](https://github.com/KatherineWang0527/CSCI596_Final_Proj/assets/62502208/86542a87-1a35-4495-80d2-00f12b813534)

 


2. 3D models shadering application

Key points:
        (1) Being more bright when closer to a light source
        (2) Having highlights when looking at the reflection of a light (specular lighting)
        (3) Being darker when light is not directly towards the model (diffuse lighting)
        (4) Cheating a lot (ambient lighting)

### More Details about the key points
### (1) The Diffuse part
The importance of the surface normal
When light hits an object, an important fraction of it is reflected in all directions. This is the “diffuse component”. When a certain flux of light arrives at the surface, this surface is illuminated differently according to the angle at which the light arrives.

If the light is perpendicular to the surface, it is concentrated on a small surface. If it arrives at a gazing angle, the same quantity of light spreads on a greater surface :

<img width="581" alt="Screen Shot 2023-11-29 at 07 29 20" src="https://github.com/KatherineWang0527/CSCI596_Final_Proj/assets/89505559/c2324747-38b5-4650-868c-916747f0b98a">


### (2) Material Color
The output color also depends on the color of the material. In this image, the white light is made out of green, red and blue light. When colliding with the red material, green and blue light is absorbed, and only the red remains.
<img width="474" alt="Screen Shot 2023-11-29 at 07 29 57" src="https://github.com/KatherineWang0527/CSCI596_Final_Proj/assets/89505559/fd3b0d0c-1ed6-4562-8725-16bd3fb40dc3">


### (3) Together
We need a handful of parameters (the various colors and powers) and some more code.

MaterialDiffuseColor is simply fetched from the texture.

LightColor and LightPower are set in the shader through GLSL uniforms.


### Steps:

### Model Loading:

Utilize a 3D modeling software (Blender, Maya, etc.) to create detailed models of a monkey face.
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

### Effect:

<img width="829" alt="Screen Shot 2023-11-29 at 07 30 59" src="https://github.com/KatherineWang0527/CSCI596_Final_Proj/assets/89505559/96c058c2-eba5-498b-9d2a-1fba0a2d235f">

<img width="773" alt="Screen Shot 2023-11-21 at 21 59 39" src="https://github.com/KatherineWang0527/CSCI596_Final_Proj/assets/89505559/4c5e64ea-e1c0-422f-bf2f-890f34ad0e24">


### Challenges:
Shader Complexity: While working in a 2D/3D space, achieving certain effects like shadows or complex lighting might require advanced shader logic.

Texture Handling: Efficiently managing and mapping textures to geometry, especially with large or detailed images.
