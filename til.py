'''
Facts Checker Program

This program checks for new Facts posted in /r/todayilearned and returns them in a dictionary
'''

import praw, time

r = praw.Reddit('TIL Facts monitor by u/kevgathuku v1.0'
                 'URL:https://github.com/kevgathuku/fact-a-day')
checked = []
content = []
facts = {}

def factsChecker():
    submissions = r.get_subreddit('todayilearned').get_hot(limit=15)
    for post in submissions:
        if post.id not in facts:
            facts[post.short_link] = post.title
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
        #Don't allow the post to start with a blank character
        if value[0] == " ":
            facts[key] = value[1:]
        elif value[0] == ":":
            facts[key] = value[1:]
        elif value[0].islower():
            facts[key] = value[0].upper() + value[1:]


    return facts

def main():
    print sanitizeFacts()

if __name__ == '__main__':
    main()