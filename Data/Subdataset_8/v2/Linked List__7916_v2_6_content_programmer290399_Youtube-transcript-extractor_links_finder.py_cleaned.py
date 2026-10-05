import urllib
import json
import time
import datetime
import sys
import argparse
import logging
import urllib.request
from rfc3339 import rfc3339
parser = argparse.ArgumentParser(description='Find all videos in a given YouTube channel')
parser.add_argument('-k', '--api-key', dest='api_key', action='store', required=True,
                    help='Google Data API key to use. You can get one here: https:
parser.add_argument('-c', '--channel', dest='channel', action='store', required=True,
                    help='YouTube channel to get videos from')
parser.add_argument('-o', '--output-file-path', dest='output_file_path', action='store', default='',
                    help='File to write found video links to (content replaced each time). If this option is not specified, the links are sent to the standard output')
parser.add_argument('-x', '--date-from', dest='date_from', action='store',
                    help='Videos published after this date will not be retrieved (expected format: yyyy-mm-dd). If not specified, the current date is taken')
parser.add_argument('-y', '--date-to', dest='date_to', action='store',
                    help='Videos published before this date will not be retrieved (expected format: yyyy-mm-dd). If not specified, we go back one month (related to -b / --date-from)')
parser.add_argument('-i', '--interval', dest='interval', action='store',
                    help='Longest period of time (in days) to retrieve videos at a time for. Since the YouTube API only permits to retrieve 500 results, the interval cannot be too big, otherwise we might hit the limit. Default: 30 days')
output_detail_level = parser.add_mutually_exclusive_group()
output_detail_level.add_argument('-q', '--quiet', dest='quiet', action='store_true', default=False,
                                 help='Only print out results or fatal errors')
output_detail_level.add_argument('-v', '--verbose', dest='verbose', action='store_true', default=False,
                                 help='Print out detailed information during execution (e.g., invoked URLs, ...)')
output_detail_level.add_argument('-d', '--debug', dest='debug', action='store_true', default=False,
                                 help='Print out all the gory details')
parser.add_argument('-l', '--log-file-path', dest='log_file_path', action='store',
                    help='File to write the logs to (content replaced each time). If this option is not specified, the logs are sent to the standard output (according to the verbosity level)')
parser.add_argument('--version', action='version', version='1.0')
args = parser.parse_args()
log = logging.getLogger('youtube_channel_finder')
handler = None
if args.log_file_path is not None:
    handler = logging.FileHandler(args.log_file_path, "w", encoding=None, delay="true")
else:
    handler = logging.StreamHandler()
log_format = '[%(asctime)s] [%(levelname)s] - %(message)s'
handler.setFormatter(logging.Formatter(log_format))
log.addHandler(handler)
if args.verbose:
    log.setLevel(level=logging.INFO)
elif args.debug:
    log.setLevel(level=logging.DEBUG)
elif args.quiet:
    log.setLevel(level=logging.ERROR)
else:
    log.setLevel(level=logging.WARN)
log.debug('Initializing variables')
date_to_start_from = None
date_to_go_back_to = None
time_interval = None
if args.date_from is not None:
    date_to_start_from = datetime.datetime.strptime(args.date_from, '%Y-%m-%d')
else:
    date_to_start_from = datetime.datetime.now()
log.info('Date to start from: %s', date_to_start_from)
if args.date_to is not None:
    date_to_go_back_to = datetime.datetime.strptime(args.date_to, '%Y-%m-%d')
else:
    date_to_go_back_to = date_to_start_from - datetime.timedelta(weeks=4)
log.info('Date to go back to: %s', date_to_go_back_to)
total_time_period = date_to_start_from - date_to_go_back_to
log.info('Total period of time to find videos for: %s', str(total_time_period))
if args.interval is not None:
    time_interval = datetime.timedelta(days=int(args.interval))
else:
    time_interval = datetime.timedelta(weeks=4)
log.info('Time interval: %s', time_interval)
youtube_api_url = 'https:
youtube_channels_api_url = youtube_api_url + 'channels?key={0}&'.format(args.api_key)
youtube_search_api_url = youtube_api_url + 'search?key={0}&'.format(args.api_key)
request_parameters_channel_id = youtube_channels_api_url + 'forUsername={0}&part=id'
request_channel_videos_info = youtube_search_api_url + 'channelId={0}&part=id&order=date&type=video&publishedBefore={1}&publishedAfter={2}&pageToken={3}&maxResults=50'
youtube_video_url = 'https:
def get_channel_id(channel_name):
    log.info('Searching channel id for channel: %s', channel_name)
    ret_val = -1
    try:
        url = request_parameters_channel_id.format(channel_name)
        log.debug("Request: %s", url)
        log.debug('Sending request')
        response = urllib.request.urlopen(url)
        log.debug('Parsing the response')
        response_as_json = json.load(response)
        response.close()
        log.debug('Response: %s', json.dumps(response_as_json, indent=4))
        log.debug('Extracting the channel id')
        if response_as_json['pageInfo'].get('totalResults') > 0:
            returned_info = response_as_json['items'][0]
            ret_val = returned_info.get('id')
            log.info('Channel id found: %s', str(ret_val))
        else:
            log.debug('Response received but it contains no item')
            raise Exception('The channel id could not be retrieved. Make sure that the channel name is correct')
        if response_as_json['pageInfo'].get('totalResults') > 1:
            log.debug('Multiple channels were received in the response. If this happens, something can probably be improved around here')
    except Exception as err:
        log.error('An exception occurred while trying to retrieve the channel id', exc_info=True)
    return ret_val
def get_channel_videos_published_in_interval(channel_id, published_before, published_after):
    log.info('Getting videos published before %s and after %s', published_before, published_after)
    ret_val = []
    found_all = False
    next_page_token = ''
    while not found_all:
        try:
            url = request_channel_videos_info.format(channel_id, published_before, published_after, next_page_token)
            log.debug('Request: %s', url)
            log.debug('Sending request')
            response = urllib.request.urlopen(url)
            log.debug('Parsing the response')
            response_as_json = json.load(response)
            response.close()
            returned_videos = response_as_json['items']
            log.debug('Response: %s', json.dumps(returned_videos, indent=4))
            for video in returned_videos:
                ret_val.append(video)
            try:
                next_page_token = response_as_json['nextPageToken']
                log.info('More videos to load, continuing')
            except Exception as err:
                log.info('No more videos to load')
                found_all = True
        except Exception as err:
            log.error('An exception occurred while trying to retrieve a subset of the channel videos. Stopping search.', exc_info=True)
            found_all = True
    log.info('Found %d video(s) in this time interval', len(ret_val))
    return ret_val
def get_channel_videos(channel_id, date_to_start_from, date_to_go_back_to, time_interval):
    log.info('Searching for videos published in channel between %s and %s', date_to_start_from, date_to_go_back_to)
    if date_to_start_from < date_to_go_back_to:
        raise Exception('The date to start from cannot be before the date to go back to!')
    ret_val = []
    start_from = date_to_start_from
    go_back_to = start_from - time_interval
    done = False
    while not done:
        if go_back_to < date_to_go_back_to:
            log.debug('The interval is now larger than the remaining time span to retrieve videos for. Using the date to go back to as next boundary')
            go_back_to = date_to_go_back_to
        if go_back_to == date_to_go_back_to:
            log.debug('Last round-trip')
            done = True
        log.debug('Converting timestamps to RFC3339 format')
        go_back_to_rfc3339 = rfc3339(go_back_to, utc=True)
        start_from_rfc3339 = rfc3339(start_from, utc=True)
        videos_published_in_interval = get_channel_videos_published_in_interval(channel_id, start_from_rfc3339, go_back_to_rfc3339)
        log.debug('Adding videos found in the interval to the results list')
        ret_val.extend(videos_published_in_interval)
        log.debug('Total video(s) found so far: %d', len(ret_val))
        if not done:
            start_from = go_back_to
            next_date = go_back_to - time_interval
            log.debug('Calculating the next date to go back to based on the interval: %s - %s => %s', go_back_to, time_interval, next_date)
            go_back_to = next_date
    log.info('Found %d video(s) in total', len(ret_val))
    return ret_val
def get_video_url(video_id):
    ret_val = youtube_video_url.format(video_id)
    log.debug('Video URL: %s', ret_val)
    return ret_val
def main():
    try:
        channel_id = get_channel_id(args.channel)
        if channel_id == -1:
            raise Exception('Impossible to continue without the channel id')
        channel_videos = get_channel_videos(channel_id, date_to_start_from, date_to_go_back_to, time_interval)
        if not len(channel_videos) > 0:
            log.info("No video found for that channel! Either there's none or a problem occurred. Enable verbose or debug logging for more details..")
            sys.exit(0)
        log.info('Generating links for found videos')
        video_urls = []
        for video in channel_videos:
            log.debug('Processing video: %s', json.dumps(video, indent=4))
            video_id = video.get('id').get('videoId')
            log.debug('Video id: %s', video_id)
            video_url = get_video_url(video_id)
            video_urls.append(video_url)
        if args.output_file_path is not None and args.output_file_path is not '':
            log.debug('File output enabled')
            log.info('Links will be written to %s', args.output_file_path)
            f = None
            try:
                f = open(args.output_file_path, 'w')
            except Exception as err:
                log.critical('Could not create/open the output file!', exc_info=True)
                raise Exception('Impossible to write the links to the output file. Verify that the path is correct and that it is accessible/can be created/can be written to')
            for video_url in video_urls:
                f.write(video_url + "\n")
            f.close()
        else:
            for video_url in video_urls:
                print(video_url)
        log.info('Done!')
    except Exception as err:
        log.critical('We tried our best but still..', exc_info=True)
        sys.exit(2)
if __name__ == '__main__':
    main()