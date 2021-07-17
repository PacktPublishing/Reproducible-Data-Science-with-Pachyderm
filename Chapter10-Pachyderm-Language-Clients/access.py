import python_pachyderm

client = python_pachyderm.Client()
print(client.get_remote_version())
print(client.list_repo())


