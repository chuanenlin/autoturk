import boto
from boto.mturk.connection import MTurkConnection
from boto.mturk.question import HTMLQuestion
from boto.mturk.layoutparam import LayoutParameter
from boto.mturk.layoutparam import LayoutParameters

hit_url_file = open("hit-url.list", "w")
hit_id_file = open("hit-id.list", "a")
img_list = [line.rstrip("\n") for line in open("C:/Users/David/autoturk/image.list")]
num_img = len(img_list)
for i in range(num_img):
    img_src = "https://s3.us-east-2.amazonaws.com/drone-net/" + img_list[i]
    mtc = MTurkConnection(
    aws_access_key_id = "[Your_access_key_ID]",
    aws_secret_access_key = "[Your_secret_access_key]",
    host = "mechanicalturk.amazonaws.com"
    )
    image_url = LayoutParameter("image_url", img_src)
    obj_to_find = LayoutParameter("objects_to_find", "drone")
    params   = LayoutParameters([image_url, obj_to_find])
    response = mtc.create_hit(
      hit_layout    = "[Your_hit_layout]",
      layout_params = params,
      hit_type      = "[Your_hit_type]"
    )
    hit_type_id = response[0].HITTypeId
    hit_id = response[0].HITId
    hit_id_file.write(hit_id + "\n")
    print("HIT ID: {}".format(hit_id))
hit_url_file.write("https://www.mturk.com/mturk/preview?groupId=" + hit_type_id + "\n")
print("HIT URL: https://www.mturk.com/mturk/preview?groupId={}".format(hit_type_id))
