import numpy as np

def sigmoid(x):
    s = 1/(1+np.exp(-x))
    return s

def sigmoid_derivative(x):
    """
    Compute the gradient (also called the slope or derivative) of the sigmoid function with respect to its input x.
    You can store the output of the sigmoid function into variables and then use it to calculate the gradient.
    
    Arguments:
    x -- A scalar or numpy array

    Return:
    ds -- Your computed gradient.
    """
    
    s = sigmoid(x)
    ds = s*(1-s)    
    return ds

def image2vector(image):
    """
    Argument:
    image -- a numpy array of shape (length, height, depth)
    
    Returns:
    v -- a vector of shape (length*height*depth, 1)
    """
    v = image
    v = image.reshape((image.shape[0]*image.shape[1]*image.shape[2]),1)    
    return v

# Gradient descent converts faster after normalization

def normalizeRows(x):
    """
    Implement a function that normalizes each row of the matrix x (to have unit length).
    
    Argument:
    x -- A numpy matrix of shape (n, m)
    
    Returns:
    x -- The normalized (by row) numpy matrix. You are allowed to modify x.
    """
    
    # Compute x_norm as the norm 2 of x. Use np.linalg.norm(..., ord = 2, axis = ..., keepdims = True)
    x_norm = np.linalg.norm(x, axis=1,ord=2, keepdims=True)
    
    # Divide x by its norm.
    x = x/x_norm

    return x
# Implementing softmax

def softmax(x):
    """Calculates the softmax for each row of the input x.

    Your code should work for a row vector and also for matrices of shape (n, m).

    Argument:
    x -- A numpy matrix of shape (n,m)

    Returns:
    s -- A numpy matrix equal to the softmax of x, of shape (n,m)
    """
    
    # Apply exp() element-wise to x. Use np.exp(...).
    x_exp = np.exp(x)

    # Create a vector x_sum that sums each row of x_exp. Use np.sum(..., axis = 1, keepdims = True).
    x_sum = np.sum(x_exp, axis=1, keepdims=True)
    
    # Compute softmax(x) by dividing x_exp by x_sum. It should automatically use numpy broadcasting.
    s = x_exp / x_sum
    
    return s

def L1(yhat, y):
    """
    Arguments:
    yhat -- vector of size m (predicted labels)
    y -- vector of size m (true labels)
    
    Returns:
    loss -- the value of the L1 loss function defined above
    """
    
	loss = np.dot(abs(y-yhat),abs(y-yhat))
    return loss

if __name__ == '__main__':

	x = np.array([1, 2, 3])
	print ("Sigmoid of x", sigmoid(x))

	x = np.array([1, 2, 3])
	print ("sigmoid_derivative(x) = " + str(sigmoid_derivative(x)))

	image = np.array([[[ 0.67826139,  0.29380381],
        [ 0.90714982,  0.52835647],
        [ 0.4215251 ,  0.45017551]],

       [[ 0.92814219,  0.96677647],
        [ 0.85304703,  0.52351845],
        [ 0.19981397,  0.27417313]],

       [[ 0.60659855,  0.00533165],
        [ 0.10820313,  0.49978937],
        [ 0.34144279,  0.94630077]]])

	print ("image2vector(image) = " + str(image2vector(image)))

	x = np.array([
    [0, 3, 4],
    [1, 6, 4]])
	print("normalizeRows(x) = " + str(normalizeRows(x)))

	x = np.array([
    [9, 2, 5, 0, 0],
    [7, 5, 0, 0 ,0]])
	print("softmax(x) = " + str(softmax(x)))

	yhat = np.array([.9, 0.2, 0.1, .4, .9])
	y = np.array([1, 0, 0, 1, 1])
	print("L1 = " + str(L1(yhat,y)))
	