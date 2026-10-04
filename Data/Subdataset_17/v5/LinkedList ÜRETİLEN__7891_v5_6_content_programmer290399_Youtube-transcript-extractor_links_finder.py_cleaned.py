import urllib.request
import json
import datetime
import sys
import argparse
import logging
from rfc3339 import rfc3339
def parse_arguments():
    parser = argparse.ArgumentParser(description='Find all videos in a given YouTube channel')
    parser.add_argument('-k', '--api-key', required=True, help='Google Data API key. Get one at https:
    parser.add_argument('-c', '--channel', required=True, help='YouTube channel to get videos from')
    parser.add_argument('-o', '--output-file-path', default='', help='File to write found video links to (replaces content each time). Defaults to standard output.')
    parser.add_argument('-x', '--date-from', help='Videos published after this date will not be retrieved (format: yyyy-mm-dd). Defaults to the current date.')
    parser.add_argument('-y', '--date-to', help='Videos published before this date will not be retrieved (format: yyyy-mm-dd). Defaults to one month before dateFrom.')
    parser.add_argument('-i', '--interval', type=int, help='Max period (in days) to retrieve videos at a time. Default: 30 days')
    output_detail_level = parser.add_mutually_exclusive_group()
    output_detail_level.add_argument('-q', '--quiet', action='store_true', help='Only print out results or fatal errors')
    output_detail_level.add_argument('-v', '--verbose', action='store_true', help='Print detailed information during execution')
    output_detail_level.add_argument('-d', '--debug', action='store_true', help='Print all details')
    parser.add_argument('-l', '--log-file-path', help='File to write logs to (replaces content each time). Defaults to standard output.')
    parser.add_argument('--version', action='version', version='1.0')
    return parser.parse_args()
def setup_logging(args):
    log = logging.getLogger('YoutubeChannelVideoFinder')
    handler = logging.FileHandler(args.logFilePath, "w") if args.logFilePath else logging.StreamHandler()
    log_format = '[%(asctime)s] [%(levelname)s] - %(message)s'
    handler.setFormatter(logging.Formatter(log_format))
    log.addHandler(handler)
    log.setLevel(logging.DEBUG if args.debug else logging.INFO if args.verbose else logging.ERROR if args.quiet else logging.WARN)
    return log
def initialize_variables(args, log):
    log.debug('Initializing variables')
    date_to_start_from = datetime.datetime.strptime(args.dateFrom, '%Y-%m-%d') if args.dateFrom else datetime.datetime.now()
    log.info('Date to start from: %s', date_to_start_from)
    date_to_go_back_to = datetime.datetime.strptime(args.dateTo, '%Y-%m-%d') if args.dateTo else date_to_start_from - datetime.timedelta(weeks=4)
    log.info('Date to go back to: %s', date_to_go_back_to)
    total_time_period = date_to_start_from - date_to_go_back_to
    log.info('Total period to find videos: %s', str(total_time_period))
    time_interval = datetime.timedelta(days=args.interval) if args.interval else datetime.timedelta(weeks=4)
    log.info('Time interval: %s', time_interval)
    return date_to_start_from, date_to_go_back_to, time_interval
def get_channel_id(channel_name, youtube_channels_api_url, log):
    log.info('Searching channel ID for channel: %s', channel_name)
    try:
        url = youtube_channels_api_url.format(channel_name)
        log.debug("Request: %s", url)
        response = urllib.request.urlopen(url)
        response_as_json = json.load(response)
        response.close()
        log.debug('Response: %s', json.dumps(response_as_json, indent=4))
        if response_as_json['pageInfo'].get('totalResults') > 0:
            channel_id = response_as_json['items'][0].get('id')
            log.info('Channel ID found: %s', channel_id)
            return channel_id
        else:
            log.debug('No channel found with the given name.')
            raise Exception('The channel ID could not be retrieved. Ensure the channel name is correct.')
    except Exception as err:
        log.error('Error retrieving channel ID.', exc_info=True)
        return -1
def get_channel_videos_published_in_interval(channel_id, published_before, published_after, request_channel_videos_info, log):
    log.info('Getting videos published before %s and after %s', published_before, published_after)
    videos = []
    next_page_token = ''
    while True:
        try:
            url = request_channel_videos_info.format(channel_id, published_before, published_after, next_page_token)
            log.debug('Request: %s', url)
            response = urllib.request.urlopen(url)
            response_as_json = json.load(response)
            response.close()
            videos.extend(response_as_json['items'])
            next_page_token = response_as_json.get('nextPageToken', '')
            if not next_page_token:
                break
        except Exception as err:
            log.error('Error retrieving channel videos.', exc_info=True)
            break
    log.info('Found %d video(s) in this time interval', len(videos))
    return videos
def get_channel_videos(channel_id, date_to_start_from, date_to_go_back_to, time_interval, request_channel_videos_info, log):
    log.info('Searching for videos published in channel between %s and %s', date_to_start_from, date_to_go_back_to)
    if date_to_start_from < date_to_go_back_to:
        raise Exception('The start date cannot be before the end date!')
    all_videos = []
    start_from = date_to_start_from
    while start_from > date_to_go_back_to:
        go_back_to = max(start_from - time_interval, date_to_go_back_to)
        published_before = rfc3339(start_from, utc=True)
        published_after = rfc3339(go_back_to, utc=True)
        videos = get_channel_videos_published_in_interval(channel_id, published_before, published_after, request_channel_videos_info, log)
        all_videos.extend(videos)
        start_from = go_back_to
    log.info('Found %d video(s) in total', len(all_videos))
    return all_videos
def get_video_url(video_id):
    return 'https:
def main():
    args = parse_arguments()
    log = setup_logging(args)
    youtube_api_url = 'https:
    youtube_channels_api_url = youtube_api_url + 'channels?key={0}&forUsername={{0}}&part=id'.format(args.apiKey)
    youtube_search_api_url = youtube_api_url + 'search?key={0}&channelId={{0}}&part=id&order=date&type=video&publishedBefore={{1}}&publishedAfter={{2}}&pageToken={{3}}&maxResults=50'.format(args.apiKey)
    date_to_start_from, date_to_go_back_to, time_interval = initialize_variables(args, log)
    try:
        channel_id = get_channel_id(args.channel, youtube_channels_api_url, log)
        if channel_id == -1:
            raise Exception('Cannot continue without the channel ID.')
        channel_videos = get_channel_videos(channel_id, date_to_start_from, date_to_go_back_to, time_interval, youtube_search_api_url, log)
        if not channel_videos:
            log.info("No video found for that channel!")
            sys.exit(0)
        video_urls = [get_video_url(video['id']['videoId']) for video in channel_videos]
        if args.outputFilePath:
            log.info('Writing links to %s', args.outputFilePath)
            with open(args.outputFilePath, 'w') as file:
                for video_url in video_urls:
                    file.write(video_url + "\n")
        else:
            for video_url in video_urls:
                print(video_url)
        log.info('Done!')
    except Exception as err:
        log.critical('An error occurred.', exc_info=True)
        sys.exit(2)
if __name__ == '__main__':
    main()