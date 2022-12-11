#Numerical Integration
While integrals are very powerful and the fundamental thereom of calculus can be error used to find the value of an integral, you cannot always find the antiderivative of a specific function. Sometimes you cannot find one at all. In this note set, I am going to show you how to use numerical integration in order to accurately approximate the value of a integral. There are two different main ways to do this: the trapezoidal rule and simpson's rule. Lets look at these:
##The Trapezoidal rule
The trapezoidal rule allows you to use trapezoids to find the area under the curve. This method is fairly accurate, but there are other methods. Lets look at the mathematical definition. If $f$ is continuous on $[a,b]$ and a regular partition on $[a,b]$ is determined by $a=x_0,x_1,x_2,x_3,...x_n=b$ then by the trapezoidal rule:
$$
\int_{a}^{b}f(x)dx \approx \frac{b-a}{2n}[f(x_0)+2f(x_1)+2f(x_2)+...+2f(x_{n-1})+f(x_n)]
$$
While the trapezoidal rule is very accurate with enough partitions, there is an error. However, the error amount can be calculated like this. If $f''$ is continuous and $M$ is a posotive real number such that $|f''(x)| \leq M$ for every $x$ in $[a,b]$ then the error involved using the trapezoidal rule will not be greater than:
$$
\frac{M(b-a)^3}{12n^2}
$$
##Simpson's rule
Simpson's rule can be used just like the trapezoidal rule to find the area under the curve without finding antiderivatives. Simpson's rule only works only small intervals that are smooth. If we need to numerically integrate a larger region we will need to use the composite version of simpson's rule which we will look at later. Simpson's rule looks like this: If $f$ is continuous on the closed interval $[a,b]$ then:
$$
\int_{a}^{b}f(x)dx \approx \frac{b-a}{6}\left[f(a)+4f(\frac{a+b}{2})+f(b)]\right]
$$
While this formula works fairly well on small intervals of functions, it does not work very well on large areas. In order to find the area of large areas we are going to have to look at using the composite version of simpson's rule. Before we get to that, lets look at the error involved with using simpson's rule. If $f^{(4)} = f''''(x)$ and $M$ is a number in the closed interval $[a,b]$ then the error involved with using simpson's rule is no greater than:
$$
\frac{1}{90}\left(\frac{b-a}{2}\right)^5|f^{(4)}(M)|
$$
The error involved with using simpson's rule is also usually less than with using the trapezoidal rule. Now that we have seen the basic version of simpson's rule lets look at the composite version which will give you better accuracey of bigger intervals.
##Composite Simpson's rule
The composite version of simpson's rule looks like this: If $f$ is continuous over the closed interval $[a,b]$ and $[a,b]$ is partitioned into $n$ subintervals and $n$ is an even integer then by the composite version of simpson's rule:
$$
\int_{a}^{b}f(x)dx \approx = \frac{b-a}{3n}\left[f(x_0)+4f(x_1)+2f(x_2)+4f(x_3)+...+2f(x_{n-2}+4f(x_{n-1})+f(x_n)\right]
$$
The error estimate for the composite version of simpson's rule looks like the following: If $M$ is a number that satisfies the condition that $|f''''(x)| \leq M$ for every $x$ in $[a,b]$ then the error for the composite version of simpson's rule is no greater than:
$$
\frac{M(b-a)^4}{180n^4}
$$
##Conclusion
There are several other forms of simpson's rule such as simpson's 1/3 rule and simpson's 3/8 rule but we are not going to be covering these here. Maybe in a future note set, but for now you can look them up. Numerical integration can be extremely accurate, and for some purposes it is easier to compute than finding an antiderivative of a function.