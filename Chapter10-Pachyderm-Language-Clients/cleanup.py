import python_pachyderm

client = python_pachyderm.Client()
client.delete_repo("photos", force=True)
client.delete_all_pipelines()

print(client.list_repo())
print(client.list_pipeline())


