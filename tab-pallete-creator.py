"""

Take File Path or URL and create Tableau Colour Palette
Choose between 1 and 10 colours for the Palette
Colour Palette Quality = 1 - takes longer but high quality
Colour Palette Quality = 10 - quicker but lower quality

-- This version includes an IF statement to choose between a File Path or URL 
-- File Path is translated into URL form

Created using colorthief

Ben Renshaw

""" 


def rgb_to_hex(rgb): 
#take tuple and return HEX value
    return '%02x%02x%02x' % rgb 

def string_search(file_name, substring): 
    line_number= 0
    results = []
    #Start at top of file and with blank list 
    with open(file_name, 'r') as read_obj:
        for line in read_obj:
            line_number +=1
            if substring in line:
                results.append(int(line_number))
                #if substring is found in search, append integer to empty list
    return results


def replace_line(file_name, line_num, text):
    lines = open(file_name, 'r').readlines()
    lines[line_num] = text
    out = open(file_name, 'w')
    out.writelines(lines)
    out.close()
    #read file, write lines and close file

def path2url(path):
    return urljoin('file:', pathname2url(path))


preferences = ''
#this should  be your file path to Preferences.tps file - don't forget \\ 
subend = '</preferences>'
#end of Preferences.tps file 
substart = '</color-palette>'
#end of last colour palette imported
import sys
import os
from urllib.request import urlopen
import io
from colorthief import ColorThief
from urllib.request import pathname2url
from urllib.parse import urljoin



urlorfilepath = input('Choose URL or File Path:\n')
#Enter URL or File Path to take you on that Path


if urlorfilepath == 'File Path':
        b = input('Please Enter An File Path:\n')
#input filepath of photo 
        d = input('Please Enter Palette Size between 1-10:\n')
#colorthief allows for a palette size of 1-10, you can choose the size here 
        cc = int(d)
#ensures that palette size input is an integer
        e = input('Please Enter a Palette Quality (Highest Quality = 1, Lowest Quality = 10):\n')
#colortheif allows for a palette quality, 1 is highest, 10 is lowest - the lower the quality the faster it is returned
        ee = int(e)
#ensures that palette quality is an integer
        url = urlopen(path2url(b))
#turns FilePath from FilePath into URL using path2url function
        pic = io.BytesIO(url.read())
#transforms URL into bytes - or actually UTF-8 
        colour_thief = ColorThief(pic)
#import bytes into colour thief 
#single = (colour_thief.get_color(quality=1)) can use this input to get single, dominant colour 
        palette = (colour_thief.get_palette(quality=ee, color_count = cc, ignore_white=True))
#this returns palette with quality & colour count from earlier inputs. ignore_white currently hardcoded 
        list=[]
#empty list
        for item in palette:
            list.append('<color>'+'#'+rgb_to_hex(item)+'</color>')
#For loop to transform RGB tuple to Hex code, and inserting necessary parts for preferences file 
        c = input('Name your Pallete:\n')
#name inputted here will be name in Tableau
        cpname = '<color-palette name='+'"'+c+'"'+' type="regular">'
#top part of colour palette in preferences file 
        cpend = '</color-palette>'
#end of colour palette in preferences file 
        new_list = str(list).replace("['","").replace("']","").replace("', '","")
#transforms list into one large string, removing punctuation, etc. 
        colour_palette = cpname+new_list+cpend
#create colour palette, ready to be written to preferences.tps 
        start = (string_search(preferences, substart))
#finds line number(s) of end of colour palettes 
        end = (string_search(preferences, subend))
#finds end of Preferences file 
        new_line = ((start[-1])+1)
#finds last colour palette using index -1, then adds one so it writes on line below 
        replace_line(preferences, new_line, colour_palette)
#replaces empty lines in preferences file with colour palette 
        print('Open Tableau & Enjoy your new palette')
elif urlorfilepath == 'URL':
        b = input('Please Enter An URL:\n')
#input URL of photo 
        d = input('Please Enter Palette Size between 1-10:\n')
#colorthief allows for a palette size of 1-10, you can choose the size here 
        cc = int(d)
