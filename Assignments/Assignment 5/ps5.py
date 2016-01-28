__author__ = 'paulsalvatore57'


                        #PART I - DATA STRUCTURE DESIGN

#Problem 1

#We want to aggregate RSS news feeds
#We will not parse the news feeds (a lot of information)
    #GUID       (str)
    #Title      (str)
    #Subject    (str)
    #Summary    (str)
    #Link       (str)
#Need to store the information as an object

#Write a class, NewsStory() with:
    #get_guid()
    #get_title()
    #get_subject()
    #get_summary()
    #get_link()

#Also needs a constructor taking the above as arguments and storing them
#This should be straight forward

# 6.00 Problem Set 5
# RSS Feed Filter

import feedparser
import string
import time
from project_util import translate_html
from news_gui import Popup

#-----------------------------------------------------------------------
#
# Problem Set 5

#======================
# Code for retrieving and parsing
# Google and Yahoo News feeds
# Do not change this code
#======================

def process(url):
    """
    Fetches news items from the rss url and parses them.
    Returns a list of NewsStory-s.
    """
    feed = feedparser.parse(url)
    entries = feed.entries
    ret = []
    for entry in entries:
        guid = entry.guid
        title = translate_html(entry.title)
        link = entry.link
        summary = translate_html(entry.summary)
        try:
            subject = translate_html(entry.tags[0]['term'])
        except AttributeError:
            subject = ""
        newsStory = NewsStory(guid, title, subject, summary, link)
        ret.append(newsStory)
    return ret

#======================
# Part 1
# Data structure design
#======================


# Problem 1

class NewsStory(object):
    def __init__(self, guid, title, subject, summary, link):
        self.guid = guid
        self.title = title
        self.subject = subject
        self.summary = summary
        self.link = link
    def get_guid(self):
        return self.guid
    def get_title(self):
        return self.title
    def get_subject(self):
        return self.subject
    def get_summary(self):
        return self.summary
    def get_link(self):
        return self.link

def testNews(site):
    for i in range(len(site)):
        print 'Article:', i + 1, "\n", 'Guid:', site[i].get_guid(), "\n", 'Title:', site[i].get_title()\
        , '\n', 'Subject:', site[i].get_subject(), "\n", 'Summary:', '\n', site[i].get_summary()\
        , "\n", 'Link:', site[i].get_link(), '\n', "-----------"


google = process('http://news.google.com/?output=rss')
# testNews(google)

#INPUTING NEWS:
# c = NewsStory(1, 2, 3, 4, 5)
# google = google + [c,]
# testNews(google)










# Part 2

class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        raise NotImplementedError


class WordTrigger(Trigger):
    def __init__(self, word):
        self.word = word.lower()
    def is_word_in(self, text):
        text = text.lower()
        for i in text:
            if i in string.punctuation:
                text = text.replace(i, " ")
        return self.word in string.split(text)


# test = WordTrigger('USA')
# for i in google:
#     title = i.get_title()
    # print title
    # if test.is_word_in(title) == True:
    #     print i.get_title()



class SubjectTrigger(WordTrigger):
    def __init__(self, word):
        WordTrigger.__init__(self, word)
    def evaluate(self, story):
        return self.is_word_in(story.get_subject())

class SummaryTrigger(WordTrigger):
    def __init__(self, word):
        WordTrigger.__init__(self, word)
    def evaluate(self, story):
        return self.is_word_in(story.get_summary())

class TitleTrigger(WordTrigger):
    def __init__(self, word):
        WordTrigger.__init__(self, word)
    def evaluate(self, story):
        return self.is_word_in(story.get_title())

# print google[0].get_title()
# c = 'nato'
# c = TitleTrigger(c)
# print c.evaluate(google[0])




###This one takes the process output and looks through the entire newsfeed, the assignment only called us to look through one at a time
# class SubjectTrigger(WordTrigger):
#     def __init__(self, NewsStoryS, word):
#         WordTrigger.__init__(self, word)
#         self.subject = []
#         for i in NewsStoryS:
#             self.subject += [i.get_subject(), ]
#     def getSubject(self):
#         return self.subject

# c = TitleTrigger(google, "clock")
# for i in c.getTitles():
#     if c.is_word_in(i) == True:
#         print i









# # Composite Triggers


class NotTrigger(Trigger):
    def __init__(self, T):
        self.T = T
    def evaluate(self, story):
        return not self.T.evaluate(story)


class AndTrigger(Trigger):
    def __init__(self, T1, T2):
        self.T1 = T1
        self.T2 = T2
    def evaluate(self, story):
        return self.T1.evaluate(story) and self.T2.evaluate(story)


class OrTrigger(Trigger):
    def __init__(self, T1, T2):
        self.T1 = T1
        self.T2 = T2
    def evaluate(self, story):
        return self.T1.evaluate(story) or self.T2.evaluate(story)



# # Phrase Trigger
# # Question 9


#MY LONG CONVOLUTED WAY
# class PhraseTrigger(Trigger):
#     def __init__(self, phrase):
#         self.phrase = phrase
#         self.length = len(phrase)
#     def evaluate(self, story):
#         n = 0
#         while n < 3:
#             if n == 0:
#                 story_test = story.get_title()
#             if n == 1:
#                 story_test = story.get_subject()
#             if n == 2:
#                 story_test = story.get_summary()
#             story_test = string.split(story_test)
#             while len(story_test) > 0:
#                 if string.split(self.phrase)[0] not in story_test:
#                     break
#                 if string.split(self.phrase)[0] in story_test:
#                     placeholder = story_test[story_test.index(string.split(self.phrase)[0]):]
#                     possiblephrase = " ".join(placeholder)[:self.length]
#                 if possiblephrase == self.phrase:
#                     return True
#                 else:
#                     story_test = story_test[story_test.index(string.split(self.phrase)[0]) + 1:]
#             n += 1
#         return False


