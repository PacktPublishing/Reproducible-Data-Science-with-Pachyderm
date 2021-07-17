import python_pachyderm

client = python_pachyderm.Client()
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

print(client.list_pipeline())
