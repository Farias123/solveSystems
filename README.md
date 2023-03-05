# solveSystems

This program solves a two equation linear system, using the Gauss Jordan method for array resolution(scaling). By the end of the program execution(if the linear system inputed is possible and determinate), the scaled array will be printed. For this program, were implemented classes, methods and functions.

## getCoef function
The getCoef function receives two parameters, the first is the equation, and the second is the definer, wether "X","Y" or "Indep"(Independent term).

If the definer is "X" the function will go through the characters of the equation and take each one until it gets to x, then the function will return the coeficient that multiplies X.

If the definer is "Y" the function will go through the characters of the equation after the plus sign and take each one until it gets to y, then the function will return the coeficient that multiplies Y.

If the definer is "Indep" the function will go through the characters of the equation after the equal sign and take each one until it gets to the end of the equation, then the function will return the independent term's value.

# Array class
This class will use the array that will be created with the terms obtained from the equation(scalars and independent), to calculate the value of X and Y using methods.

## scale method
This method is for scaling 2X3 arrays, where its representation would be:
[A B C], where the system's in this format: {Ax + By = C
[D E F]									    {Dx + Ey = F

The first step to scale the array is to zero the first term of the second line, subtracting on second line, the first line multiplied by D/A, this way D will be reduced to zero.

The next step is to pass the term E dividing on the right side, so we stay with E equal to 1, i.e. 0x + 1y = F, so F is the value of y.

Now we will zero the second term of the first line, we will subtract on the first line, the second line multiplied by B, this way B now will be reduced to zero.

On this step, on the first line we will pass A dividing on the right side, so we stay with A equal to 1, i.e. 1x + 0y = C, so C is the value of x.

All done, our array is scaled.

The other methods, getXValue and getYValue, only use the scale method and take by the end of it the value of C and F respectively.

## Exceptions
By the end of the code there are 2 exceptions:

The first one was created for when a Zero Division Error happens on the array scaling, which means that the proportion between X and Y multipliers is the same. If this happens it means the system is not possible and determinate. 

The second exception was created for, if on the second equation, the X multiplier or the independent term are qual to zero, the Zero Division Error won't happen.


## Input examples
Ex1.:
2.0x + -4.0y = 10.0
4.0x + -5.0y = 6.0

Ex2.:
2x + 4y = 12
4x + 5y = 6

## Output examples
Ex1.:
The X value is: -4.333333333333334 
And the Y value is: -4.666666666666667
The scaled array is:
 [1, 0, -4.333333333333334] 
 [0, 1, -4.666666666666667]

Ex2.:
The X value is: -6.0 
And the Y value is: 6.0
The scaled array is:
 [1, 0, -6.0] 
 [0, 1, 6.0]