#ensures that palette size input is an integer
        e = input('Please Enter a Palette Quality (Highest Quality = 1, Lowest Quality = 10):\n')
#colortheif allows for a palette quality, 1 is highest, 10 is lowest - the lower the quality the faster it is returned
        ee = int(e)
#ensures that palette quality is an integer
        url = urlopen(b)
#opens given URL
        pic = io.BytesIO(url.read())
#transforms URL into bytes - or actually UTF-8 
        colour_thief = ColorThief(pic)
#import bytes into colour thief 
#single = (colour_thief.get_color(quality=1)) can use this input to get single, dominant colour 
        palette = (colour_thief.get_palette(quality=ee, color_count = cc, ignore_white=True))
#this returns palette with quality & colour count from earlier inputs. ignore_white currently hardcoded 
        list=[]
#empty list
        for item in palette:
            list.append('<color>'+'#'+rgb_to_hex(item)+'</color>')
#For loop to transform RGB tuple to Hex code, and inserting necessary parts for preferences file 
        c = input('Name your Pallete:\n')
#name inputted here will be name in Tableau
        cpname = '<color-palette name='+'"'+c+'"'+' type="regular">'
#top part of colour palette in preferences file 
        cpend = '</color-palette>'
#end of colour palette in preferences file 
        new_list = str(list).replace("['","").replace("']","").replace("', '","")
#transforms list into one large string, removing punctuation, etc. 
   
        colour_palette = cpname+new_list+cpend
#create colour palette, ready to be written to preferences.tps 

        start = (string_search(preferences, substart))
#finds line number(s) of end of colour palettes 
        end = (string_search(preferences, subend))
#finds end of Preferences file 
        new_line = ((start[-1])+1)
#finds last colour palette using index -1, then adds one so it writes on line below 

        replace_line(preferences, new_line, colour_palette)
#replaces empty lines in preferences file with colour palette 
        print('Open Tableau & Enjoy your new palette')

elif urlorfilepath == 'File Path':
        b = input('Please Enter An File Path:\n')
#input URL of photo 
        d = input('Please Enter Palette Size between 1-10:\n')
#colorthief allows for a palette size of 1-10, you can choose the size here 
        cc = int(d)
#ensures that palette size input is an integer
        e = input('Please Enter a Palette Quality (Highest Quality = 1, Lowest Quality = 10):\n')
#colortheif allows for a palette quality, 1 is highest, 10 is lowest - the lower the quality the faster it is returned
        ee = int(e)
#ensures that palette quality is an integer
        url = urlopen(path2url(b))
#opens given URL
        pic = io.BytesIO(url.read())
#transforms URL into bytes - or actually UTF-8 
        colour_thief = ColorThief(pic)
#import bytes into colour thief 
#single = (colour_thief.get_color(quality=1)) can use this input to get single, dominant colour 
        palette = (colour_thief.get_palette(quality=ee, color_count = cc, ignore_white=True))
#this returns palette with quality & colour count from earlier inputs. ignore_white currently hardcoded 
        list=[]
#empty list
        for item in palette:
            list.append('<color>'+'#'+rgb_to_hex(item)+'</color>')
#For loop to transform RGB tuple to Hex code, and inserting necessary parts for preferences file 
        c = input('Name your Pallete:\n')
#name inputted here will be name in Tableau
        cpname = '<color-palette name='+'"'+c+'"'+' type="regular">'
#top part of colour palette in preferences file 
        cpend = '</color-palette>'
#end of colour palette in preferences file 
        new_list = str(list).replace("['","").replace("']","").replace("', '","")
#transforms list into one large string, removing punctuation, etc. 
   
        colour_palette = cpname+new_list+cpend
#create colour palette, ready to be written to preferences.tps 

        start = (string_search(preferences, substart))
#finds line number(s) of end of colour palettes 
        end = (string_search(preferences, subend))
#finds end of Preferences file 
        new_line = ((start[-1])+1)
#finds last colour palette using index -1, then adds one so it writes on line below 

        replace_line(preferences, new_line, colour_palette)
#replaces empty lines in preferences file with colour palette 
        print('Open Tableau & Enjoy your new palette')
os.system('pause') 
