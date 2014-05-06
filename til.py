'''
Facts Checker Program

This program checks for new Facts posted in /r/todayilearned
'''

import praw, time

r = praw.Reddit('TIL Facts monitor by u/kevgathuku v1.0'
                 'URL:https://github.com/kevgathuku/til-buffer')
checked = [] 
while True:
    submissions = r.get_subreddit('todayilearned').get_hot(limit=15)
    for post in submissions:
        if post.id not in checked:
            if post.title.startswith('TIL that'):
                print post.title[9:] + " " + post.short_link
            elif post.title.startswith('TIL '):
                print post.title[4:] + " " + post.short_link
            checked.append(post.id)

    #Sleep for 30 minutes before retrying
    time.sleep(1800)