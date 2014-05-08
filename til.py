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
        if post.id not in facts:
            facts[post.id] = post.title + " " + post.short_link
    #facts = dict(zip(checked, content))
    return facts
        #Sleep for 30 minutes before retrying
            #time.sleep(30*60)

def sanitizeFacts():
    facts = factsChecker()
    for id, fact in facts.iteritems():
        if fact.startswith('TIL that ') or fact.startswith('TIL That '):
            facts[id] = fact[9:]
        elif fact.startswith('TIL '):
            facts[id] = fact[4:]
        elif fact.startswith('TIL - '):
            facts[id] = fact[6:]
        elif fact.startswith('TIL, ') or fact.startswith('TIL: ') or fact.startswith('TIL, '):
            facts[id] = fact[5:]

    for key, value in facts.iteritems():
        if value[0].islower():
            facts[key] = value[0].upper() + value[1:]

    return facts

if __name__ == '__main__':
    print factsChecker()