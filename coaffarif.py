
alpha:int = 2
betta:int = 1
gamma:int = 1

# def qi(x):
#     return x+1
# def pi(x, gamma):
#     return 1+(x**gamma)
# def ui(x, alpha,beta,):
#     return (x**alpha)*((1-x)**beta)
# def ai(i, h, gamma):
#     return (pi(i*h, gamma))
# def gi(i,h):
#     return qi(i*h)
# def p_(i,h,gamma):
# 	return gamma*((i*h)**(gamma - 1))
# def u_(i,h,alpha,beta,gamma):
# 	return ((alpha*((i*h)**(alpha-1)) * ((1-i*h)**beta))-(((i*h)**alpha)*beta*((1-i*h)**(beta-1))))
# def u__(i,h,alpha,beta,gamma):
# 	return alpha * (alpha - 1) *((i*h)**(alpha - 2)) *((1 - (i*h))** beta)- 2 * alpha * beta * ((i*h)**(alpha - 1)) * ((1 - i*h)** (beta - 1)) + beta * (beta - 1) * ((i*h)**alpha) *((1 - i*h)**(beta - 2))
# def f(i,h,alpha,beta,gamma):
# 	return -(p_(i,h,gamma)*u_(i,h,alpha,beta,gamma)+pi(i,gamma)*u__(i,h,alpha,beta,gamma))+(qi(i)*ui(i,alpha,beta))
def qi(x):
    return x+1
def pi(x):
    return 1+(x)
def ui(x):
    return (x**2)*((1-x)**1)
def ai(i, h):
    return (pi(i*h))
def gi(i,h):
    return qi(i*h)
def p_(i,h):
	return 1*((i*h)**(1 - 1))
def u_(i,h):
	return ((2*((i*h)**(2-1)) * ((1-i*h)**1))-(((i*h)**2)*1*((1-i*h)**(1-1))))
def u__(i,h):
	return 2 * (2 - 1) *((i*h)**(2 - 2)) *((1 - (i*h))** 1)- 2 * 2 * 1 * ((i*h)**(2 - 1)) * ((1 - i*h)** (1 - 1)) + 1 * (1 - 1) * ((i*h)**2) *((1 - i*h)**(1 - 2))
def f(i,h):
	return -(p_(i,h)*u_(i,h)+pi(i)*u__(i,h))+(qi(i)*ui(i))