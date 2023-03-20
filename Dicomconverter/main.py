import numpy as np
import pydicom
from PIL import Image



#pydicom part
ds = pydicom.dcmread("file/path/goeshere")
pixel_data = ds.pixel_array
print(ds)

#apply windowing for usual computer screen
pixel_data = pydicom.pixel_data_handlers.apply_windowing(pixel_data,ds,0)


# Normalize the pixel values to the range [0, 65535] 
pixel_data = (pixel_data / np.max(pixel_data)) * 65535.0

# Convert the pixel values to the uint16 data type
pixel_data = pixel_data.astype('uint16')

#save 
image = Image.fromarray(pixel_data)
image.save("newconverteddcm.png")














