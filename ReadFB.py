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

data = graph.request("204153042939851/posts/?fields=message,link,permalink_url,created_time,type,name,id,comments.limit(0).summary(true),shares,likes.limit(0).summary(true),reactions.limit(0).summary(true)&limit=100")
print(data)

