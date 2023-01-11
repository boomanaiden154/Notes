# Physcis Lecture 2 01/11/2023

* HW1 will be out tonight, due next Wednesday
* Review of position/velocity/acceleration definitions
  * $$x(t)$$
  * $$v(t)=\frac{d}{dt}x(t)$$
  * $$a(t)=\frac{d}{dt}v(t)$$
* Definition position
  * We need reference
  * We need direction
* Particle
  * Something that doesn't have any dimensions, can be referred to with a point
* Focus is on particle/particle motion for now rather than looking at extended
objects
* Further review of position/velocity/acceleration definitions
  * $$x(t)=\int_{0}^{t}v(t)\,dt+x(0)$$
  * $$v(t)=\int_{0}^{t}a(t)\,dt+v(0)$$
  * We can really do this with any point where we know the value of the
  function, not just at zero.
* Free fall
  * $$a(t)=g$$
  * $$v(t)=\int_{0}^{t}g\,dt+v(0)=gt+v_0$$
  * Notation note: $v(0)=v_0$, same for $x(0)$ and $a(0)$.
  * $$x(t)=\int_{0}^{t}gt\,dt+\int_{0}^{t}v_0t+x_0=\frac{1}{2}gt^2+v_0t+x_0$$
  * Within this class $g=-10\frac{\text{meters}}{\text{second}^2}$ unless
  otherwise specified.
* Vectors
  * The way to specify any arbitrary coordinate
  * Each individual scalar that composes the vector represent the distance from
  the origin in a specific direction (along an axis)(better shown visually)
  * Let's define a vector in a vector space:
    * Define addition
      * $$\vec{v_1}+\vec{v_2}=\vec{v_3}$$
      * $$\vec{0}+\vec{v_1}=\vec{v_1}$$
      * $$-\vec{v_1}+\vec{v_1}=\vec{0}$$
    * Define scalar multiplication
      * $$a \times \vec{v_1}=a\vec{v_1}$$
      * $$1 \times \vec{v_1}=\vec{v_1}$$
      * $$-1 \times \vec{v_1}=-\vec{v_1}$$
  * Vector space obeys these rules?
  * Vector space we are cosndiering:
  $\mathbb{R}^3=\mathbb{R}\times\mathbb{R}\times\mathbb{R}$
  * Addition is component wise
    * $(a_1,b_1,c_1)+(a_2,b_2,c_2)=(a_1+b_1,a_2+b_2,c_1+c_2)$
    * This new vector is also a vector in $\mathbb{R}^3$.
  * (0,0,0) is the zero vector
  * The inverse vector of $(a,b,c)$ is $(-a,-b,-c)$
  * $\mathbb{R}$ is something we can visualize and perform geometric
  manipulations on
  * We draw the vectors as lines from an origin to to the point that they
  represent.
  * We're using free vectors within this class. IE if we move the vector around
  to a different origin, we're perfectly fine.
  * Projection is also pretty important. The length of the vector in the
  directio of another vector is the project of that vector.
  * The length of the line representing the vector is the magnitude.
    * $$\left|\vec{v}\right|=\sqrt{a^2+b^2+c^2}$$
    * This is the notation/definition of the magitude
    * Proving this is a pretty easy extension of the pythagorean theorem in
    3D.
  * Standard notation for vectors in this class is $(a,b,c)$, but writing it
  out in component form as $a\hat{i}+b\hat{j}+c\hat{k}$ is also fine.
  * We can rewrite a vector as a unit vector multipled by its component
    * $$\sqrt{a^2+b^2+c^2}\left(\frac{(a,b,c)}{\sqrt{a^2+b^2+c62}}\right)$$
    * The left side is the scalar portion and the right side is the vector
    portion.
  * We can fairly easily prove that a vector divided point wise by its
  magnitude ends up being a unit vector. Just plug into the formulas and
  simplify.
  * $\vec{v}$ is the notation for a standard vector
  * $\hat{v}$ is the notation for a unit vector
  * Inner product/dot product/scalar product of two vectors
    * The inner product is defined as
    $(a,b,c)\cdot(a_2,b_2,c_2)=a_2a+b_2b+c_2c$
    * The alternative definition using some intuition from geometry is
    $\vec{v_1}\cdot\vec{v_2}=\left|\vec{v_1}\right|\left|\vec{v_2}\right|\cos{\theta}$
    * Proof involves just drawing everything out and using the law of cosines.