# c = "aaa bbb ccc"
# d = "zzz aaa bbb cc ddd aaa bbb ccc"
# c = PhraseTrigger(c)
# print c.evaluate(d)


# print google[0].get_summary()
# c = 'Bad Day in'
# c = PhraseTrigger(c)
# print c.evaluate(google[0])



#HIS WAY THAT MAKES ACTUAL SENSE:
class PhraseTrigger(Trigger):
    def __init__(self, phrase):
        self.phrase = phrase
    def evaluate(self, story):
        return self.phrase in story.get_title() or\
               self.phrase in story.get_subject() or\
               self.phrase in story.get_summary()


#The in command is much more powerful than I thought and I would have benefitted from testing it
# c = 'abcdef'
# d = 'de'
# print d in c        #This is true, so it can deal with things that are in the middle of a string

# #======================
# # Part 3
# # Filtering
# #======================

def filter_stories(stories, triggerlist):
    """
    Takes in a list of NewsStory-s.
    Returns only those stories for whom
    a trigger in triggerlist fires.
    """
    filtered = []
    for i in stories:
        for j in triggerlist:
            # j = PhraseTrigger(j)        #In the testsuite this line must be commented out because triggers are inputted as PhraseTriggers already
            if j.evaluate(i):
                filtered += [i, ]
    return filtered

# c = [string.split(google[0].get_title())[1]]
# c += [string.split(google[1].get_title())[1]]
# print filter_stories(google, c)
# print filter_stories(google, c)[1].get_title()

#UNDERSTANDING ERROR:
#The above code isn't meant to take a list of strings and use them as triggers, but rather a list of trigger object which makes more sense
#Under this input condition the commented out line in filter_stories is unnecessary
#This gives more variation since it allows for or/and/not triggers to be implemented




# #======================
# # Part 4
# # User-Specified Triggers
# #======================
#
def readTriggerConfig(filename):
    """
    Returns a list of trigger objects
    that correspond to the rules set
    in the file filename
    """
    # Here's some code that we give you
    # to read in the file and eliminate
    # blank lines and comments
    triggerfile = open(filename, "r")
    all = [ line.rstrip() for line in triggerfile.readlines() ]
    lines = []
    for line in all:
        if len(line) == 0 or line[0] == '#':
            continue
        lines.append(line)
    # print lines
    dicttriggers = {}
    realtriggers = []
    for i in lines:
        if 'TITLE' in i: dicttriggers[string.split(i)[0]] = TitleTrigger(string.split(i)[2])
        if 'SUBJECT' in i: dicttriggers[string.split(i)[0]] = SubjectTrigger(string.split(i)[2])
        if 'SUMMARY' in i: dicttriggers[string.split(i)[0]] = SummaryTrigger(string.split(i)[2])
        if 'PHRASE' in i: dicttriggers[string.split(i)[0]] = PhraseTrigger((i)[len(string.split(i)[0]) + 8:])
    for i in lines:
        if 'AND' in i: dicttriggers[string.split(i)[0]] = AndTrigger(dicttriggers[string.split(i)[2]], dicttriggers[string.split(i)[3]])
        if 'OR' in i: dicttriggers[string.split(i)[0]] = OrTrigger(dicttriggers[string.split(i)[2]], dicttriggers[string.split(i)[3]])
    for i in lines:
        if 'ADD' in i:
            for n in range(1, len(string.split(i))):
                realtriggers +=[dicttriggers[string.split(i)[n]], ]
    return realtriggers


# print readTriggerConfig("/Users/paulsalvatore57/PycharmProjects/MIT600/Assignments/Assignment 5/triggers.txt")


#Len2
#TITLE: a single word.
#SUBJECT: a single word.
#SUMMARY: a single word.
#NOT: the name of the trigger that will be NOT'd.

#Len3
#AND: the names of the two other triggers that will be AND'd.
#OR: the names of the two other triggers that will be OR'd.

#Len >= 3
#PHRASE: a phrase.




# import thread
#
# def main_thread(p):
#     # A sample trigger list - you'll replace
#     # this with something more configurable in Problem 11
#     t1 = SubjectTrigger("Obama")
#     t2 = SummaryTrigger("MIT")
#     t3 = PhraseTrigger("Supreme Court")
#     t4 = OrTrigger(t2, t3)
#     triggerlist = [t1, t4]
#
#     # TODO: Problem 11
#     # After implementing readTriggerConfig, uncomment this line
#     #triggerlist = readTriggerConfig("triggers.txt")
#
#     guidShown = []
#
#     while True:
#         print "Polling..."
#
#         # Get stories from Google's Top Stories RSS news feed
#         stories = process("http://news.google.com/?output=rss")
#         # Get stories from Yahoo's Top Stories RSS news feed
#         stories.extend(process("http://rss.news.yahoo.com/rss/topstories"))
#
#         # Only select stories we're interested in
#         stories = filter_stories(stories, triggerlist)
#
#         # Don't print a story if we have already printed it before
#         newstories = []
#         for story in stories:
#             if story.get_guid() not in guidShown:
#                 newstories.append(story)
#
#         for story in newstories:
#             guidShown.append(story.get_guid())
#             p.newWindow(story)
#
#         print "Sleeping..."
#         time.sleep(SLEEPTIME)
#
# SLEEPTIME = 60 #seconds -- how often we poll
# if __name__ == '__main__':
#     p = Popup()
#     thread.start_new_thread(main_thread, (p,))
#     p.start()











