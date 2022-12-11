#Calculating Derivatives
In order to calculate derivatives you can either use one of the several definitions of the derivative or you can use several of the rules available in order to find a functions derivative. It is usually much easier to use the rules of differentiation to find a functions derivative. However, I am going to cover both in this note set as you should know both.
##Definitions of a derivative
There are two main mathematical definitions of a derivative. The increment definition of a derivative and the normal definition of a derivative. The normal definition of a derivative looks like this:
$$\lim_{h\to0}\frac{f(x + h) - f(x)}{h}$$
The increment definition of a derivative looks like this:
$$\lim_{\Delta x \to 0}\frac{f(x + \Delta x) - f(x)}{\Delta x}$$
As you can see these definitions are functionally equvilant they are just in different forms. The increment definition of a derivative takes advantage of increments which are useful in many different ways. Now, lets look at an example. If we want to take the derivative of this function:
$$f(x)=x^2$$
We need to find $$f(x + \Delta x)$$ we can do this using some simple function manipulation. The calculation to find $$f(x + \Delta x)$$ looks like the following
$$f(x + \Delta x)= (x + \Delta x)^2 = x^2 + 2x \Delta x + \Delta x^2$$
If we plug all of this into the limit it looks like this:
$$\lim_{\Delta x \to 0}\frac{x^2 + 2x \Delta x + \Delta x^2 - x^2}{\Delta x}$$
We can cancel out x squared and then the equation looks like this
$$\lim_{\Delta x \to 0}\frac{2x \Delta x + \Delta x^2}{\Delta x}$$
After doing some ration expression simplification we get this:
$$\lim_{\Delta x \to 0}2x + \Delta x$$
And since this is a limit we have to move delta x towards zero which gives us $$f'(x) = 2x$$.Yeah, we found the derivative of $$f(x)=x^2$$
##Rules of derivatives
While the definitions of derivatives are great and all, they are not exactly the fastest way to find a derivative. The fastest way to find a derivative would be to use a computer or to use the rules of derivatives. One of the simplest rules of derivatives is the power rule. The power rule looks like this:
$$D_x(x^n) = nx^{n-1}$$
As you can see, with this rule it would be much easier to compute the derivative that we computed last section with the power rule. The calculation would look like this:
$$D_x x^2 = 2x^{2-1}$$
Simplified the equation looks like this:
$$D_x x^2 = 2x^1 = 2x$$
This is the exact same answer that we got while using the definition of the derivative. Know, lets go look at some other rules. If you are finding the derivative of a linear equation, the derivative will be constant and it will be equal to the slope. This formula describes this mathematically:
$$D_x(mx+b) = m$$
If you try to take the derivative of a constant function it will always be 0. This makes sense because the slope of a horizontal line is 0. This formula describes this mathematically:
$$D_x(c) = 0$$
If you multiply a function by a constant and you try to take the derivative of it the derivative will be the constant multiplied by the derivative of the function. This looks like this:
$$D_x[cf(x)] = cD_xf(x)$$
Next, what if we add two functions. For example, if we add x squared and 2x squared. This formula right here describes how this would work:
$$D_x[f(x) + g(x)] = D_xf(x) + D_xg(x)$$
This works very similarlly with subtraction:
$$D_x[f(x) - g(x)] = D_xf(x) - D_xg(x)$$
Next, lets look at trigenometric functions. There are many cases in the real world where you would want to take a derivative of a function involving trigenometric functions. The derivative of sin looks like this:
$$D_x sin x = cos x$$
The derivative of tangent looks like this:
$$D_x tan x = sec^2 x$$
The derivative of cosine looks like this:
$$D_x cos x = -sin x$$
The derivative of cot looks like this:
$$D_x cot x = -esc^2 x$$
Now that we know all of the basic functions, we can know look at the reciprocal rule, the product rule, and the quotient rule. The product rule looks like this:
$$D_xf(x)g(x) = f(x)D_xg(x) + g(x)D_xf(x)$$
The product rule is very useful as in the real world you will need to take derivatives of functions involving products. Next up, lets look at the quotient rule. The quotient rule looks like this:
$$D_x(\frac{f(x)}{g(x)}) = \frac{g(x)D_xf(x) - f(x)D_xg(x)}{[g(x)^2]}$$
This rule is very useful for the same reasons as listed for the product rule. Finally, there is the reciprocal rule. It makes it easier to find the derivative of reciprocal functions. The reciprocal looks like this:
$$D_x[\frac{1}{g(x)}] = -\frac{D_xg(x)}{[g(x)]^2}$$
##The Chain Rule
While all of these rules for finding derivatives are useful, we still have not covered one use case. What if we want to find the derivative of a function like $f(x) = sin 2x$. While we can solve this normally, it is much easier to do this with the chain rule. The chain function looks like this:
$$(f(x) \circ g(x))' = g'(x)f'(g(x))$$