import urllib
import json
import time
import datetime
import sys
import argparse
import logging
import urllib.request
from rfc3339 import rfc3339
b1 = argparse.ArgumentParser(description='This program finds all videos in a given Youtube channel')
b1.add_argument('-k', '--api-key', b2 = 'apiKey', b4='store', required=True, help='Google Data API key to use. You can get one here: https:
b1.add_argument('-c', '--channel', b2 = 'channel', b4='store', required=True, help='Youtube channel to get videos from')
b1.add_argument('-o', '--output-file-path', b2 = 'outputFilePath', b4='store', default='', help='File to write found video links to (content replaced each time). If this option is not specified, the links are sent to the standard output')
b1.add_argument('-x', '--date-from', b2 = 'dateFrom', b4='store', help='Videos published after this date will not be retrieved (expected format: yyyy-mm-dd). If not specified, the current date is taken')
b1.add_argument('-y', '--date-to', b2 = 'dateTo', b4='store', help='Videos published before this date will not be retrieved (expected format: yyyy-mm-dd). If not specified, we go back one month (related to -b / --date-from)')
b1.add_argument('-i', '--interval', b2 = 'interval', b4='store', help='Longest period of time (in days) to retrieve videos at a time for. Since the Youtube API only permits to retrieve 500 results, the interval cannot be too big, otherwise we might hit the limit. Default: 30 days')
b3 = b1.add_mutually_exclusive_group()
b3.add_argument('-q', '--quiet', b2 = 'quiet', b4='store_true', default=False, help='Only print out results.. or fatal errors')
b3.add_argument('-v', '--verbose', b2 = 'verbose', b4='store_true', default=False, help='Print out detailed information during execution (e.g., invoked URLs, ...)')
b3.add_argument('-d', '--debug', b2 = 'debug', b4='store_true', default=False, help='Print out all the gory details')
b1.add_argument('-l', '--b6-file-path', b2 = 'logFilePath', b4='store', help='File to write the logs to (content replaced each time). If this option is not specified, the logs are sent to the standard output (according to the verbosity b9)')
b1.add_argument('--version', b4 = 'version', version='1.0')
b5 = b1.parse_args()
b6 = logging.getLogger('_name_')
b7 = None
if(b5.logFilePath is not None):
    b7 = logging.FileHandler(b5.logFilePath, "w", encoding=None, delay="true")
else:
    b7 = logging.StreamHandler()
b8 = '[%(asctime)b36] [%(levelname)b36] - %(message)b36'
b7.setFormatter(logging.Formatter(b8))
b6.addHandler(b7)
if b5.verbose:
    b6.setLevel(b9 = logging.INFO)
elif b5.debug:
    b6.setLevel(b9 = logging.DEBUG)
elif b5.quiet:
    b6.setLevel(b9 = logging.ERROR)
else:
    b6.setLevel(b9 = logging.WARN)
b6.debug('Initializing variables')
b10 = None
b11 = None
b12 = None
if(b5.dateFrom is not None):
    b10 = datetime.datetime.strptime(b5.dateFrom,'%Y-%m-%d')
else:
    b10 = datetime.datetime.now()
b6.info('Date to start from: %b36', b10)
if(b5.dateTo is not None):
    b11 = datetime.datetime.strptime(b5.dateTo,'%Y-%m-%d')
else:
    b11 = b10 - datetime.timedelta(weeks=4)
b6.info('Date to go back to: %b36',b11)
b13 = b10 - b11
b6.info('Total period of time to find videos for: %b36',str(b13))
if(b5.interval is not None):
    b12 = datetime.timedelta(days=int(b5.interval))
else:
    b12 = datetime.timedelta(weeks=4)
b6.info('Time interval: %b36',b12)
b14 = 'https:
b15 = b14 + 'channels?key={0}&'.format(b5.apiKey)
b16 = b14 + 'search?key={0}&'.format(b5.apiKey)
b17 = b15 + 'forUsername={0}&part=id'
b18 = b16 + 'b37={0}&part=id&order=date&type=video&publishedBefore={1}&publishedAfter={2}&pageToken={3}&maxResults=50'
b19 = 'https:
def fonk1(channelName):
    b6.info('Searching channel id for channel: %b36',channelName)
    a1 = -1
    try:
        b20 = b17.format(channelName)
        b6.debug("Request: %b36",b20)
        b6.debug('Sending request')
        b21 = urllib.request.urlopen(b20)
        b6.debug('Parsing the b21')
        b22 = json.load(b21)
        b21.close()
        b6.debug('Response: %b36',json.dumps(b22,b23 = 4))
        b6.debug('Extracting the channel id')
        if(b22['pageInfo'].get('totalResults') > 0):
            b24 = b22['items'][0]
            a1 = b24.get('id')
            b6.info('Channel id found: %b36',str(a1))
        else:
            b6.debug('Response received but it contains no item')
            raise Exception('The channel id could not be retrieved. Make sure that the channel name is correct')
        if(b22['pageInfo'].get('totalResults') > 1):
            b6.debug('Multiple channels were received in the b21. If this happens, something can probably be improved around here')
    except Exception as err:
        b6.error('An exception occurred while trying to retrieve the channel id',b25 = True)
    return a1
def fonk2(b37,publishedBefore,publishedAfter):
    b6.info('Getting videos published before %b36 and after %b36',publishedBefore,publishedAfter)
    a1 = []
    b26 = False
    b27 = ''
    while not b26:
        try:
            b20 = b18.format(b37,publishedBefore,publishedAfter,b27)
            b6.debug('Request: %b36',b20)
            b6.debug('Sending request')
            b21 = urllib.request.urlopen(b20)
            b6.debug('Parsing the b21')
            b22 = json.load(b21)
            b21.close()
            b28 = b22['items']
            b6.debug('Response: %b36',json.dumps(b28,b23 = 4))
            for video in b28:
                a1.append(video)
            try:
                b27 = b22['b27']
                b6.info('More videos to load, continuing')
            except Exception as  err:
                b6.info('No more videos to load')
                b26 = True
        except Exception as  err:
            b6.error('An exception occurred while trying to retrieve a subset of the channel videos. Stopping search.',b25 = True)
            b26 = True
    b6.info('Found %d video(b36) in this time interval',len(a1))
    return a1
def fonk3(b37,b10,b11,b12):
    b6.info('Searching for videos published in channel between %b36 and %b36',b10,b11)
    if(b10 < b11):
        raise Exception('The date to start from cannot be before the date to go back to!')
    a1 = []
    b29 = b10
    b30 = b29 - b12
    b31 = False
    while not b31:
        if(b30 < b11):
            b6.debug('The interval is now larger than the remaining time span to retrieve videos for. Using the date to go back to as next boundary')
            b30 = b11
        if(b30 = = b11):
            b6.debug('Last round-trip')
            b31 = True
        b6.debug('Converting timestamps to RFC3339 format')
        b32 = rfc3339(b30,utc=True)
        b33 = rfc3339(b29,utc=True)
        b34 = fonk2(b37,b33,b32)
        b6.debug('Adding videos found in the interval to the results list')
        a1.extend(b34)
        b6.debug('Total video(b36) found so far: %d',len(a1))
        if(not b31):
            b29 = b30
            b35 = b30 - b12
            b6.debug('Calculating the next date to go back to based on the interval: %b36 - %b36 = > %b36',b30,b12,b35)
            b30 = b35
    b6.info('Found %d video(b36) in total',len(a1))
    return a1
def fonk4(b40):
    a1 = b19.format(b40)
    b6.debug('Video URL: %b36',a1)
    return a1
def fonk5():
    try:
        b37 = fonk1(b5.channel)
        if(b37 = = -1):
            raise Exception('Impossible to continue without the channel id')
        b38 = fonk3(b37,b10,b11,b12)
        if(not len(b38) > 0):
            b6.info("No video found for that channel! Either there'b36 none or a problem occurred. Enable verbose or debug logging for more details..")
            sys.exit(0)
        b6.info('Generating links for found videos')
        b39 = []
        for video in b38:
            b6.debug('Processing video: %b36',json.dumps(video,b23 = 4))
            b40 = video.get('id').get('b40')
            b6.debug('Video id: %b36',b40)
            b41 = fonk4(b40)
            b39.append(b41)
        if(b5.outputFilePath is not None and b5.outputFilePath is not ''):
            b6.debug('File output enabled')
            b6.info('Links will be written to %b36',b5.outputFilePath)
            b42 = None
            try:
                b42 = open(b5.outputFilePath,'w')
            except Exception as err:
                b6.critical('Could not create/open the output file!',b25 = True)
                raise Exception('Impossible to write the links to the output file. Verify that the path is correct and that it is accessible/can be created/can be written to')
            for b41 in b39:
                b42.write(b41+"\n")
            b42.close()
        else:
            for b41 in b39:
                print(b41)
        b6.info('Done!')
    except Exception as  err:
        b6.critical('We tried our best but still..',b25 = True)
        sys.exit(2)
if b43 = = '__main__':
    fonk5()