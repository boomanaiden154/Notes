#Riemann sums
In the last note set we looked at how to calculate the area under the curve using summations. While we could do it and we used limits to make it equal to the area $A$, there were several limitations. No $x$ in the closed interval $[a,b]$ could be negative, $f$ has to be continuous on every single $x$ in $[a,b]$, all subintervals have to have the same length $\Delta x$, and $w_k$ has to be the minimum or maximum value depending upon whether or not we are using inscribed or circumcised rectangles. In this note set I am going to show you how to use Riemann sums which remove these limitations. Riemann sums allow the following things:

1. $f$ may be discontinuous at some $x$ in $[a,b]$
2. The lengths of the subintervals may be different
3. $f(x)$ may be negative for some $x$ in $[a,b]$
4. $w_k$ may be any number in $[x_{k-1},x_k]$

Now that we know what Riemann sums can do, lets review some background information that you need to know. Lets start off with partitions.
##Partitions
Partitions are used to divide closed intervals such as $[a,b]$ into subintervals of different lengths. If you want to divide a close interval $[a,b]$ into subintervals, they would be of the form $[x_0,x_1]$, $[x_2,x_3]$,$[x_3,x_4]$...$[x_{n-1},x_n]$. If we are dividing a close interval into subintervals, the following must be true: $x_0 \lt x_1 \lt x_2 \lt x_3 \lt x_4 ... \lt x_5$. Now, lets introduce some new notation. Lets let $\Delta x_k$ represent the distance between $x_{k-1}$ and $x_k$. Now, lets look at the norm of a partition. The norm of a partition is the maximum $\Delta x_k$ in the partition. The norm of a partition $p$ is represented with two vertical bars surrounding it like this:$||p||$. This will come in handy a little bit later. However, the b iggest thing that you should take away from this section is how to turn an interval into subintervals and how to find $\Delta x_k$ for any valid $k$. Now, lets look at an example. If we have a closed interval $[0,5]$ and we break it into subintervals like this: $[0,1]$,$[1,1.5]$,$[2,2.5]$,$[2.5,4.5]$,$[4.5,5]$, find $\Delta x_k$ for $k$ = 1,2,3. If the first subinterval is $[0,1]$ then the distance in this one is obviously 1. Next, $1.5 - 1 = 0.5$. Finally, $2.5-2=0.5$. So $\Delta x_1=1$,$\Delta x_2=0.5$, and $\Delta x_3=0.5$. Now, lets look at the formula for finding a Riemann sum.
##Riemann sums
The riemann sum of a partition $p$ looks like the following:
$$
R_p = \sum_{k=1}^nf(w_k)\Delta x_k
$$
Where $w_k$ may be any number in $[x_{k-1},x_k]$, and $\Delta x_k$ is the difference between $x_{k-1}$ and $x_k$. The function $f$ also has to be only be defined on the interval $[a,b]$. The Riemann sum approaches the actual area under the curve $A$ as the norm of the partition $p$ approaches zero. This can be looked at in the formula below:
$$
A = \lim_{||p|| \to 0}\sum_{k=1}^nf(w_k)\Delta x_k
$$
##Conclusion
Riemann sums are pretty useful and they can be used in order to find the area under the curve $A$,  but there are better methods. In the next note set, we are going to look at the fundamental thereom of calculus which gives you the exact value of $A$. 