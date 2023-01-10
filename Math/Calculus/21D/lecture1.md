# Lecture 1 1/9/23

* Class is focused on generalizing the fundamental theorem of Calculus to
  more than one variable.
* Three generalizations of the derivative to functions involving more than
  one variable.
  * The Gradient
  * Divergence
  * Curl
* Each of these have an associated equivalent of the fundamental theorem.
* Course Organization
  * Text: Thomas Calculus (Specifically the 11th edition is what will be taught
  out of, although some notes seem to have been made to adjust for changes)
  * Class website: [here](https://math.ucdavis.edu/~temple/MAT21D)
  * Office hours: WF 2:15-4:50 (right before class)
  * Thursday discussion sections
  * Grading
    * Midterms - 100pts each (2)
      * Midterm I Friday, Feb 3
      * Midterm II Friday, Mar 10
  * Homework problems are on the syllabus
  * Quizzes in the discussion sections based on the HW problems are given in
  discussion sections.
  * HW Quiz grades are used to bump/drop grades that are borderline cases,
  otherwise they don't make that much of a difference.
* Maxwell's equations are much more useful/beautiful when written in terms of
  gradient/curl/divergence.
* Lead TA is working on the canvas page, will be up soon
* Exams will be somwhat similar to the homework, also based on the lecture
* All prior midterms and finals are on Temple's website as listed above.
* Vector calculus is the theory of Calculus for functions of more than one
  variable.
* Viewing formula as functions makes them easier to describe
  * $y=x^2\implies\text{parabola}$
  * View as a function
    $y=f(x)=x^2$
  * We can use the notation to describe tangent lines:
    $$m=\lim_{\Delta x\to0}\frac{f(x+\Delta x) - f(x)}{\Delta x}
    =\frac{\Delta y}{\Delta x}=f'(x)$$
* Fundamental theorem of Calculus
  * Area problem
  * $$\text{area} = \int_{a}^{b}f(x)dx=F(b)-F(a)$$
  * $$F'(x)=f(x)$$
* Now, let's look at a function of more than one variable:
  * $w=f(x,y,z)$
  * input $(x,y,z)$ is a coordinate in three dimensional space
  * If output is a scalar we call this a scalar valued function
    of a vector.
  * If $w=<w_1,w_2,w_3>$, we call this a vector valued function
    of a vector or a vector field.
* As mentioned before there are three generalizations of the derivtive for
  vectors:
  * The gradient($\nabla$)
  * The divergence
  * The curl
* The gradient:
  * $$\nabla f = (\frac{\partial f}{\partial x},
    \frac{\partial f}{\partial y},
    \frac{\partial f}{\partial z})$$
  * We can also view this as the dot product of the gradient operator and the
    function itself:
    * $$\nabla=(\frac{\partial}{\partial x},
      \frac{\partial}{\partial y},
      \frac{\partial}{\partial z})$$
    * $$\nabla \cdot f=\text{same as the above}$$
* The divergence:
  * $$\text{Div}\vec{F}=M_x+N_y+P_z$$
  * $$\vec{F}(x,y,z)=(M(x,y,z),N(x,y,z),P(x,y,z))$$
  * $$M_x=\frac{\partial M}{\partial x}(x,y,z)$$
  * $$N_x=\frac{\partial N}{\partial y}(x,y,z)$$
  * $$P_x=\frac{\partial P}{\partial z}(x,y,z)$$
* The curl:
  * The cross product
  * $$\text{Curl}\vec{F}=\nabla \times \vec{F}
  * Usually computed like other cross products with the determinant of a
    constructed matrix.
* Each of these has a fundamental theorem of Calculus
  * Eg the line integral