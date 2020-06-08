import praw
import pandas as pd

reddit = praw.Reddit(client_id = '9FdeBeB-2QZNjQ', client_secret = 'EbJb8kcJ_csQd_LQww-33GNmCKM', user_agent = 'Nosleep_project')

nosleep_subreddit = reddit.subreddit('nosleep')

posts = []
for post in nosleep_subreddit.hot(limit=10):
    posts.append([post.title, post.score, post.id, post.subreddit, post.url, post.num_comments, post.selftext, post.created])

#posts = pd.DataFrame(posts,columns=['title', 'score', 'id', 'subreddit', 'url', 'num_comments', 'body', 'created'])
#print(posts)
#posts.to_csv('stories.csv')

print(posts[1][-2])
