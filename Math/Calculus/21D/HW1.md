# 21D HW1

This HW set after the first lecture consisted of the following problems from
section 15.1 of Thomas' Calculus: 1,2,4,5,7,9,13,21,23,38. I used the 14th
edition of the textbook in contrast to the official version for the course
being the 11th, so some things might not match up perfectly.

#### Problem 1

Evaluate the following iterated integral:
$$\int_{1}^{2}\int_{0}^{4}2xy\,dy\,dx$$
Let's start off by evaluting the inner integral:
$$\int_{0}^{4}2xy\,dy=2x\int_{0}^{4}y\,dy=
2x\left( \left. \frac{y^2}{2} \right|_{0}^{4} \right)$$
$$= 2x\left( \frac{16-0}{2}\right)=2x\cdot 8=16x$$
Now we need to plug this back into the outer integral:
$$\int_{1}^{2}16x\,dx=\left. 8x^2 \right|_{1}^{2}=32-8=24$$
This gives our final answer, $24$.

#### Problem 2

Evaluate the following iterated integral:
$$\int_{0}^{2}\int_{-1}^{1}(x-y)\,dy\,dx$$
Start off by evaluating the inner integral:
$$\int_{-1}^{1}(x-y)\,dy=\left. \left( xy - \frac{1}{2}y^2\right) 
\right|_{-1}^{1}$$
$$= \left( x - \frac{1}{2} + x + \frac{1}{2}\right) = 2x$$
Now we need to evalute the outer integral:
$$\int_{0}^{2}2x\,dx=\left. \left( x^2 \right) \right|_{0}^{2}=4$$

#### Problem 4

Evaluate the following iterated integral:
$$\int_{0}^{1}\int_{0}^{1}\left(1-\frac{x^2+y^2}{2}\right)\,dx\,dy$$
Again, start off by evaluating the inner integral:
$$\int_{0}^{1}\left(1-\frac{x^2+y^2}{2}\right)\,dx
=\int_{0}^{1}\left(1-\frac{1}{2}x^2=\frac{1}{2}y^2\right)\,dx$$
$$=\left.\left( x-\frac{1}{6}x^3-\frac{1}{2}y^2x\right)\right|_{0}^{1}$$
$$=1-\frac{1}{6}-\frac{1}{2}y^2-(0-0+0)=\frac{5}{6}-\frac{1}{2}y^2$$
Now putting this into the outer integral:
$$\int_{0}^{1}\left(\frac{5}{6}+\frac{1}{2}y^2\right)\,dy$$
$$=\left.\left(\frac{5}{6}y + \frac{1}{6}y^3\right)\right|_{0}^{1}
=\frac{5}{6}-{1}{6}=\frac{2}{3}$$

#### Problem 7

Evaluate the following iterated integral:
$$\int_{0}^{1}\int_{0}^{1}\frac{y}{1+xy}\,dx\,dy$$
Again, start off by evaluating the inner integral:
$$\int_{0}^{1}\frac{y}{1+xy}\,dx$$
Let's do a u-substitution setting $u=1+xy$, which makes $du=y\,dx$ and
$dx=\frac{du}{y}$. Recomputing the lower bound we get $1+0*y=1$ for the lower
bound and $1+1*y=1+y$ for the upper bound. This yields the following:
$$\int_{1}^{1+y}\frac{y}{u}\cdot\frac{du}{y} = \int_{1}^{1+y}\frac{1}{u}\,du$$
$$=\left.\log{u}\right|_{1}^{1+y}=\log{1+y}$$
Plugging this into the outer integral, we get the following:
$$\int_{0}^{1}\log{(1+y)}\,dy$$
Doing another u-substitution, setting $u=1+y$ yields $du=1dx=dx$, makes the
lower bound $0+1=1$ and the upper bound $1+1=2$, which gives us the following
integral:
$$\int_{1}^{2}\log{u}du$$
Taking advantage of the fact that
$$\int \log{x}=x(\log{x}-1)+C$$
We can then finish the problem:
$$\int_{1}^{2}\log{u}du=u\left.\left( \log{u}-1\right)\right|_{1}^{2}$$
$$=2(\log{2}-1)-1(\log{1}-1)=2\log{2}-2+1=2\log{2}-1=\log{4}-1$$

#### Problem 9

Evaluate the following iterated integral:
$$\int_{0}^{\log{2}}\int_{1}^{\log{5}}e^{2x+y}\,dy\,dx$$
We start by evaluating the inner integral:
$$\int_{1}^{\log{5}}e^{2x+y}\,dy\,dx$$
Factoring out some constants and then simplifying:
$$e^{2x}\int_{1}^{\log{5}}e^{y}dy=e^{2x}\left.\left(e^y\right)
\right|_{1}^{\log{5}}$$
$$=5e^{2x}-e^{2x+1}$$
Now we can plug this into the outer integral:
$$\int_{2}^{\log{2}}5e^{2x}-e^{2x+1}\,dx$$
I found it helpful to split the integral and do a u-substitution on the two
parts. Working on the first part:
$$\int_{0}^{\log{2}}5e^{2x}dx$$
Setting $u=2x$ gives $du=2\,dx$ and $dx=\frac{du}{2}$, and the lower bound
changes to $0*2=0$ and the upper bound changes to $2*\log{2}=2\log{2}$,
which yields the following integral:
$$\int_{0}^{2\log{2}}\frac{5e^u}{2}\,du=\frac{5}{2}\int_{0}^{2\log{2}}e^udu$$
$$=\frac{5}{2}\left(\left.e^u\right|_{0}^{2\log{2}}\right)
=\frac{5}{2}(4-1)=\frac{15}{2}$$
Then for the other part of the outer integral:
$$\int_{0}^{\log{2}}e^{2x+1}\,dx$$
We again do a u-subsitution, setting $u=2x+1$ which gives $du=2\,dx$,
$dx=\frac{du}{2}$, the lower bound as $2*0+1=1$, and the upper bound as
$2*\log{2}+1=2\log{2}+1$. This yields the following integral:
$$\int_{1}^{2\log{2}+1}e^u\,\frac{du}{2}$$
Solving:
$$\frac{1}{2}\int_{1}^{2\log{2}+1}e^udu=\frac{1}{2}
\left(\left.e^u\right|_{1}^{2\log{2}+1}\right)$$
$$=\frac{1}{2}\left(e^{2\log{2}+1}-e^1\right)-\frac{1}{2}(4e-e)=\frac{3e}{2}$$
Putting this all back together into the original outer integral:
$$\frac{15}{2}-\frac{3e}{2}$$
Or as the textbook puts it in the factored form:
$$\frac{3}{2}(5-e)$$

