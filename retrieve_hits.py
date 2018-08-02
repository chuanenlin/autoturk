import boto
from boto.mturk.connection import MTurkConnection
from boto.mturk.question import HTMLQuestion
from boto.mturk.layoutparam import LayoutParameter
from boto.mturk.layoutparam import LayoutParameters
import json
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import requests
from io import BytesIO
from PIL import Image
import os

worker_file = open("worker.list", "a")
hit_list = [line.rstrip('\n') for line in open("C:/Users/David/autoturk/hit-id.list")]
img_list = [line.rstrip('\n') for line in open("C:/Users/David/autoturk/image.list")]
num_img = len(img_list)
for i in range(num_img):
    mtc = MTurkConnection(
    aws_access_key_id = "[Your_access_key_ID]",
    aws_secret_access_key = "[Your_secret_access_key]",
    host = "mechanicalturk.amazonaws.com"
    )
    hit_id = hit_list[i]
    result = mtc.get_assignments(hit_id)
    assignment = result[0]
    worker_id = assignment.WorkerId
    worker_file.write(worker_id + "\n")
    for answer in assignment.answers[0]:
      if answer.qid == "annotation_data":
        worker_answer = json.loads(answer.fields[0])
    print("Worker ID: {}".format(worker_id))
    label_path = "C:/Users/David/autoturk/labels/"
    label_file = open(os.path.join(label_path, img_list[i][:-4] + ".txt"), "w")
    for j in range(0, len(worker_answer)):
        category = worker_answer[j]["label"]
        x_center = float(worker_answer[j]["width"]) / 2 + worker_answer[j]["left"]
        y_center = float(worker_answer[j]["height"]) / 2 + worker_answer[j]["top"]
        x_width = float(worker_answer[j]["width"])
        y_width = float(worker_answer[j]["height"])
        # print("YOLO format: [category number][object center in X][object center in Y][object width in X][object width in Y]")
        label_file.write("0 " + str(x_center) + " " + str(y_center) + " " + str(x_width) + " " + str(y_width) + "\n")
        print("{} {} {} {} {}\n".format(category, x_center, y_center, x_width, y_width))
    label_file.close()

    # To visualize
    img_src = "https://s3.us-east-2.amazonaws.com/drone-net/" + img_list[i]
    # Load the image from the HIT
    response = requests.get(img_src)
    img = Image.open(BytesIO(response.content))
    im = np.array(img, dtype=np.uint8)
    # Create figure, axes, and display the image
    fig,ax = plt.subplots(1)
    ax.imshow(im)
    # Draw the bounding box
    for answer in worker_answer:
        rect = patches.Rectangle((answer["left"],answer["top"]),answer["width"],answer["height"],linewidth=1,edgecolor="#32cd32",facecolor="none")
        ax.add_patch(rect)
    # Show the bounding box
    plt.show()
