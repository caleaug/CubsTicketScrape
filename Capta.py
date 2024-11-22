from TicketInit import *
import numpy as np
from PIL import Image
import io, cv2
from matplotlib import pyplot as plt
import cv2 as cv
'''
driver = uc.Chrome()
driver.get("https://seatgeek.com/chicago-cubs-tickets/a/mlb/" + str(6100804))
page = BeautifulSoup(driver.page_source, "html.parser")

driver.save_screenshot("page.png")
im = Image.open("page.png")
im1 = im.crop((1120, 192, 1185,347))
#im1.show()

im2 = im.crop((1185, 192, 1400,347))
#im2.show()
im2.save("page.png")
'''
        
background = "page.png"
puzzle = "Capta2.1.jpg"

img = cv.imread(background, cv.IMREAD_GRAYSCALE)
img2 = img.copy()
template = cv.imread(puzzle, cv.IMREAD_GRAYSCALE)

w, h = 50, 50

methods = ['cv.TM_CCOEFF', 'cv.TM_CCOEFF_NORMED', 'cv.TM_CCORR',
            'cv.TM_CCORR_NORMED', 'cv.TM_SQDIFF', 'cv.TM_SQDIFF_NORMED']
for meth in methods:
    img = img2.copy()
    method = eval(meth)
    # Apply template Matching
    res = cv.matchTemplate(img,template,method)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
    # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
    if method in [cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)
    cv.rectangle(img,top_left, bottom_right, 255, 2)
    plt.subplot(121),plt.imshow(res,cmap = 'gray')
    plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(img,cmap = 'gray')
    plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
    plt.suptitle(meth)
    plt.show()



"""
background = cv2.imread(background, cv2.IMREAD_GRAYSCALE)
puzzle = cv2.imread(puzzle, cv2.IMREAD_GRAYSCALE)


background_edges = cv2.Canny(background, 100, 200)
puzzle_edges = cv2.Canny(puzzle, 100, 200)

result = cv2.matchTemplate(background_edges, puzzle_edges, cv2.TM_CCOEFF)
#min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
print(result)


"""
'''

#plt.subplot(121),plt.imshow(img,cmap = 'gray')
#plt.title('Original Image'), plt.xticks([]), plt.yticks([])
#plt.subplot(122),plt.imshow(edges,cmap = 'gray')
#plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
 
#plt.show()


"""
import sys
import numpy
numpy.set_printoptions(threshold=sys.maxsize)

background = "Capta2.2.png"
img = cv2.imread(background, cv2.IMREAD_GRAYSCALE)
edges = cv2.Canny(img,50,100)

plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
 
plt.show()
'''

