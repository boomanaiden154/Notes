# Antiderivatives

Antiderivatives are a  very useful tool in Calculus and they are mostly used when finding indefinite integrals. In this note set we are going to take a quick look at Antiderivatives. An antiderivative is pretty much the opposite of a derivative. Here is the formal definition: a function $F(x)$ is an antiderivative of $f(x)$ if $F'(x) = f(x)$. As you can see this is pretty much the opposite of a derivative. Now, lets look at finding some antiderivatives.

## Antiderivatives example 1 and constants

So, in this example we are going to find the antiderivative of $2x$. Finding the antiderivative of $2x$ is quite simple. We have to find what functions derivative equals $2x$ and most of you should know that if $f(x) = x^2$ then $f'(x) = 2x$. This means that the antiderivative of $2x$ is $x^2$. However, this is not the complete answer. If we remember from the previous lesson that I did on the rules of finding derivatives if there is a constant $c$ in a function, and the function looks like this $f(x) = c$ then the derivative will equal 0. This means that the antiderivative of $2x$ is actually $x^2 + c$. In this case $c$ can represent any constant. Now, lets look at another example.

## Antiderivatives example 2

Now that we know the basics of Antidifferentation, lets look at a more complicated example. Lets try and find the antiderivative of $x^5$. There is a basic rule that covers this. If $F(x)$ represents the antiderivative of the function and $f(x)$ is the function, and $f(x) = x^n$ then

$$
F(x) = \frac{1}{n + 1}x^{n+1} + c
$$

If we plug our function $x^5$ into this formula, we get:

$$
F(x) = \frac{1}{5 + 1}x^{5+1} + c
$$

or

$$
F(x) = \frac{1}{6}x^6 + c
$$

We can verify that this is the antiderivative of $f(x) = x^5$ by taking the derivative of $F(x)$ if we take the derivative we end up getting $f(x) = x^5$. If we you try to find this diervative yourself make sure you nullify $c$ by exchanging it with 0 because it is a constant.

## Indefinite Integrals

Indefinite integrals do have several different applications in the real world but there most notable application is in the fundamental thereom of calculus in which they are used to find definite integrals. The notation for an indefinite integral looks like this:

$$
\int f(x) dx = F(x) + c
$$

$dx$ tells us what variable we are integrating. For exampe if we had a function $f(t)$, we would have to integrate along the variable $t$. This would look like this:

$$
\int f(t) dt = F(t) + c
$$

In order to integrate a function we can use the indefinite integral. We will look at some ways we can use this in a later note set. In order to integrate we have to find the antiderivative of $f(x)$. For example, if we had an integral that looked like the following:

$$
\int 2x dx
$$

And we wanted to integrate it, we would simply find the antiderivative. This would look like this:

$$
\int 2x dx = x^2 + c
$$

## Some rules for finding antiderivatives

While most of these rules are pretty much the opposite of the rules for finding derivatives, I feel like they are worth restating here. All of the rules are stated in terms of indefinite integrals. Here is the list:

$$
\int x^n dx = \frac{1}{n + 1}x^{n+1} + c
$$

$$
\int e^x dx = e^x + c
$$

$$
\int cos(x) dx = sin(x) + c
$$

$$
\int cot(x) dx = ln|sin(x)| = -ln|csc(x)| + c
$$

$$
\int csc^2(x) dx = -cot(x) + c
$$

$$
\int csc(x)cot(x)dx = -csc(x) + c
$$

$$
\int \frac{1}{\sqrt{1-x^2}}dx = arcsin(x) + c
$$

$$
\int \frac{1}{x}dx = ln|x| + c
$$

$$
\int sin(x) dx = -cos(x)+ c
$$

$$
\int tan(x) dx = ln|sec(x)| = -ln|cos(x)| + c
$$

$$
\int sec^2(x)dx = tan(x)+ c
$$

$$
\int sec(x)tan(x)dx = sec(x) + c
$$

$$
\int \frac{1}{x^2+1}(x)dx = arctan(x) + c
$$

As you can see several of these rules are simply the same as the rules for differentiation except they are on opposite sides of the equation. If you have memorized the rules for differentation then you should easily be able to find these rules for antidifferentiation on the fly. If the antidiervative you wish to find does not have a rule on this list then you may be able to expand it and then apply some of the rules on this list.
