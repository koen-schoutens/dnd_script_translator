import cv2

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


img = cv2.imread('data/runes.png')
my_string = "C***i* Darok"
first = True

for char in my_string:
    img_character = getLetter(char, img)
    if first:
        first = False
        final_character = img_character
    else:
        final_character = cv2.hconcat([final_character, img_character])

cv2.imshow('final img', final_character)
cv2.imwrite("output.png", final_character)
cv2.waitKey(0)
cv2.destroyAllWindows()

