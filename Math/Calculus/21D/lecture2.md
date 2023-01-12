# 21D Lecture II 1/11/2023

* Quite a bit of stuff seems to have been repeated from the first lecture,
still repeating it here so maybe I remember it better.
* Introduction
  * Vector Calculus is Calculus for functions of more than one variable
  * Suppose $w=f(x,y,z)$
    * $(x,y,z)\in\mathbb{R}^3$
    * If the output is a scalar, $w\in\mathbb{R}$
      * In this case we can also say this is a scalar valued function.
    * Normally treating points/vectors pretty similarly and using whichever
    one is nicer for the particular problem we're working on.
    * For a scalar valued function, we can say $f:\mathbb{R}^3\to\mathbb{R}$
    * If the output is a vector, $\vec{F}:\mathbb{R}^3\to\mathbb{R}^3$
      * We can also use the following notation for the function:
      $$\vec{F}(x,y,z)=\overrightarrow{(M(x,y,z),N(x,y,z),P(x,y,z))}$$
  * Notation
    * $$\frac{\partial}{\partial x}f=\partial_xf=f_x$$
    * All are partial derivatives
  * The three first order linear differential operators:
    * The gradient
      * $$\nabla=(\frac{\partial}{\partial x},\frac{\partial}{\partial y},\frac{\partial}{\partial z})$$
      * $$\nabla f(x,y,z)=(\partial_xf,\partial_yf,\partial_zf)$$
      * Gradient "Del"
      * Maps $\mathbb{R}^3$ to $\mathbb{R}^3$ or in other terms
      $\nabla f: \mathbb{R}^3 \to \mathbb{R}^3$
    * Divergence
      * $$\text{div}\,\vec{F}=\left(\frac{\partial M}{\partial x},\frac{\partial N}{\partial y},\frac{\partial P}{\partial Z}\right)$$
      * $=M_x+N_y+P_z$
      * Maps $\mathbb{R}^3$ to $\mathbb{R}$$ or in other terms
      $\text{div}\,\vec{F}:\mathbb{R}^3\to\mathbb{R}$
    * Curl
      * $$\text{curl}\,\vec{F}=(P_y-N_z,M_z-P_x,N_x-M_y)$$
      * The determinant of the matrix composed exactly the same as the cross
      product.
      * Maps $\mathbb{R}^3$ to $\mathbb{R}^3$ or in other terms
      $\nabla f: \mathbb{R}^3 \to \mathbb{R}^3$
  * Goal of the class
    * Each of the linear differential operators listed above, the gradient,
    divergence, and curl has a fundamental theorem of Calculus associated
    with it
    * Gradient - line integral
      * $$\int\limits_{C}\overrightarrow{\nabla f}\cdot\vec{T}\,ds=f(B)-f(A)$$
      * Integrating over the curve $C$
      * The line integral of the gradient of a scalar valued function along a
      curve is equal to the change in between the bounds
      * Equivalent to conservation of energy. Also has something to do with
      work.
    * Divergence Theorem
      * Let's say we have a volume $V$ and a normal vector on that volume,
      $\vec{n}$
      * $$\iiint\limits_{V}\text{div}\,\vec{F}\,dv=\iint\limits_{S}\vec{F}\cdot\vec{n}\,dA$$
      * The integral of the divergence of f $\text{div}\vec{F}$ over a three
      dimensional volume is equivalent to the flux of $\vec{F}$ through
      boundary $S$.
      $$\text{div}\,\vec{F}=\frac{\text{flux}}{\text{volt}}$$
    * The FTC goes with curl
      * Two dimensional surface $S$ with boundary curve around it $C$ and
      normal on the curve $\vec{n}$
      * $$\iint\limits_{S}\text{curl}\,\vec{F}\cdot\vec{n}\,dA=\int\limits_{C}\vec{F}\cdot\vec{T}\,ds$$
      * The integral of curl $\vec{F}$ over a 2D surface $S$ equals the circulation
      in $\vec{F}$ around the boundary curve $C$.
      * Curl of $\vec{F}$ is a measure of circulation per area.
  * If we want to integrate over a volume: $$\iiint\limits_{V}f(x,y,z)\,dV$$
  * Surface integral - integrating over a 3D surface, $S$: 
  $$\iint\limits_{S}f\,dA$$
  * Line Integral - Integration a function on a line/curve $C$:
  $$\int\limits_{C}\vec{F}\cdot\vec{T}\,ds$$
* 15.1 - Multiple Integrals
  * Let's suppose $z=f(x,y)$ and $R$ is a region in the XY plane.
  * The volume under the function $f$ over the region $R$ is represented by
  the following:
  $$\iint\limits_{R}f(x,y)\,dA$$
  * To evaluate use the slice method
  * Let's take $R$ to be a rectangle in the $XY$ plane with sides parallel to
  the axises.
    * Define $R$ to have the following limitations: $0\le x\le a$ and
    $0 \le y \le b$
  * $$V = \sum A(X)\Delta x$$
    * Represent the volume as composed by a bunch of slices through the volume
    perpendicular to the x-axis.
  * If we take the above and let $\Delta x$ go to zero, we get the following:
    * $$\int_{0}^{a}A(x)dx=\int_{0}^{a}\int_{0}^{b}f(x,y)\,dy\,dx$$