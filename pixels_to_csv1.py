'''
    Takes an image and a rgb value and outputs pixel values where 
    the image has that color.
'''

import os
from PIL import Image
import pandas as pd

def rgb_of_pixel(folder_path, files):
    for img_path in files:
        actualPath = str(folder_path) + str(img_path)
        print(actualPath)
        image = Image.open(actualPath).convert('RGB')
        width, height = image.size
        
        xList = []
        yList = []
        count = 0
        for x in range(0,width):
            for y in range(0, height):
                r, g, b = image.getpixel((x,y))
                # print(r,g,b)
                if r < 100 and g > 200:
                    xList.append(x)
                    yList.append(y)
                    count += 1
        print('Count: ', count)

        # Checks that there are actually coordinates of that color
        if (len(xList) == len(yList)) > 0:
            df = pd.DataFrame({'x': xList, 'y': yList})
            if not os.path.isfile(folder_path + '/colored_pixels.csv'):
                df.to_csv(folder_path + 'colored_pixels.csv', index=False)
                print('Length: ', len(df))
            else: # else it exists so append without writing the header
                existing = pd.read_csv(folder_path + '/colored_pixels.csv')
                existing_values = set(zip(existing['x'], existing['y']))
                df['exists_in_df1'] = df.apply(lambda row: (row['x'], row['y']) in existing_values, axis=1)
                new_values = df[df['exists_in_df1'] == False].drop(columns=['exists_in_df1'])
                print('Length: ', len(df))
                new_values.to_csv(folder_path + 'colored_pixels.csv', mode='a', header=False, index=False)
        
        
        image.close()


def find_png_filenames( path_to_dir, suffix=".png" ):
    filenames = os.listdir(path_to_dir)
    return [ filename for filename in filenames if filename.endswith( suffix ) ]

folderPath = './images/MY_30/'
pngFileList = find_png_filenames(folderPath)
print(rgb_of_pixel(folderPath, pngFileList))