# *************** HOMEWORK 6 ***************
# GOOD LUCK!

# ********************* Helper functions ***********************
import matplotlib.pyplot as plt


def display(image):
    plt.imshow(image, cmap="gist_gray")
    plt.show()

# ************************ QUESTION 1 **************************
def load_binary_image(img_path):
    """
    Function that take txt file and convert it to a 2d array (list of list) that each number represent a pixel
    :param img_path: path to the txt file
    :return: the final 2d array
    """
    list_of_lists = []
    temp = []
    final_list = []
    count = 0
    f = open(img_path) #open file
    for line in f:
        lines = line.split() #split lines
        list_of_lists.append(lines) #add each line
    while [] in list_of_lists:
        list_of_lists.remove([]) #Removes excess blank lists
    for i in list_of_lists:
        for j in i[count]:
            temp.append(int(j)) #make each char into int and add it back as seperate cell
            count += 1
        count = 0 #reset counter
        final_list.append(temp) #add the list we use to the final one
        temp = []
    f.close()
    return final_list
# ************************ QUESTION 2 **************************
def add_padding(image, padding):
    """
    Function that take 2d array and add padding to it
    :param image: 2d array
    :param padding: padding wanted
    :return: 2d array after padding
    """
    after_padding = list(image) #array after padding
    for i in range(len(after_padding)):
        after_padding[i] = [0] * padding + after_padding[i] + [0] * padding #add padding to sides
    for j in range(padding):
        after_padding.append([0] * len(after_padding[0]))
        after_padding.insert(0, [0] * len(after_padding[0])) #add padding to top and bottom
    return after_padding

# ************************ QUESTION 3 **************************
def erosion(img_path, structuring_element):
    """
    Function that take txt file and preform erosion on him
    :param img_path: path to the txt file
    :param structuring_element: 2d array of the structuring element
    :return: 2d array of the image after erosion
    """
    image_original = load_binary_image(img_path)
    image_after = []
    temp = []

    if structuring_element == [[0, 0, 0], [0, 0, 0], [0, 0, 0]]:
        return image_original
    image_original = add_padding(image_original, 1)
    col = len(image_original[0])
    row = len(image_original)
    for x in range(1, row - 1):
        for y in range(1, col - 1):
            if image_original[x][y] == structuring_element[1][1] or structuring_element[1][1] == 0: #Test Middle
                if (image_original[x+1][y] == structuring_element[2][1] or structuring_element[2][1] == 0) and (image_original[x-1][y] == structuring_element[0][1] or structuring_element[0][1] == 0): #Test Right and Left
                    if (image_original[x][y - 1] == structuring_element[1][0] or structuring_element[1][0] == 0) and (image_original[x][y + 1] == structuring_element[1][2] or structuring_element[1][2] == 0): #Test Up and Down
                        if (image_original[x-1][y-1] == structuring_element[0][0] or structuring_element[0][0] == 0) and (image_original[x+1][y-1] == structuring_element[2][0] or structuring_element[2][0] == 0) and\
                                (image_original[x+1][y+1] == structuring_element[2][2] or structuring_element[2][2] == 0) and (image_original[x-1][y+1] == structuring_element[0][2] or structuring_element[0][2] == 0): #Test Diagonal
                            temp.append(1)
                        else:
                            temp.append(0)
                    else:
                        temp.append(0)
                else:
                    temp.append(0)
            else:
                temp.append(0)
        image_after.append(temp)
        temp = []
    return image_after

# ************************ QUESTION 4 **************************
def dilation(img_path, structuring_element):
    """
    Function that take txt file and preform dilation on him
    :param img_path: path to the txt file
    :param structuring_element: 2d array of the structuring element
    :return: 2d array of the image after dilation
    """
    image_original = load_binary_image(img_path)
    image_after = []
    temp = []

    if structuring_element == [[0, 0, 0], [0, 0, 0], [0, 0, 0]]:
        return image_original

    image_original = add_padding(image_original, 1)
    row = len(image_original)
    col = len(image_original[0])
    counter = 0
    for x in range(1, row - 1):
        for y in range(1, col - 1):
            if image_original[x][y] == structuring_element[1][1] and structuring_element[1][1] == 1:  # Test Middle
                counter += 1
            if x - 1 >= 0 and image_original[x - 1][y] == structuring_element[0][1] and structuring_element[0][1] == 1:
                counter += 1
            if x + 1 <= row - 1 and image_original[x + 1][y] == structuring_element[2][1] and structuring_element[2][1] == 1:  # Test Right and Left
                counter += 1
            if y - 1 >= 0 and image_original[x][y - 1] == structuring_element[1][0] and structuring_element[1][0] == 1:
                counter += 1
            if y + 1 <= col - 1 and image_original[x][y + 1] == structuring_element[1][2] and structuring_element[1][2] == 1:  # Test Up and Down
                counter += 1
            if x - 1 >= 0 and y - 1 >= 0 and image_original[x - 1][y - 1] == structuring_element[0][0] and structuring_element[0][0] == 1:
                counter += 1
            if x + 1 <= row - 1 and y - 1 >= 0 and image_original[x + 1][y - 1] == structuring_element[2][0] and structuring_element[2][0] == 1:
                counter += 1
            if x + 1 <= row - 1 and y + 1 <= col - 1 and image_original[x + 1][y + 1] == structuring_element[2][2] and structuring_element[2][2] == 1:
                counter += 1
            if x - 1 >= 0 and y + 1 <= col - 1 and image_original[x - 1][y + 1] == structuring_element[0][2] and structuring_element[0][2] == 1:  # Test Diagonal
                counter += 1
            if counter > 0:
                temp.append(1)
            else:
                temp.append(0)
            counter = 0
        image_after.append(temp)
        temp = []
    return image_after