#### Problem 13

Solve the following iterated integral:
$$\int_{1}^{4}\int_{1}^{e}\frac{\log{x}}{xy}\,dx\,dy$$
Looking at the inner integral:
$$\int_{1}^{e}\frac{\log{x}{xy}}\,dx$$
We can see that a u-substitution and some factoring would help:
$$\frac{1}{y}\int_{1}^{e}\frac{\log{x}}{x}\,dx$$
With a u-substitution we set $u=\log{x}$, which makes $du=\frac{1}{x}dx$,
$dx = x\,du$, the lower bound $\log{1}=0$, and the upper bound $\log{e}=1$.
This gives the following integral:
$$\frac{1}{y}\int_{0}^{1}\frac{u}{x}x\,du=
\frac{1}{y}\int_{0}^{1}u\,du$$
Evaluating the integral gives:
$$\frac{1}{y}\left(\left.\frac{u^2}{2}\right|_{0}^{1}\right) =
\frac{1}{y}\left(\frac{1}{2}-\frac{0}{2}\right) = \frac{1}{2y}$$
Plugging this into the outer integral:
$$\int_{1}^{4}\frac{1}{2y}\,dy=\frac{1}{2}\int_{1}^{4}\frac{1}{y}\,dy$$
Evaluating:
$$\frac{1}{2}\left(\log{4}-\log{1}\right)=\frac{1}{2}\log{4}=
\frac{1}{2}(2\log(2))=\log{2}$$

#### Problem 21

Evaluating the following integral:
$$\iint_{R}e^{x-y}\,dA$$
Where $R$ is the region bounded by $0\le x\le\log{2}$ and $0\le y\le\log{2}$.
First let's setup the problem as a series of iterated integrals:
$$\int_{0}^{\log{2}}\int_{0}^{\log{2}}e^{x-y}\,dx\,dy$$
In this case it doesn't really matter in what order we iterate the integrals.
Solving the inner integral:
$$\int_{0}^{\log{2}}e^{x-y}\,dx=\frac{1}{e^y}\int_{0}^{\log{2}}e^xdx$$
$$=\frac{e^x|_{0}^{\log{2}}}{e^y}=\frac{1}{e^y}$$
Plugging into the outer integral:
$$\int_{0}^{\log{2}}e^{-y}\,dy=\left.-e^{-y}\right|_0^{\log{2}}
=-\frac{1}{2}+1=\frac{1}{2}$$

#### Problem 23

Evaluate the following double integral:
$$\iint_{R}\frac{xy^3}{x^2+1}dA$$
over the region R bounded by $0\le x\le 1$
and $0\le y\le 2$. Let's start by writing out the iterated integrals:
$$\int_{0}^{1}\int_{0}^{2}\frac{xy^3}{x^2+1}\,dy\,dx$$
Solving:
$$\frac{x}{x^2+1}\int_{0}^{2}y^3\,dy=\frac{x}{x^2+1}
\left(\left.\frac{y^4}{4}\right|_{0}^{2}\right)$$
$$=\frac{x}{x^2+1}(4)$$
Plugging this into the outer integral:
$$4\int_{0}^{1}\frac{x}{x^2+1}\,dx$$
Using a u-substitution with $u=x^2+1$ yields $du=2x\,dx$, $dx=\frac{du}{2x}$,
the lower bound as $0^2+1=1$, and the upper bound as $1^2+1=2$:
$$2\int_{1}^{2}\frac{1}{u}\,du=2\left(\left.\log{u}\right|_{1}^{2}\right)$$
$$=2(\log{2}-0)=2\log{2}$$

#### Problem 38

For problem 38 we are asked to evaluate the following iterated integral problem
using Fubini's theorem:
$$\int_{0}^{1}\int_{0}^{3}xe^{xy}\,dx\,dy$$
This problem looks pretty difficult to evaluate in its current form, but it also
looks like if we were integrating in reverse order we would be able to solve the
problem much more easily. Fubini's theorem allows us to restate the above
iterated integral as the following:
$$\int_{0}^{3}\int_{0}^{1}xe^{xy}\,dy\,dx$$
Evaluating the new inner integral:
$$x\int_{0}^{1}e^{xy}dy$$
Using a u-substitution with $u=xy$ yields $du=x\,dy$, $dy=\frac{du}{x}$,
the lower bound as $x*0=0$, and the upper bound as $x*1=x$:
$$\int_{0}^{x}e^udu=e^x-1$$
Plugging this into the outer integral:
$$\int_{0}^{3}\left(e^x-1\right)\,dx$$
Splitting the integral helps with the evaluation:
$$\int_{0}^{3}e^x\,dx-\int_{0}{3}1dx=\left.e^x\right|_{0}^{3}-3=e^3-4$$