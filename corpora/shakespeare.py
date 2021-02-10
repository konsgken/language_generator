import os
import urllib.request
import codecs

DATA_DIR = 'data'
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

shakespeare_url = 'http://www.gutenberg.org/files/100/100-0.txt'
raw_shakespeare_data = os.path.join(DATA_DIR, 'shakespeare_raw.txt')
if not os.path.exists(raw_shakespeare_data):
    print('Downloading shakespeare corpus from %s' % shakespeare_url)
    urllib.request.urlretrieve(shakespeare_url, raw_shakespeare_data)

with codecs.open(raw_shakespeare_data, 'rb', 'utf-8') as f:
    shakespeare = f.readlines()

shakespeare = shakespeare[139:147417]


boilerplate = {u'<<THIS ELECTRONIC VERSION OF THE COMPLETE WORKS OF WILLIAM\r\n',
u'SHAKESPEARE IS COPYRIGHT 1990-1993 BY WORLD LIBRARY, INC., AND IS\r\n',
u'PROVIDED BY PROJECT GUTENBERG ETEXT OF ILLINOIS BENEDICTINE COLLEGE\r\n',
u'WITH PERMISSION.  ELECTRONIC AND MACHINE READABLE COPIES MAY BE\r\n',
u'DISTRIBUTED SO LONG AS SUCH COPIES (1) ARE FOR YOUR OR OTHERS\r\n',
u'PERSONAL USE ONLY, AND (2) ARE NOT DISTRIBUTED OR USED\r\n',
u'COMMERCIALLY.  PROHIBITED COMMERCIAL DISTRIBUTION INCLUDES BY ANY\r\n',
u'SERVICE THAT CHARGES FOR DOWNLOAD TIME OR FOR MEMBERSHIP.>>\r\n'}
shakespeare = [l for l in shakespeare if l not in boilerplate]


shakespeare_sonnets = os.path.join(DATA_DIR, 'shakespeare_sonnets.txt')
if not os.path.exists(shakespeare_sonnets):
    with codecs.open(shakespeare_sonnets, 'wb', 'utf-8') as f:
        print('Saving shakespeare sonnets file.')
        for i in range(2772):
            f.write(shakespeare[i])


shakespeare_plays = os.path.join(DATA_DIR, 'shakespeare_plays.txt')
if not os.path.exists(shakespeare_plays):
    with codecs.open(shakespeare_plays, 'wb', 'utf-8') as f:
        print('Saving shakespeare plays file.')
        for i in range(2773, len(shakespeare)):
            f.write(shakespeare[i])