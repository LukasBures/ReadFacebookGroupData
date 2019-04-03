import facebook as fb

f_token = open("token.txt", "r")
token = f_token.readline()
f_token.close()

f_group = open("group.txt", "r")
group_id = f_group.readline()
f_group.close()

graph = fb.GraphAPI(access_token=token, version="3.1")

data = graph.request("me")
print(data)

data = graph.request("{0}/posts".format(group_id))
print(data)

