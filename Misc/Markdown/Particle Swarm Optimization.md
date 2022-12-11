# Particle Swarm Optimization

Particle Swarm Optimization(PSO) consists of initializing a set of particles. This consists of creating random matrices with dimensions of the number of particles by the dimensions of the solution. There are three matrices needed, one for the velocities, and one for the positions, and one for the personal best positions. There are two vectors that are needed, the global best position, which has a size of the dimension of the problem, and the particle best fitnesses, which has a length of the particle count. 

### Intialization

Initialization consists of creating random numbers for the velocity and position matrices. The matrix that contains the personal best position for each particle is the same as the position matrix in the initialization process. The global best position vector is initialized to a vector containing all zeros, and the vector containing the personal best fitness values, and the global best fitness value are initialized to negative infinity(theoretically, the minimum float value in practice), so that everything gets reset upon the first iteration.

### Main algorithm

The main algorithm does three main things, it updates the velocity matrix, it updates the position matrix, and then it finds new personal bests, and a new global best, if there is one. First off, velocities are updated according to the equation:

$$
v_{x,i}=v_{x,i-1}+c_1*r_1(p_x-q_{x,i})+c_2*r_2*(g-q_{x,i})
$$

The variable *v* represent the velocities, $c_1$ and $c_2$ are constants, they are usually set to two. $r_1$ and $r_2$ are random numbers between one and two. $p$ represent the matrix of personal bests, and $q$ represents the matrix of positions. $g$ represents the global best vector. This equation can be read as follows: the velocity of particle $x$ at iteration $i$ is equal to the velocity of particle $x​$ at iteration $i-1$ plus $c_1$ times $r_1$ times the personal best of particle $x$ minus the current position of particle $x$ plus $c_2$ times $r_2$ times the global best minus the current position of particle $x$. This is usually done particle by particle, dimension by dimension, but it is more efficient to do it in matrix form. To do this, two temporary matrices are needed for the computation, making it not that intensive on memory allocation.

$$
t_1=c_1*r(p-q)
$$

Where $t_1$ is the first temporary matrix, $c_1$ is a constant, $r$ is a vector of random values, $p$ is the particle personal best matrix, and $q$ is the particle position matrix. The equation for the second temporary matrix is as follows:

$$
t_2=c_2*r(g-q)
$$

$t_2$ is the second temporary matrix, $c_2$ is a constant, $r$ is a vector of random values, $g$ is the global best vector, and $q$ is the particle position matrix. There is a slight issue with the dimensions of the $g$ vector, because it needs to be made into a matrix with the same dimensions as $q$. This is done by simply taking the $g$ vector, and repeating it until it is the same size as the $q$ matrix. This is not very efficient, and it could be done in place using a custom kernel, or maybe a specialized point wise operation. After we have these two temporary matrices, we can easily compute the final velocity

$$
v=v+t_1+t_2
$$

The velocity matrix is equal to the sum of the velocity matrix, and the two temporary matrices that were computed earlier. After we have computed the velocity, either through normal methods, or through the matrix method, we need to compute the new positions. This is a similar formula for the matrix method and for the normal method. For the point-wise method:

$$
q_{x,i}=q_{x,i-1}+v_{x,i}
$$



This can be read as follows: the position of particle $x$ at iteration $i$ is equal to the position of particle $x$ at iteration $i -1$ plus the velocity of particle $x$ at iteration $i$. The matrix method is a fair amount simpler, but very similar:

$$
q=q+v
$$

You simply add the existing position matrix to the velocity matrix to get the new position matrix. This can be done in the same memory space as the original position matrix, making this fairly memory efficient.

### Updating personal bests, and the global best

Updating personal bests is fairly simple. It consists of taking a fitness function, $f(x)$, which takes in the particle's position as a vector, and gives out a single number as the fitness. If the fitness is of a particle is greater than the fitness stored in the vector which contains the personal best for each particle, then the value in that vector is updated, and the personal best matrix is updated for that particle. 

$$
\begin{cases}
                                   p_x=q_x & \text{if $f(q_x) > f(p_x)$} \\
                                   \text{do nothing} & \text{if $f(q_x) < f(p_x)$}
  \end{cases}
$$

The variables are as follows: $p$ is the personal best matrix, and $q$ is the particle position matrix. This equation can be read as follows: If the fitness of particle $x$ is greater than the personal best of particle $x$, then set the personal best position of particle $x$ to equal the current position of particle $x$. Otherwise, do nothing. Finding the global best is a very similar process, consisting of evaluating each particle for the global best. The equation is very similar:

$$
\begin{cases}
g=q_x & \text{if $f(q_x)>f(g)$} \\
\text{do nothing} & \text{if $f(q_x)<f(g)$}
\end{cases}
$$

The variables in this equation are as follows: $g$ is the global best vector, and $q$ is the particle position matrix. This equation can be read as follows: If the fitness of particle $x$ is the greater than the global best fitness, then set the global best to equal the fitness of the particle, otherwise do nothing.

### Hardware acceleration

Accelerating the initialization can be done on a Cuda GPU using cuRAND, and the main algorithm can mostly be implemented with a high degree of parallelism using cuBLAS. The only time cuBLAS cannot be used is in finding the second temporary matrix, $t_2$, because of how the global best vector is used. This will probably require a custom kernel. Updating the personal best and global best can be done on the GPU, but will be more difficult then the main algorithm. The fitness function will have to be ported to the GPU, and this may or may not be efficient depending upon the fitness function. If the fitness function is very poor at utilizing parallelism, or contains a high degree of branching, making it slow on a massively parallel device, then the particle position matrix can be transferred back to the CPU at the expense of a significant slowdown. Evaluating and updating the personal best can be done in a fairly highly parallel fashion depending upon the particle count. Evaluating the global best will require a parallel reduction, which will provide a significant hurdle in a proper high speed implementation of this algorithm on highly parallel hardware.






