import python_pachyderm
from python_pachyderm.service import pps_proto

client = python_pachyderm.Client()

client.create_repo("photos")

with client.commit('photos', 'master') as i:
    client.put_file_url(i, 'landscape.png', 'https://i.imgur.com/zKo9Mdl.jpg')
    client.put_file_url(i, 'hand.png', 'https://i.imgur.com/HtZ8FyG.png')
    client.put_file_url(i, 'red_vase.png', 'https://i.imgur.com/d45jop9.jpg')

client.create_pipeline(
    pipeline_name="contour",
    transform=pps_proto.Transform(
        cmd=["python3", "contour.py"],
        image="svekars/contour-histogram:1.0",
    ),
    input=pps_proto.Input(
        pfs=pps_proto.PFSInput(glob="/", repo="photos")
    ),
)

client.create_pipeline(
    pipeline_name="histogram",
    transform=pps_proto.Transform(
        cmd=["python3", "histogram.py"],
        image="svekars/contour-histogram:1.0",
    ),
    input=pps_proto.Input(
        pfs=pps_proto.PFSInput(glob="/", repo="contour")
    ),
)

print(list(client.list_repo()))
print(list(client.list_file(("photos", "master"), "")))
print(list(client.list_pipeline()))
