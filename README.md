# TrigEvaluationEquationGenerator

### This project intends to create unique trigonometric equations that vary with degree and radian values. 

## "Customization"

##### To change window size:
> ``root.geometry("480x260")`` 
> The first number indicates width, second indicates the height

##### Allow the window to be resized:
> ``root.resizable(width=False, height=False)``
> Change False to True

##### Add/Remove functions or angles:
> The lists ``functions``, ``deg_angles``, and ``rad_angles`` contain the function, angle values, and radian values respectively which can be changed or left as is.

##### Changing font:
> ``app= appWindow(root, appFont, equationFont)``
> The default font is Courier for the equation, and Arial for the buttons/labels. However they can be overidden by passing in another font in the app initialization. (You need to have the font installed on your machine for this to work)

