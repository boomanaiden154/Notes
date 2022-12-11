#Summations
A summation can be used to sum a set of numbers. If you have a set of numbers $a$ with $n$ elements, you can sum it with the following:
$$
\sum_{k=1}^{n}a_k
$$
Expanded, this looks like this
$$
a_1 + a_2 + a_3 \dots + a_n
$$
While summations are quite simple, they have many different uses in mathematics. They can be used to find a definite integral, and they can be used for many different applications in computer science. Now that you know the basic notation for summations, lets establish some basic rules that can be used to approximate summations without having to add up each element. We can also use different variables for our summation. For example, if we wanted the number of elements to be $b$ and we wanted our index to be $c$ then the summation would look like this:
$$
\sum_{c=1}^ba_k
$$
There is not really an established notation for what variables to use for summations. While there may be certain guidelines in specific fields of mathematics or science, there are not any general guidelines.
##Some rules for finding summations
In this section I am going to list most of the basic summation rules without much explanation. I feel that these rules are easily explainable by just looking at them.
$$
\sum_{k=1}^nc=nc
$$
$$
\sum_{k=1}^nk=\frac{n(n+1)}{2}
$$
$$
\sum_{k=1}^nk^2=\frac{n(n+1)(2n+1)}{6}
$$
$$
\sum_{k=1}^nk^3=\left(\frac{n(n+1)}{2}\right)^2
$$
$$
\sum_{k=1}^nca_k = c\sum_{k=1}^nk
$$
$$
\sum_{k=1}^n(a_k +  b_k) = \sum_{k=1}^na_k + \sum_{k=1}^nb_k
$$
$$
\sum_{k=1}^n(a_k - b_k) = \sum_{k=1}^na_k - \sum_{k=1}^nb_k
$$
As you can see, these are just some general rules that you can use in order to simplify a summation without adding up all of its terms. Sometimes adding up all of the terms will be simpler, and sometimes you simply cannot apply one of these rules, but if you have a very large value for $n$ then you will most likely want to use one of these rules.