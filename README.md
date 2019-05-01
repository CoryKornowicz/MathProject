# MathProject
A python app to evaluate functions in terms of Taylor and Maclaurin Series 

This project requires the following Python Dependencies to run:

SymPy [sudo pip3 install sympy]
NumPy [sudo pip3 install numpy] 
Matplotlib [sudo pip3 install matplotlib]
PySide2 [sudo pip3 install PySide2]

The project is a zipped PyCharm Project so you could run the main.py file from the command line to load the project or you could import it into PyCharm if you want to analyze the code more. 

The interface is designed in a way to not clutter the output. For the ranges to display, this pertains to the graph that is generated. The range that is input will display those equations on the graph as well as the original function every time. The box for how many iterations will calculate that many iterations of the Taylor Series. Usually, the number of iterations to perform will be the same number as the max iterations to display. The two input fields on the left hand side are for the x-offset to be added to the x of the function (typically referred to the form of (x-a)). If you input an offset of 0, it will perfrom Maclaurin Series, otherwise they will be Taylor Series. The iterate by box if meant to define how the user wants to iterate through the Taylor Series by. This is particularly useful for the trigonometric functions. 

Lastly, the function box is left to be filled in. It takes in a LaTeX formatted string for the equation. One of the websites I used to test LaTeX functions is [LaTeX Calculator]:https://www.codecogs.com/latex/eqneditor.php
This makes it super easy to build any trigonometric function, or equation. 

However, it isn't without its limitations. For example, e^x is not displayed particularly well in the LaTeX generator, as well as it isn't recognized natively in SymPy. It would need its own wrapper function to handle its exception case. Sometimes it will show an expansion at n =1, but the graph will not be plotted. 

I do plan to update it for handling e^x equations at some point, but with the respect to finals in mind, it will have to wait until afterwards. I hope you enjoy the first iteration of the project, Dr. Gratton!
