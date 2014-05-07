'''
Facts Checker Program

This program checks for new Facts posted in /r/todayilearned
'''

import praw, time

r = praw.Reddit('TIL Facts monitor by u/kevgathuku v1.0'
                 'URL:https://github.com/kevgathuku/til-buffer')
checked = []
content = []
facts = {}

def factsChecker():
    submissions = r.get_subreddit('todayilearned').get_hot(limit=15)
    for post in submissions:
        if post.id not in checked:
            if post.title.startswith('TIL that ') or post.title.startswith('TIL That '):
                post.title = post.title[9:] + " " + post.short_link
            elif post.title.startswith('TIL '):
                post.title = post.title[4:] + " " + post.short_link
            elif post.title.startswith('TIL - '):
                post.title = post.title[6:] + " " + post.short_link
            checked.append(post.id)
            content.append(post.title)
    facts = dict(zip(checked, content))
    return facts
        #Sleep for 30 minutes before retrying
            #time.sleep(5)

if __name__ == '__main__':
    print factsChecker()