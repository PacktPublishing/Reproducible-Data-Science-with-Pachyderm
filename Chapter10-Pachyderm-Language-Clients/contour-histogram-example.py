import python_pachyderm

client = python_pachyderm.Client()

client.create_repo("photos")

with client.commit('photos', 'master') as i:
    client.put_file_url(i, 'landscape.png', 'https://i.imgur.com/zKo9Mdl.jpg')
    client.put_file_url(i, 'hand.png', 'https://i.imgur.com/HtZ8FyG.png')
    client.put_file_url(i, 'red_vase.png', 'https://i.imgur.com/d45jop9.jpg')

client.create_pipeline(
    pipeline_name="contour",
    transform=python_pachyderm.Transform(
        cmd=["python3", "contour.py"],
        image="svekars/contour-histogram:0.85",
    ),
    input=python_pachyderm.Input(
        pfs=python_pachyderm.PFSInput(glob="/", repo="photos")
    ),
)

client.create_pipeline(
    pipeline_name="histogram",
    transform=python_pachyderm.Transform(
        cmd=["python3", "histogram.py"],
        image="svekars/contour-histogram:0.85",
    ),
    input=python_pachyderm.Input(
        pfs=python_pachyderm.PFSInput(glob="/", repo="contour")
    ),
)

print(client.list_repo())
print(list(client.list_file("photos/master", "")))
print(client.list_pipeline())
