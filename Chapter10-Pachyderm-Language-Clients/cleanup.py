import python_pachyderm

client = python_pachyderm.Client()
client.delete_repo("photos", force=True)
client.delete_pipeline(pipeline_name="contour", force=True, keep_repo=False)
client.delete_pipeline(pipeline_name="histogram", force=True, keep_repo=False)

print(list(client.list_repo()))
print(list(client.list_pipeline()))

