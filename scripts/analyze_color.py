from skimage import data, io
from skimage.color import rgb2hsv
from glob import glob
import csv

# analyze_color.py - 
# opens every image in thumbs/1024 and averages its pixels
# to get H,S,V numbers, then saves as colors.csv.
# Requires scikit-image and dependencies.

# THIS SCRIPT IS SLOWWWWWWWWWWW 
# please replace it with something in node pipeline

# assumes we are in a folder structure of: 
#   vikus-viewer-data
#     data
#     scripts
#       analyze_color.py
#   thumbs
#   vikus-viewer
#     data* (linked alias)  
idlist = glob('../../thumbs/1024/*.jpg')
# idlist = ['../../thumbs/1024/A_1_99.jpg']
csvdata = [['id','hue','saturation','value']]

for i, n in enumerate(idlist):
  print('starting',i, n)
  id = n[n.rfind('/')+1:n.rfind('.')]
  temp = rgb2hsv(io.imread(n))
  all_hue = 0
  all_sat = 0
  all_val = 0
  row_len = len(temp)
  col_len = 0
  # print(row_len)
  for y, row in enumerate(temp):
    col_len = len(row)
    for x, cell in enumerate(row):
      all_hue = all_hue + cell[0]
      all_sat = all_sat + cell[1]
      all_val = all_val + cell[2]
  pix_count = row_len*col_len
  # print(all_hue, all_val, pix_count)
  all_hue = all_hue / pix_count
  all_sat = all_sat / pix_count
  all_val = all_val / pix_count
  # print('hue:',all_hue,', val:',all_val,', ',id)
  csvdata.append([id, all_hue, all_sat, all_val])

# print(csvdata[0],csvdata[1])

with open('colors.csv', 'w', newline='') as f:
  writer = csv.writer(f)
  writer.writerows(csvdata)

print('all done, thanks!')

