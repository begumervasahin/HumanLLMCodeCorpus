import sys
import argparse
import logging
import urllib.request
import json
import datetime
from rfc3339 import rfc3339
parser = argparse.ArgumentParser(description='Find all videos in a given YouTube channel')
parser.add_argument('-k', '--api-key', dest='api_key', action='store', required=True,
                    help='Google Data API key. Obtain from: https:
parser.add_argument('-c', '--channel', dest='channel', action='store', required=True,
                    help='YouTube channel to retrieve videos from')
parser.add_argument('-o', '--output-file-path', dest='output_file_path', action='store', default='',
                    help='File to write video links to. If not provided, links are sent to standard output')
parser.add_argument('-x', '--date-from', dest='date_from', action='store',
                    help='Earliest video publish date (format: yyyy-mm-dd). Defaults to current date')
parser.add_argument('-y', '--date-to', dest='date_to', action='store',
                    help='Latest video publish date (format: yyyy-mm-dd). Defaults to one month before the start date')
parser.add_argument('-i', '--interval', dest='interval', action='store',
                    help='Longest time interval (in days) to retrieve videos at once. Default: 30 days')
output_detail_level = parser.add_mutually_exclusive_group()
output_detail_level.add_argument('-q', '--quiet', dest='quiet', action='store_true', default=False,
                                 help='Print only results or fatal errors')
output_detail_level.add_argument('-v', '--verbose', dest='verbose', action='store_true', default=False,
                                 help='Print detailed information during execution (e.g., invoked URLs)')
output_detail_level.add_argument('-d', '--debug', dest='debug', action='store_true', default=False,
                                 help='Print all details')
parser.add_argument('-l', '--log-file-path', dest='log_file_path', action='store',
                    help='File to write logs to. If not provided, logs are sent to standard output')
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
date_to_start_from = datetime.datetime.strptime(args.date_from, '%Y-%m-%d') if args.date_from else datetime.datetime.now()
log.info('Date to start from: %s', date_to_start_from)
date_to_go_back_to = datetime.datetime.strptime(args.date_to, '%Y-%m-%d') if args.date_to else date_to_start_from - datetime.timedelta(weeks=4)
log.info('Date to go back to: %s', date_to_go_back_to)
time_interval = datetime.timedelta(days=int(args.interval)) if args.interval else datetime.timedelta(weeks=4)
log.info('Time interval: %s', time_interval)
youtube_api_url = 'https:
youtube_channels_api_url = youtube_api_url + 'channels?key={0}&'.format(args.api_key)
youtube_search_api_url = youtube_api_url + 'search?key={0}&'.format(args.api_key)
request_parameters_channel_id = youtube_channels_api_url + 'forUsername={0}&part=id'
request_channel_videos_info = youtube_search_api_url + 'channelId={0}&part=id&order=date&type=video&publishedBefore={1}&publishedAfter={2}&pageToken={3}&maxResults=50'
youtube_video_url = 'https:
def get_channel_id(channel_name):
    try:
        url = request_parameters_channel_id.format(channel_name)
        log.debug("Request: %s", url)
        response = urllib.request.urlopen(url)
        response_as_json = json.load(response)
        response.close()
        if response_as_json['pageInfo'].get('totalResults') > 0:
            return response_as_json['items'][0].get('id')
        else:
            raise Exception('Channel id could not be retrieved. Ensure the channel name is correct')
    except Exception as err:
        log.error('An exception occurred while retrieving the channel id', exc_info=True)
        return -1
def get_channel_videos_published_in_interval(channel_id, published_before, published_after):
    ret_val = []
    found_all = False
    next_page_token = ''
    while not found_all:
        try:
            url = request_channel_videos_info.format(channel_id, published_before, published_after, next_page_token)
            response = urllib.request.urlopen(url)
            response_as_json = json.load(response)
            response.close()
            returned_videos = response_as_json['items']
            ret_val.extend(returned_videos)
            next_page_token = response_as_json.get('nextPageToken')
            if not next_page_token:
                found_all = True
        except Exception as err:
            log.error('An exception occurred while retrieving channel videos. Stopping search.', exc_info=True)
            found_all = True
    return ret_val
def get_channel_videos(channel_id, date_to_start_from, date_to_go_back_to, time_interval):
    ret_val = []
    start_from = date_to_start_from
    go_back_to = start_from - time_interval
    while go_back_to >= date_to_go_back_to:
        if go_back_to < date_to_go_back_to:
            go_back_to = date_to_go_back_to
        go_back_to_rfc3339 = rfc3339(go_back_to, utc=True)
        start_from_rfc3339 = rfc3339(start_from, utc=True)
        videos_published_in_interval = get_channel_videos_published_in_interval(channel_id, start_from_rfc3339, go_back_to_rfc3339)
        ret_val.extend(videos_published_in_interval)
        if go_back_to == date_to_go_back_to:
            break
        start_from = go_back_to
        go_back_to -= time_interval
    return ret_val
def get_video_url(video_id):
    return youtube_video_url.format(video_id)
def main():
    try:
        channel_id = get_channel_id(args.channel)
        if channel_id == -1:
            raise Exception('Failed to retrieve channel id')
        channel_videos = get_channel_videos(channel_id, date_to_start_from, date_to_go_back_to, time_interval)
        if not channel_videos:
            log.info("No videos found for the channel.")
            sys.exit(0)
        video_urls = [get_video_url(video.get('id').get('videoId')) for video in channel_videos]
        if args.output_file_path:
            with open(args.output_file_path, 'w') as f:
                for video_url in video_urls:
                    f.write(video_url + "\n")
        else:
            for video_url in video_urls:
                print(video_url)
        log.info('Done!')
    except Exception as err:
        log.critical('An error occurred', exc_info=True)
        sys.exit(2)
if __name__ == '__main__':
    main()