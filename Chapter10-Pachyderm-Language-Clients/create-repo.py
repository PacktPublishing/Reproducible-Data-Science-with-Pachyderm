import python_pachyderm

client = python_pachyderm.Client()
client.create_repo("photos")
print(client.list_repo())


