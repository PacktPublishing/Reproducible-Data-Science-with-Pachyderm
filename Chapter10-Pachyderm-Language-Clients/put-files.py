import python_pachyderm

client = python_pachyderm.Client()
with client.commit('photos', 'master') as i:
    client.put_file_url(i, 'landscape.png', 'https://i.imgur.com/zKo9Mdl.jpg')
    client.put_file_url(i, 'hand.png', 'https://i.imgur.com/HtZ8FyG.png')
    client.put_file_url(i, 'red_vase.png', 'https://i.imgur.com/d45jop9.jpg')
print(list(client.list_file("photos/master", "")))

