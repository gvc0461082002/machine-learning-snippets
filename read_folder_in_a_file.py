import glob
import os
files = glob.glob(r"yourpath\*")
print(files)
write_to = open("wholesource.txt",'w+')
count = 0;
# iterate over the list getting each file
for fle in files:
     title = os.path.basename(fle.title())
   # open the file and then call .read() to get the text
     with open(fle) as f:

      text = f.read()
      #print(text)
      count=count+1
      write_to.write("\n")
      write_to.write("第"+str(count)+"个文件")
      write_to.write(title)
      write_to.write(text)
      write_to.write("\n")
      write_to.write("第" + str(count) + "个文件结束")
      write_to.write("\n")
      write_to.write("\n")