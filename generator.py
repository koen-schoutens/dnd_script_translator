import cv2
# importing os module
import os

OUTPUT_PATH = './output'

def getLetter(letter, img):
    number = ord(letter.lower()) -97
    if not (0 <= number <= 25):
        number = 26
    pixel_height = 50
    y1 = (number*pixel_height) + number
    y2 = y1+pixel_height
    x1 = 0
    x2 = pixel_height
    img_cropped = img[y1:y2, x1:x2]
    return img_cropped


pharase = input("Pharase you want to convert: ")

img = cv2.imread('data/runes.png')
first = True

for char in pharase:
    img_character = getLetter(char, img)
    if first:
        first = False
        final_character = img_character
    else:
        final_character = cv2.hconcat([final_character, img_character])

if not os.path.exists(OUTPUT_PATH):
    os.mkdir(OUTPUT_PATH)


cv2.imwrite(OUTPUT_PATH +"/image.png", final_character)
cv2.destroyAllWindows()

