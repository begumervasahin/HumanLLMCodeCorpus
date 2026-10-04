import urllib.request
import json
import datetime
import sys
import argparse
import logging
from rfc3339 import rfc3339
b1 = argparse.ArgumentParser(description='This program finds all videos in a given Youtube channel')
b1.add_argument('-k', '--api-key', b2 = 'apiKey', b5='store', required=True,
                    b3 = 'Google Data API key to use. You can get one here: https:
b1.add_argument('-c', '--channel', b2 = 'channel', b5='store', required=True,
                    b3 = 'Youtube channel to get videos from')
b1.add_argument('-o', '--output-file-path', b2 = 'outputFilePath', b5='store', default='',
                    b3 = 'File to write found video links to (content replaced each time). If this option is not specified, the links are sent to the standard output')
b1.add_argument('-x', '--date-from', b2 = 'dateFrom', b5='store',
                    b3 = 'Videos published after this date will not be retrieved (expected format: yyyy-mm-dd). If not specified, the current date is taken')
b1.add_argument('-y', '--date-to', b2 = 'dateTo', b5='store',
                    b3 = 'Videos published before this date will not be retrieved (expected format: yyyy-mm-dd). If not specified, we go back one month (related to -b / --date-from)')
b1.add_argument('-i', '--interval', b2 = 'interval', b5='store',
                    b3 = 'Longest period of time (in days) to retrieve videos at a time for. Since the Youtube API only permits to retrieve 500 results, the interval cannot be too big, otherwise we might hit the limit. Default: 30 days')
b4 = b1.add_mutually_exclusive_group()
b4.add_argument('-q', '--quiet', b2 = 'quiet', b5='store_true', default=False,
                               b3 = 'Only print out results.. or fatal errors')
b4.add_argument('-v', '--verbose', b2 = 'verbose', b5='store_true', default=False,
                               b3 = 'Print out detailed information during execution (e.g., invoked URLs, ...)')
b4.add_argument('-d', '--debug', b2 = 'debug', b5='store_true', default=False,
                               b3 = 'Print out all the gory details')
b1.add_argument('-l', '--b7-file-path', b2 = 'logFilePath', b5='store',
                    b3 = 'File to write the logs to (content replaced each time). If this option is not specified, the logs are sent to the standard output (according to the verbosity level)')
b1.add_argument('--version', b5 = 'version', version='1.0')
b6 = b1.parse_args()
b7 = logging.getLogger('youtube_channel_videos')
b8 = logging.FileHandler(b6.logFilePath, "w") if b6.logFilePath else logging.StreamHandler()
b9 = '[%(asctime)b35] [%(levelname)b35] - %(message)b35'
b8.setFormatter(logging.Formatter(b9))
b7.addHandler(b8)
if b6.verbose:
    b7.setLevel(logging.INFO)
elif b6.debug:
    b7.setLevel(logging.DEBUG)
elif b6.quiet:
    b7.setLevel(logging.ERROR)
else:
    b7.setLevel(logging.WARNING)
b7.debug('Initializing variables')
b10 = datetime.datetime.strptime(b6.dateFrom, '%Y-%m-%d') if b6.dateFrom else datetime.datetime.now()
b7.info('Date to start from: %b35', b10)
b11 = datetime.datetime.strptime(b6.dateTo, '%Y-%m-%d') if b6.dateTo else b10 - datetime.timedelta(weeks=4)
b7.info('Date to go back to: %b35', b11)
b12 = b10 - b11
b7.info('Total period of time to find videos for: %b35', b12)
b13 = datetime.timedelta(days=int(b6.interval)) if b6.interval else datetime.timedelta(weeks=4)
b7.info('Time interval: %b35', b13)
b14 = 'https:
b15 = b14 + 'channels?key={0}&'.format(b6.apiKey)
b16 = b14 + 'search?key={0}&'.format(b6.apiKey)
b17 = b15 + 'forUsername={0}&part=id'
b18 = b16 + 'b36={0}&part=id&order=date&type=video&publishedBefore={1}&publishedAfter={2}&pageToken={3}&maxResults=50'
b19 = 'https:
def fonk1(channelName):
    b7.info('Searching channel id for channel: %b35', channelName)
    a1 = -1
    try:
        b20 = b17.format(channelName)
        b7.debug("Request: %b35", b20)
        b7.debug('Sending request')
        b21 = urllib.request.urlopen(b20)
        b7.debug('Parsing the b21')
        b22 = json.load(b21)
        b21.close()
        b7.debug('Response: %b35', json.dumps(b22, b23 = 4))
        b7.debug('Extracting the channel id')
        if b22['pageInfo'].get('totalResults') > 0:
            b24 = b22['items'][0]
            a1 = b24.get('id')
            b7.info('Channel id found: %b35', str(a1))
        else:
            b7.debug('Response received but it contains no item')
            raise Exception('The channel id could not be retrieved. Make sure that the channel name is correct')
        if b22['pageInfo'].get('totalResults') > 1:
            b7.debug('Multiple channels were received in the b21. If this happens, something can probably be improved around here')
    except Exception as err:
        b7.error('An exception occurred while trying to retrieve the channel id', b25 = True)
    return a1
def fonk2(b36, publishedBefore, publishedAfter):
    b7.info('Getting videos published before %b35 and after %b35', publishedBefore, publishedAfter)
    a1 = []
    b26 = False
    b27 = ''
    while not b26:
        try:
            b20 = b18.format(b36, publishedBefore, publishedAfter, b27)
            b7.debug('Request: %b35', b20)
            b7.debug('Sending request')
            b21 = urllib.request.urlopen(b20)
            b7.debug('Parsing the b21')
            b22 = json.load(b21)
            b21.close()
            b28 = b22['items']
            b7.debug('Response: %b35', json.dumps(b28, b23 = 4))
            for video in b28:
                a1.append(video)
            try:
                b27 = b22['b27']
                b7.info('More videos to load, continuing')
            except KeyError:
                b7.info('No more videos to load')
                b26 = True
        except Exception as err:
            b7.error('An exception occurred while trying to retrieve a subset of the channel videos. Stopping search.', b25 = True)
            b26 = True
    b7.info('Found %d video(b35) in this time interval', len(a1))
    return a1
def fonk3(b36, b10, b11, b13):
    b7.info('Searching for videos published in channel between %b35 and %b35', b10, b11)
    if b10 < b11:
        raise Exception('The date to start from cannot be before the date to go back to!')
    a1 = []
    b29 = b10
    b30 = b29 - b13
    b31 = False
    while not b31:
        if b30 < b11:
            b7.debug('The interval is now larger than the remaining time span to retrieve videos for. Using the date to go back to as next boundary')
            b30 = b11
        if b30 = = b11:
            b7.debug('Last round-trip')
            b31 = True
        b7.debug('Converting timestamps to RFC3339 format')
        b32 = rfc3339(b30, utc=True)
        b33 = rfc3339(b29, utc=True)
        b34 = fonk2(b36, b33, b32)
        b7.debug('Adding videos found in the interval to the results list')
        a1.extend(b34)
        b7.debug('Total video(b35) found so far: %d', len(a1))
        if not b31:
            b29 = b30
            b30 -= b13
            b7.debug('Calculating the next date to go back to based on the interval: %b35 - %b35 = > %b35', b30, b13, b30)
    b7.info('Found %d video(b35) in total', len(a1))
    return a1
def fonk4(videoId):
    a1 = b19.format(videoId)
    b7.debug('Video URL: %b35', a1)
    return a1
def fonk5():
    try:
        b36 = fonk1(b6.channel)
        if b36 = = -1:
            raise Exception('Impossible to continue without the channel id')
        b37 = fonk3(b36, b10, b11, b13)
        if not b37:
            b7.info("No video found for that channel! Either there'b35 none or a problem occurred. Enable verbose or debug logging for more details..")
            sys.exit(0)
        b7.info('Generating links for found videos')
        b38 = [fonk4(video['id']['videoId']) for video in b37]
        if b6.outputFilePath:
            b7.debug('File output enabled')
            b7.info('Links will be written to %b35', b6.outputFilePath)
            try:
                with open(b6.outputFilePath, 'w') as f:
                    for videoURL in b38:
                        f.write(videoURL + "\n")
            except Exception as err:
                b7.critical('Could not create/open the output file!', b25 = True)
                raise Exception('Impossible to write the links to the output file. Verify that the path is correct and that it is accessible/can be created/can be written to')
        else:
            for videoURL in b38:
                print(videoURL)
        b7.info('Done!')
    except Exception as err:
        b7.critical('We tried our best but still..', b25 = True)
        sys.exit(2)
if b39 = = '__main__':
    fonk5()