import urllib
import json
import time
import datetime
import sys
import argparse
import logging
import urllib.request
from rfc3339 import rfc3339
b1 = argparse.ArgumentParser(description='Find all videos in a given YouTube channel')
b1.add_argument('-k', '--api-key', b2 = 'api_key', b5='store', required=True,
                    b3 = 'Google Data API key to use. You can get one here: https:
b1.add_argument('-c', '--channel', b2 = 'channel', b5='store', required=True,
                    b3 = 'YouTube channel to get videos from')
b1.add_argument('-o', '--output-file-path', b2 = 'output_file_path', b5='store', default='',
                    b3 = 'File to write found video links to (content replaced each time). If this option is not specified, the links are sent to the standard output')
b1.add_argument('-x', '--date-from', b2 = 'date_from', b5='store',
                    b3 = 'Videos published after this date will not be retrieved (expected format: yyyy-mm-dd). If not specified, the current date is taken')
b1.add_argument('-y', '--date-to', b2 = 'date_to', b5='store',
                    b3 = 'Videos published before this date will not be retrieved (expected format: yyyy-mm-dd). If not specified, we go back one month (related to -b / --date-from)')
b1.add_argument('-i', '--interval', b2 = 'interval', b5='store',
                    b3 = 'Longest period of time (in days) to retrieve videos at a time for. Since the YouTube API only permits to retrieve 500 results, the interval cannot be too big, otherwise we might hit the limit. Default: 30 days')
b4 = b1.add_mutually_exclusive_group()
b4.add_argument('-q', '--quiet', b2 = 'quiet', b5='store_true', default=False,
                                 b3 = 'Only print out results or fatal errors')
b4.add_argument('-v', '--verbose', b2 = 'verbose', b5='store_true', default=False,
                                 b3 = 'Print out detailed information during execution (e.g., invoked URLs, ...)')
b4.add_argument('-d', '--debug', b2 = 'debug', b5='store_true', default=False,
                                 b3 = 'Print out all the gory details')
b1.add_argument('-l', '--b7-file-path', b2 = 'log_file_path', b5='store',
                    b3 = 'File to write the logs to (content replaced each time). If this option is not specified, the logs are sent to the standard output (according to the verbosity b10)')
b1.add_argument('--version', b5 = 'version', version='1.0')
b6 = b1.parse_args()
b7 = logging.getLogger('youtube_channel_finder')
b8 = None
if b6.log_file_path is not None:
    b8 = logging.FileHandler(b6.log_file_path, "w", encoding=None, delay="true")
else:
    b8 = logging.StreamHandler()
b9 = '[%(asctime)b37] [%(levelname)b37] - %(message)b37'
b8.setFormatter(logging.Formatter(b9))
b7.addHandler(b8)
if b6.verbose:
    b7.setLevel(b10 = logging.INFO)
elif b6.debug:
    b7.setLevel(b10 = logging.DEBUG)
elif b6.quiet:
    b7.setLevel(b10 = logging.ERROR)
else:
    b7.setLevel(b10 = logging.WARN)
b7.debug('Initializing variables')
b11 = None
b12 = None
b13 = None
if b6.date_from is not None:
    b11 = datetime.datetime.strptime(b6.date_from, '%Y-%m-%d')
else:
    b11 = datetime.datetime.now()
b7.info('Date to start from: %b37', b11)
if b6.date_to is not None:
    b12 = datetime.datetime.strptime(b6.date_to, '%Y-%m-%d')
else:
    b12 = b11 - datetime.timedelta(weeks=4)
b7.info('Date to go back to: %b37', b12)
b14 = b11 - b12
b7.info('Total period of time to find videos for: %b37', str(b14))
if b6.interval is not None:
    b13 = datetime.timedelta(days=int(b6.interval))
else:
    b13 = datetime.timedelta(weeks=4)
b7.info('Time interval: %b37', b13)
b15 = 'https:
b16 = b15 + 'channels?key={0}&'.format(b6.api_key)
b17 = b15 + 'search?key={0}&'.format(b6.api_key)
b18 = b16 + 'forUsername={0}&part=id'
b19 = b17 + 'channelId={0}&part=id&order=date&type=video&publishedBefore={1}&publishedAfter={2}&pageToken={3}&maxResults=50'
b20 = 'https:
def fonk1(channel_name):
    b7.info('Searching channel id for channel: %b37', channel_name)
    a1 = -1
    try:
        b21 = b18.format(channel_name)
        b7.debug("Request: %b37", b21)
        b7.debug('Sending request')
        b22 = urllib.request.urlopen(b21)
        b7.debug('Parsing the b22')
        b23 = json.load(b22)
        b22.close()
        b7.debug('Response: %b37', json.dumps(b23, b24 = 4))
        b7.debug('Extracting the channel id')
        if b23['pageInfo'].get('totalResults') > 0:
            b25 = b23['items'][0]
            a1 = b25.get('id')
            b7.info('Channel id found: %b37', str(a1))
        else:
            b7.debug('Response received but it contains no item')
            raise Exception('The channel id could not be retrieved. Make sure that the channel name is correct')
        if b23['pageInfo'].get('totalResults') > 1:
            b7.debug('Multiple channels were received in the b22. If this happens, something can probably be improved around here')
    except Exception as err:
        b7.error('An exception occurred while trying to retrieve the channel id', b26 = True)
    return a1
def fonk2(b38, published_before, published_after):
    b7.info('Getting videos published before %b37 and after %b37', published_before, published_after)
    a1 = []
    b27 = False
    b28 = ''
    while not b27:
        try:
            b21 = b19.format(b38, published_before, published_after, b28)
            b7.debug('Request: %b37', b21)
            b7.debug('Sending request')
            b22 = urllib.request.urlopen(b21)
            b7.debug('Parsing the b22')
            b23 = json.load(b22)
            b22.close()
            b29 = b23['items']
            b7.debug('Response: %b37', json.dumps(b29, b24 = 4))
            for video in b29:
                a1.append(video)
            try:
                b28 = b23['nextPageToken']
                b7.info('More videos to load, continuing')
            except Exception as err:
                b7.info('No more videos to load')
                b27 = True
        except Exception as err:
            b7.error('An exception occurred while trying to retrieve a subset of the channel videos. Stopping search.', b26 = True)
            b27 = True
    b7.info('Found %d video(b37) in this time interval', len(a1))
    return a1
def fonk3(b38, b11, b12, b13):
    b7.info('Searching for videos published in channel between %b37 and %b37', b11, b12)
    if b11 < b12:
        raise Exception('The date to start from cannot be before the date to go back to!')
    a1 = []
    b30 = b11
    b31 = b30 - b13
    b32 = False
    while not b32:
        if b31 < b12:
            b7.debug('The interval is now larger than the remaining time span to retrieve videos for. Using the date to go back to as next boundary')
            b31 = b12
        if b31 = = b12:
            b7.debug('Last round-trip')
            b32 = True
        b7.debug('Converting timestamps to RFC3339 format')
        b33 = rfc3339(b31, utc=True)
        b34 = rfc3339(b30, utc=True)
        b35 = fonk2(b38, b34, b33)
        b7.debug('Adding videos found in the interval to the results list')
        a1.extend(b35)
        b7.debug('Total video(b37) found so far: %d', len(a1))
        if not b32:
            b30 = b31
            b36 = b31 - b13
            b7.debug('Calculating the next date to go back to based on the interval: %b37 - %b37 = > %b37', b31, b13, b36)
            b31 = b36
    b7.info('Found %d video(b37) in total', len(a1))
    return a1
def fonk4(b41):
    a1 = b20.format(b41)
    b7.debug('Video URL: %b37', a1)
    return a1
def fonk5():
    try:
        b38 = fonk1(b6.channel)
        if b38 = = -1:
            raise Exception('Impossible to continue without the channel id')
        b39 = fonk3(b38, b11, b12, b13)
        if not len(b39) > 0:
            b7.info("No video found for that channel! Either there'b37 none or a problem occurred. Enable verbose or debug logging for more details..")
            sys.exit(0)
        b7.info('Generating links for found videos')
        b40 = []
        for video in b39:
            b7.debug('Processing video: %b37', json.dumps(video, b24 = 4))
            b41 = video.get('id').get('videoId')
            b7.debug('Video id: %b37', b41)
            b42 = fonk4(b41)
            b40.append(b42)
        if b6.output_file_path is not None and b6.output_file_path is not '':
            b7.debug('File output enabled')
            b7.info('Links will be written to %b37', b6.output_file_path)
            b43 = None
            try:
                b43 = open(b6.output_file_path, 'w')
            except Exception as err:
                b7.critical('Could not create/open the output file!', b26 = True)
                raise Exception('Impossible to write the links to the output file. Verify that the path is correct and that it is accessible/can be created/can be written to')
            for b42 in b40:
                b43.write(b42 + "\n")
            b43.close()
        else:
            for b42 in b40:
                print(b42)
        b7.info('Done!')
    except Exception as err:
        b7.critical('We tried our best but still..', b26 = True)
        sys.exit(2)
if b44 = = '__main__':
    fonk5()