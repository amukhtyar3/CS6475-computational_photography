from time import time
import logging
import argparse
import painterly 
#from painterly import Painting


q_radii = {
    'low': [64, 32, 16, 8],
    'medium': [64, 16, 8, 4],
    'high': [64, 8, 4, 2]}

in_filename='./test-images/haruhi.png'

if __name__ == '__main__':
    
    
    
    # set brush radii
    radi = q_radii['medium']
    
    # load and convert input image to RGB
    
    newPainting = painterly.Painting(in_filename)
    
    
    # render the image
    newPainting.render(radii=radi)
    
    # save the output image
    out_filename='output.png'
    newPainting.save(filepath=out_filename)
    
