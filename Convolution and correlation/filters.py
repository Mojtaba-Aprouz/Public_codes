
#### Mojtaba Aprouz - 40030594


from email.mime import image
import numpy as np





def conv_nested(image, kernel):

    """A naive implementation of convolution filter.



    This is a naive implementation of convolution using 4 nested for-loops.

    This function computes convolution of an image with a kernel and outputs

    the result that has the same shape as the input image.



    Args:

        image: numpy array of shape (Hi, Wi).

        kernel: numpy array of shape (Hk, Wk).



    Returns:

        out: numpy array of shape (Hi, Wi).

    """

    Hi, Wi = image.shape

    Hk, Wk = kernel.shape

    out = np.zeros((Hi, Wi))



    ### YOUR CODE HERE

    temp = np.zeros((Hi + Hk-1,Wi + Wk-1))
    for row in range(Hi + Hk-1):
        for col in range(Wi + Wk-1):
            for i in range(Hk):
                for j in range(Wk):
                    if (0<= row-i < Hi)&(0<= col-j < Wi):
                        temp[row,col] += (image[row-i , col-j]*kernel[i, j])
    out=temp[int(Hk/2):int(Hk/2)+Hi, int(Wk/2):int(Wk/2)+Wi]


    ### END YOUR CODE



    return out



def zero_pad(image, pad_height, pad_width):

    """ Zero-pad an image.



    Ex: a 1x1 image [[1]] with pad_height = 1, pad_width = 2 becomes:



        [[0, 0, 0, 0, 0],

         [0, 0, 1, 0, 0],

         [0, 0, 0, 0, 0]]         of shape (3, 5)



    Args:

        image: numpy array of shape (H, W).

        pad_width: width of the zero padding (left and right padding).

        pad_height: height of the zero padding (bottom and top padding).



    Returns:

        out: numpy array of shape (H+2*pad_height, W+2*pad_width).

    """



    H, W = image.shape

    out = None



    ### YOUR CODE HERE

    image_padded = np.zeros(shape=(H+2*pad_height, W+2*pad_width ))   
    image_padded[pad_height:-(pad_height), pad_width:-(pad_width)] = image 
    out=image_padded


    ### END YOUR CODE

    return out





def conv_fast(image, kernel):

    """ An efficient implementation of convolution filter.



    This function uses element-wise multiplication and np.sum()

    to efficiently compute weighted sum of neighborhood at each

    pixel.



    Hints:

        - Use the zero_pad function you implemented above

        - There should be two nested for-loops

        - You may find np.flip() and np.sum() useful



    Args:

        image: numpy array of shape (Hi, Wi).

        kernel: numpy array of shape (Hk, Wk).



    Returns:

        out: numpy array of shape (Hi, Wi).

    """

    Hi, Wi = image.shape

    Hk, Wk = kernel.shape

    out = np.zeros((Hi, Wi))



    ### YOUR CODE HERE
    padded_img = zero_pad(image, int(Hk/2), int(Wk/2)) 
    fliped_kernel=np.flip(kernel)
    for row in range(Hi):
        for col in range(Wi):
                    out[row,col]=np.sum( padded_img[row:row+Hk , col:col+Wk]*fliped_kernel)
    ### END YOUR CODE



    return out



def conv_faster(image, kernel):

    """

    Args:

        image: numpy array of shape (Hi, Wi).

        kernel: numpy array of shape (Hk, Wk).



    Returns:

        out: numpy array of shape (Hi, Wi).

    """

    Hi, Wi = image.shape

    Hk, Wk = kernel.shape

    out = np.zeros((Hi, Wi))



    ### YOUR CODE HERE

    pass

    ### END YOUR CODE



    return out



def cross_correlation(f, g):

    """ Cross-correlation of f and g.



    Hint: use the conv_fast function defined above.



    Args:

        f: numpy array of shape (Hf, Wf).

        g: numpy array of shape (Hg, Wg).



    Returns:

        out: numpy array of shape (Hf, Wf).

    """



    out = None

    ### YOUR CODE HERE

    kernel=np.flip(g)
    out = conv_fast(f, kernel)

    ### END YOUR CODE



    return out



def zero_mean_cross_correlation(f, g):

    """ Zero-mean cross-correlation of f and g.



    Subtract the mean of g from g so that its mean becomes zero.



    Hint: you should look up useful numpy functions online for calculating the mean.



    Args:

        f: numpy array of shape (Hf, Wf).

        g: numpy array of shape (Hg, Wg).



    Returns:

        out: numpy array of shape (Hf, Wf).

    """



    out = None

    ### YOUR CODE HERE

    g=g-np.mean(g)
    out = cross_correlation(f, g)

    ### END YOUR CODE



    return out



def normalized_cross_correlation(f, g):

    """ Normalized cross-correlation of f and g.



    Normalize the subimage of f and the template g at each step

    before computing the weighted sum of the two.



    Hint: you should look up useful numpy functions online for calculating 

          the mean and standard deviation.



    Args:

        f: numpy array of shape (Hf, Wf).

        g: numpy array of shape (Hg, Wg).



    Returns:

        out: numpy array of shape (Hf, Wf).

    """



    out = None

    ### YOUR CODE HERE
    Hg , Wg = g.shape
    Hf , Wf = f.shape

    out=np.zeros_like(f)
    padded_img=zero_pad(f,int(Hg/2),int(Wg/2))
    for i in range(Hf):
        for j in range(Wf):
            slice=padded_img[i:i+Hg,j:j+Wg]
            out[i,j]=np.sum(((slice-np.mean(slice))/np.std(slice))*((g-np.mean(g))/np.std(g)))


    ### END YOUR CODE



    return out