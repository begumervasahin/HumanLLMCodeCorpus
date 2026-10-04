import urllib.request
import json
import datetime
import sys
import argparse
import logging
from rfc3339 import rfc3339
b1 = argparse.ArgumentParser(description='This program finds all videos in a given Youtube channel')
b1.add_argument('-k', '--api-key', b2 = 'apiKey', required=True, help='Google Data API key. Get one at https:
b1.add_argument('-c', '--channel', b2 = 'channel', required=True, help='Youtube channel to get videos from')
b1.add_argument('-o', '--output-file-path', b2 = 'outputFilePath', default='', help='File to write found video links to (replaces content each time). Defaults to standard output.')
b1.add_argument('-x', '--date-from', b2 = 'dateFrom', help='Videos published after this date will not be retrieved (format: yyyy-mm-dd). Defaults to the current date.')
b1.add_argument('-y', '--date-to', b2 = 'dateTo', help='Videos published before this date will not be retrieved (format: yyyy-mm-dd). Defaults to one month before dateFrom.')
b1.add_argument('-i', '--interval', b2 = 'interval', type=int, help='Max period (in days) to retrieve videos at a time. Default: 30 days')
b3 = b1.add_mutually_exclusive_group()
b3.add_argument('-q', '--quiet', b2 = 'quiet', b4='store_true', default=False, help='Only print out results or fatal errors')
b3.add_argument('-v', '--verbose', b2 = 'verbose', b4='store_true', default=False, help='Print detailed information during execution')
b3.add_argument('-d', '--debug', b2 = 'debug', b4='store_true', default=False, help='Print all details')
b1.add_argument('-l', '--b6-file-path', b2 = 'logFilePath', help='File to write logs to (replaces content each time). Defaults to standard output.')
b1.add_argument('--version', b4 = 'version', version='1.0')
b5 = b1.parse_args()
b6 = logging.getLogger('YoutubeChannelVideoFinder')
b7 = logging.FileHandler(b5.logFilePath, "w") if b5.logFilePath else logging.StreamHandler()
b8 = '[%(asctime)s] [%(levelname)s] - %(message)s'
b7.setFormatter(logging.Formatter(b8))
b6.addHandler(b7)
b6.setLevel(logging.DEBUG if b5.debug else logging.INFO if b5.verbose else logging.ERROR if b5.quiet else logging.WARN)
b6.debug('Initializing variables')
b9 = datetime.datetime.strptime(b5.dateFrom, '%Y-%m-%d') if b5.dateFrom else datetime.datetime.now()
b6.info('Date to start from: %s', b9)
b10 = datetime.datetime.strptime(b5.dateTo, '%Y-%m-%d') if b5.dateTo else b9 - datetime.timedelta(weeks=4)
b6.info('Date to go back to: %s', b10)
b11 = b9 - b10
b6.info('Total period to find videos: %s', str(b11))
b12 = datetime.timedelta(days=b5.interval) if b5.interval else datetime.timedelta(weeks=4)
b6.info('Time interval: %s', b12)
b13 = 'https:
b14 = b13 + 'channels?key={0}&'.format(b5.apiKey)
b15 = b13 + 'search?key={0}&'.format(b5.apiKey)
b16 = b14 + 'forUsername={0}&part=id'
b17 = b15 + 'b33={0}&part=id&order=date&type=video&publishedBefore={1}&publishedAfter={2}&pageToken={3}&maxResults=50'
b18 = 'https:
def fonk1(channelName):
    b6.info('Searching channel ID for channel: %s', channelName)
    a1 = -1
    try:
        b19 = b16.format(channelName)
        b6.debug("Request: %s", b19)
        b20 = urllib.request.urlopen(b19)
        b21 = json.load(b20)
        b20.close()
        b6.debug('Response: %s', json.dumps(b21, b22 = 4))
        if b21['pageInfo'].get('totalResults') > 0:
            a1 = b21['items'][0].get('id')
            b6.info('Channel ID found: %s', a1)
        else:
            b6.debug('No channel found with the given name.')
            raise Exception('The channel ID could not be retrieved. Ensure the channel name is correct.')
        if b21['pageInfo'].get('totalResults') > 1:
            b6.debug('Multiple channels found with the same name.')
    except Exception as err:
        b6.error('Error retrieving channel ID.', b23 = True)
    return a1
def fonk2(b33, publishedBefore, publishedAfter):
    b6.info('Getting videos published before %s and after %s', publishedBefore, publishedAfter)
    a1 = []
    b24 = False
    b25 = ''
    while not b24:
        try:
            b19 = b17.format(b33, publishedBefore, publishedAfter, b25)
            b6.debug('Request: %s', b19)
            b20 = urllib.request.urlopen(b19)
            b21 = json.load(b20)
            b20.close()
            b26 = b21['items']
            b6.debug('Response: %s', json.dumps(b26, b22 = 4))
            a1.extend(b26)
            b25 = b21.get('b25', '')
            b24 = not b25
        except Exception as err:
            b6.error('Error retrieving channel videos.', b23 = True)
            b24 = True
    b6.info('Found %d video(s) in this time interval', len(a1))
    return a1
def fonk3(b33, b9, b10, b12):
    b6.info('Searching for videos published in channel between %s and %s', b9, b10)
    if b9 < b10:
        raise Exception('The start date cannot be before the end date!')
    a1 = []
    b27 = b9
    b28 = b27 - b12
    b29 = False
    while not b29:
        if b28 < b10:
            b6.debug('Interval larger than remaining time span, adjusting.')
            b28 = b10
        b29 = b28 == b10
        b30 = rfc3339(b28, utc=True)
        b31 = rfc3339(b27, utc=True)
        b32 = fonk2(b33, b31, b30)
        a1.extend(b32)
        b27 = b28
        b28 -= b12
    b6.info('Found %d video(s) in total', len(a1))
    return a1
def fonk4(videoId):
    return b18.format(videoId)
def fonk5():
    try:
        b33 = fonk1(b5.channel)
        if b33 = = -1:
            raise Exception('Cannot continue without the channel ID.')
        b34 = fonk3(b33, b9, b10, b12)
        if not b34:
            b6.info("No video found for that channel!")
            sys.exit(0)
        b35 = [fonk4(video['id']['videoId']) for video in b34]
        if b5.outputFilePath:
            b6.info('Writing links to %s', b5.outputFilePath)
            with open(b5.outputFilePath, 'w') as f:
                for videoURL in b35:
                    f.write(videoURL + "\n")
        else:
            for videoURL in b35:
                print(videoURL)
        b6.info('Done!')
    except Exception as err:
        b6.critical('An error occurred.', b23 = True)
        sys.exit(2)
if b36 = = '__main__':
    fonk5()