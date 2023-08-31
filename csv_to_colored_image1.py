'''
    Takes a csv file with pixel coordinates
    and the pixels of new image with specified color 
'''


from PIL import Image
import pandas as pd



def getCoordinates(csv_path):

    df = pd.read_csv(csv_path)
    x = df['x'].tolist()
    y = df['y'].tolist()
    return x,y

def colorImage(x,y, clean_image, altered_image):
    '''
        Takes a csv file with pixel coordinates and changes
        the pixels of new image to specified color 
    '''

    image = Image.open(clean_image)

    for i in range(len(x)):
        pixel = image.getpixel((x[i], y[i]))
        new_color = (7,255,77)
        image.putpixel((x[i],y[i]), new_color)
    image.save(altered_image)
    image.close()

folder_path = './images/MY_30/'
image_name = '160.2'
clean_image = folder_path + image_name + '.png'
altered_image = folder_path + image_name + '_alt.png'
csv_path = folder_path + 'colored_pixels.csv'

x,y = getCoordinates(csv_path)
colorImage(x,y, clean_image, altered_image)

