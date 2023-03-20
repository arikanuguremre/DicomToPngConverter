import numpy as np
import pydicom
import cv2 as cv
from PIL import Image
from pydicom.data import get_testdata_file


#pydicom part
ds = pydicom.dcmread("file/path/goeshere")
pixel_data = ds.pixel_array
print(ds)

#apply windowing for usual computer screen
pixel_data = pydicom.pixel_data_handlers.apply_windowing(pixel_data,ds,0)


# Normalize the pixel values to the range [0, 65535] again
#normalized_pixel_data = (pixel_data - np.min(pixel_data)) / np.ptp(pixel_data) * 65535.0
pixel_data = (pixel_data / np.max(pixel_data)) * 65535.0

# Convert the pixel values to the uint16 data type
pixel_data = pixel_data.astype('uint16')
#cv.imshow("Converted 16-bit depth png",pixel_data)
#cv.waitKey(0)
#save 
image = Image.fromarray(pixel_data)
image.save("newconverteddcm.png")














