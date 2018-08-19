from PIL import Image

if __name__ == '__main__':
   file_list = [line.rstrip('\n') for line in open("C:/Users/David/autoturk/labels/labels.list")]
   num_file = len(file_list)
   for i in range(num_file):
       im = Image.open("C:/Users/David/autoturk/images/" + file_list[i][:-4] + ".jpg")
       width, height = im.size
       x_scale = 1./width
       y_scale = 1./height
       label_file = open("C:/Users/David/autoturk/labels/formatted/" + file_list[i], "a")
       lines = [line.rstrip('\n') for line in open("C:/Users/David/autoturk/labels/" + file_list[i])]
       num_lines = len(lines)
       for l in range(num_lines):
           line = lines[l].split()
           x_center = float(line[1]) * x_scale
           y_center = float(line[2]) * y_scale
           x_width = float(line[3]) * x_scale
           y_width = float(line[4]) * y_scale
           if l == num_lines - 1:
               label_file.write("0 " + str(x_center) + " " + str(y_center) + " " + str(x_width) + " " + str(y_width))
               continue
           label_file.write("0 " + str(x_center) + " " + str(y_center) + " " + str(x_width) + " " + str(y_width) + "\n")
           print("0 " + str(x_center) + " " + str(y_center) + " " + str(x_width) + " " + str(y_width) + "\n")
       print("Formatted " + file_list[i])
