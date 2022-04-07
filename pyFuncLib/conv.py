import numpy as np
def conv(f, img):
    """
    convolution of a filter kernel and input images (without padding: image size after convolution will decrease)
    -> f: input filter kernel
    -> img: input image

    <- img_out: output convoluted image
    """
    fr, fc= f.shape
    img_out = np.zeros((img.shape[0] - fr + 1, img.shape[1] - fc + 1))
    f = f[range(fr - 1, -1, -1), :][:, range(fc - 1, -1, -1)]
    for r in np.arange(img.shape[0] - fr + 1):
        for c in np.arange(img.shape[1] - fc + 1):
            current_patch = img[r:r+fr, c:c+fc]
            img_out[r, c] = np.sum(current_patch * f)

    return img_out