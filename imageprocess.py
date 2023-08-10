from skimage import io, color
img=io.imread('universe.jpg')
dimensions = color.guess_spatial_dimensions(img)
print (dimensions)
