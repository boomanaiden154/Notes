# The Quadratic Formula

The quadratic formula is a very useful tool in algebra 1. It allows you to take any quadratic formula($ax^2 + bx + c$) and find its roots. Finding a quadratic formula's roots allows you to do all sorts of things such as find when a quadratic formula is equal to a certain number and is also important later on in subjects such as Calculus.

## The Formula

First off, lets define what a quadratic function is. A quadratic function is a function of the form

$$
f(x)=ax^2+bx+c
$$

In order for this equation to be a quadratic $a$,$b$, and $c$ need to be real numbers. The quadratic formula when graphed takes the form of a parabola that is either wider, more compact, and shifted up or down, left or right. Sometimes, we want to know the zeroes of the quadratic function or when the quadratic formula we are analyzing equals zero. One of the most versatile ways to do this is the quadratic formula. The quadratic formula looks like this:

$$
x = \frac{-b\pm\sqrt{b^2-4ac}}{2a}
$$

Sometimes this equation will have two real solutons, sometimes it will have one real solution, and sometimes it will have no real solutions. think about this graphically, if the quadratic formula has two solutions it intercepts the x-axis at two points. If it has one solution, it it intersects the x axis at one point, and if it has no solutions then it intersects the x axis at zero points.

## Deriving the formula

The quadratic formula can be derived fairly easily by completing the square(using variables in place of numbers). If we start off with the general form of a quadratic, $ax^2+bx+c$, when we solve for $x$ by completing the square, we will end up with the quadratic formula.

$$
ax^2+bx+c=0
$$

$$
x^2+\frac{b}{a}x=-\frac{c}{a}
$$

After we have taken $c$ off the left side and divided by $a$, we can then add $\left(\frac{b}{2}\right)^2$ on both sides, which allows us to easily factor the quadratic on the left hand side. 

$$
x^2+\frac{b}{a}x+\left(\frac{b}{2a}\right)^2=\left(\frac{b}{2a}\right)^2-\frac{c}{a}
$$

factoring the quadratic, we end up getting this equation:

$$
\left(x+\frac{b}{2a}\right)^2=\left(\frac{b}{2a}\right)^2-\frac{c}{a}
$$

Then we simplify the right hand side a little bit

$$
\left(x+\frac{b}{2a}\right)^2=\frac{b^2}{4a^2}-\frac{c}{a}
$$

Then we multiply $\frac{c}{a}$ by $4a$ so that we can have both fractions on the right hand side with the same denominator, and thhen we simplify

$$
\left(x+\frac{b}{2a}\right)^2=\frac{b^2}{4a^2}-\frac{4ac}{4a^2}
$$

$$
\left(x+\frac{b}{2a}\right)^2=\frac{b^2-4ac}{4a^2}
$$

Now, we can see some of the characteristics of the quadratic formula starting to come out. We can see the discriminant, $b^2-4ac$, and we can almost see the denominator, $2a$, but not quite. Next, we need to take the square root of both sides, and simplify.

$$
\sqrt{\left(x+\frac{b}{2a}\right)^2}=\sqrt{\frac{b^2-4ac}{4a^2}}
$$

$$
\left(x+\frac{b}{2a}\right)=\pm\frac{\sqrt{b^2-4ac}}{\sqrt{4a^2}}
$$

$$
x+\frac{b}{2a}=\pm\frac{\sqrt{b^2-4ac}}{2a}
$$

Now that we have taken the square root and simplified, we have a delightfully simple step in front of us. The fraction on the left hand side already has a denominator of $2a$, so all that we have to do is move it to the other side and simplify

$$
x=-\frac{b}{2a}\pm\frac{\sqrt{b^2-4ac}}{2a}
$$

$$
x=-\frac{b}{2a}\pm\frac{\sqrt{b^2-4ac}-b}{2a}
$$

And then rearranging this, we get the classic quadratic formula

$$
x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}
$$

## Finding the number of roots(The discriminant)

There is a simple formula to see how many different real roots a quadratic has. If we take a quadratic in standard form($ax^2+bx+c$), then the number of real roots is determined by the discriminant. The discriminant is simply the expression $b^2-4ac$. If the discriminant is greater than zero than the quadratic has two real roots, and if the discriminant is equal to zero then it has one real root, and if the discriminant is negative than there are no real solutions. The following formula shows this in mathematical notation:

$$
\begin{cases}
\text{0 real roots} & \text{if $b^2-4ac<0$} \\ 
\text{1 real root} & \text{if $b^2-4ac=0$} \\
\text{2 real roots} & \text{if $b^2-4ac>0$}
\end{cases}
$$

You may have noticed that the discriminant is the term under the radical in the quadratic formula. This is key to understanding how the discriminant determines the number of real roots that a quadratic has. You may have also noticed the $\pm$ term in front of the radical. This is important as well. If we are working with real number coefficients, we have the same three cases as before. The discriminant is negative, the discriminant is equal to zero, or the discriminant is positive. Lets look at how these three situations play out in the quadratic formula. If the discriminant is equal to a negative number, then simplification of the radical does not lead to real roots. We cannot simplify the quadratic formula any further(without getting into complex numbers). If the discriminant is equal to zero, then we only have one real root, because the $\pm$ operator in front of the radical also plays a key role in the number of solutions. Since anything plus zero, or anything minus zero is itself, we can simplify this out leaving us with one solution. If the discriminant is greater than zero, we get a positive real number upon simplification of the radical. When this is to the right of the $\pm$ term, we get two different real roots.

## The fundamental thereom of algebra and the complex conjugate thereom applied to quadratics

The fundamental thereom of algebra says that any polynomial has a number of roots(repeated, complex, or real) equal to the highest degree of any of its terms. For quadratics, this would mean that every quadratic will have two roots because the highest degree term in a standard form quadratic is $ax^2$. If a quadratic has to have two roots, why does it only have zero or one real solutions if the discriminant is less than or equal to zero? This is because of complex solutions. Complex roots for quadratics are obtained simply by plugging in all the numbers into the quadratic formula as you normally would, but then simplifying $i$, or the $\sqrt{-1}$ out of the radical. This will give you a complex solution(a number of the form $a+bi$). There is another thereom, called the complex conjugate thereom, that states all complex solutions to polynomials must be in pairs. This is consistent for when the discriminant is less than zero, because then both solutions to the quadratic are complex, but what if the discriminant is equal to zero? If one solution is real, then the other root can't be complex because complex solutions have to come in pairs. The other option is a repeated solution. Repeated roots in quadratics occur when we multiply two linear polynomials together that have the same solution. Algebraically, combining two linear polynomialroot quadratic would look like this:

$$
(x-a)^2=(x-a)(x-a)
$$

$$
x^2-2ax+a^2
$$

This is the generalized form for a perfect square trinomial. When we take two polynomials and multiply them together, the resulting polynomial inherits all of the roots of the polynomials making it up. This helps to explain why a quadratic that only has one real root satisfies the fundamental thereom of algebra. It inherits the two roots from the two factors composing it. This is a special case though because the two solutions from the two factors are actually the same. When this occurs, we say that the resulting polynomial has a root or solution with a rootcity of however many repeat roots it has. With the example above, we can say that the polynomial has a root at $a$ with a multiplicity of two, because the two factors composing it both have a root at $a$.
