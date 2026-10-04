import urllib.request
import json
import datetime
import sys
import argparse
import logging
from rfc3339 import rfc3339
parser = argparse.ArgumentParser(description='This program finds all videos in a given YouTube channel.')
parser.add_argument('-k', '--api-key', dest='apiKey', required=True,
                    help='Google Data API key to use. Get one here: https:
parser.add_argument('-c', '--channel', dest='channel', required=True,
                    help='YouTube channel to get videos from')
parser.add_argument('-o', '--output-file-path', dest='outputFilePath', default='',
                    help='File to write found video links to (content replaced each time). If not specified, links are sent to standard output')
parser.add_argument('-x', '--date-from', dest='dateFrom',
                    help='Videos published after this date will not be retrieved (format: yyyy-mm-dd). If not specified, the current date is taken')
parser.add_argument('-y', '--date-to', dest='dateTo',
                    help='Videos published before this date will not be retrieved (format: yyyy-mm-dd). If not specified, we go back one month from --date-from')
parser.add_argument('-i', '--interval', dest='interval', type=int, default=30,
                    help='Longest period of time (in days) to retrieve videos at a time. Default: 30 days')
outputDetailLevel = parser.add_mutually_exclusive_group()
outputDetailLevel.add_argument('-q', '--quiet', dest='quiet', action='store_true', default=False,
                               help='Only print out results or fatal errors')
outputDetailLevel.add_argument('-v', '--verbose', dest='verbose', action='store_true', default=False,
                               help='Print out detailed information during execution')
outputDetailLevel.add_argument('-d', '--debug', dest='debug', action='store_true', default=False,
                               help='Print out all the details')
parser.add_argument('-l', '--log-file-path', dest='logFilePath',
                    help='File to write the logs to (content replaced each time). If not specified, logs are sent to standard output')
parser.add_argument('--version', action='version', version='1.0')
args = parser.parse_args()
log = logging.getLogger('youtube_channel_videos')
handler = logging.FileHandler(args.logFilePath, "w") if args.logFilePath else logging.StreamHandler()
logFormat = '[%(asctime)s] [%(levelname)s] - %(message)s'
handler.setFormatter(logging.Formatter(logFormat))
log.addHandler(handler)
if args.verbose:
    log.setLevel(logging.INFO)
elif args.debug:
    log.setLevel(logging.DEBUG)
elif args.quiet:
    log.setLevel(logging.ERROR)
else:
    log.setLevel(logging.WARNING)
log.debug('Initializing variables')
dateToStartFrom = datetime.datetime.strptime(args.dateFrom, '%Y-%m-%d') if args.dateFrom else datetime.datetime.now()
log.info('Date to start from: %s', dateToStartFrom)
dateToGoBackTo = datetime.datetime.strptime(args.dateTo, '%Y-%m-%d') if args.dateTo else dateToStartFrom - datetime.timedelta(days=30)
log.info('Date to go back to: %s', dateToGoBackTo)
totalTimePeriod = dateToStartFrom - dateToGoBackTo
log.info('Total period of time to find videos for: %s', totalTimePeriod)
timeInterval = datetime.timedelta(days=args.interval)
log.info('Time interval: %s', timeInterval)
youtubeApiUrl = 'https:
youtubeChannelsApiUrl = f'{youtubeApiUrl}channels?key={args.apiKey}&'
youtubeSearchApiUrl = f'{youtubeApiUrl}search?key={args.apiKey}&'
requestParametersChannelId = f'{youtubeChannelsApiUrl}forUsername={{0}}&part=id'
requestChannelVideosInfo = f'{youtubeSearchApiUrl}channelId={{0}}&part=id&order=date&type=video&publishedBefore={{1}}&publishedAfter={{2}}&pageToken={{3}}&maxResults=50'
youtubeVideoUrl = 'https:
def get_channel_id(channel_name):
    log.info('Searching channel id for channel: %s', channel_name)
    try:
        url = requestParametersChannelId.format(channel_name)
        log.debug("Request: %s", url)
        response = urllib.request.urlopen(url)
        response_as_json = json.load(response)
        response.close()
        log.debug('Response: %s', json.dumps(response_as_json, indent=4))
        if response_as_json['pageInfo'].get('totalResults') > 0:
            channel_id = response_as_json['items'][0].get('id')
            log.info('Channel id found: %s', channel_id)
            return channel_id
        else:
            raise ValueError('No channel found with the given name.')
    except Exception as err:
        log.error('Failed to retrieve channel id', exc_info=True)
        return None
def get_videos_in_interval(channel_id, published_before, published_after):
    log.info('Getting videos published before %s and after %s', published_before, published_after)
    videos = []
    next_page_token = ''
    while True:
        try:
            url = requestChannelVideosInfo.format(channel_id, published_before, published_after, next_page_token)
            log.debug('Request: %s', url)
            response = urllib.request.urlopen(url)
            response_as_json = json.load(response)
            response.close()
            videos.extend(response_as_json['items'])
            next_page_token = response_as_json.get('nextPageToken', '')
            if not next_page_token:
                break
        except Exception as err:
            log.error('Failed to retrieve videos', exc_info=True)
            break
    log.info('Found %d video(s) in this interval', len(videos))
    return videos
def get_channel_videos(channel_id, date_from, date_to, interval):
    log.info('Searching for videos published in channel between %s and %s', date_from, date_to)
    videos = []
    start = date_from
    end = start - interval
    while start > date_to:
        if end < date_to:
            end = date_to
        start_rfc3339 = rfc3339(start, utc=True)
        end_rfc3339 = rfc3339(end, utc=True)
        videos_in_interval = get_videos_in_interval(channel_id, start_rfc3339, end_rfc3339)
        videos.extend(videos_in_interval)
        start = end
        end -= interval
    log.info('Found %d video(s) in total', len(videos))
    return videos
def get_video_url(video_id):
    return youtubeVideoUrl.format(video_id)
def main():
    try:
        channel_id = get_channel_id(args.channel)
        if not channel_id:
            raise ValueError('Could not retrieve the channel id')
        videos = get_channel_videos(channel_id, dateToStartFrom, dateToGoBackTo, timeInterval)
        if not videos:
            log.info("No videos found for that channel! Enable verbose or debug logging for more details.")
            sys.exit(0)
        video_urls = [get_video_url(video['id']['videoId']) for video in videos]
        if args.outputFilePath:
            log.info('Writing links to %s', args.outputFilePath)
            try:
                with open(args.outputFilePath, 'w') as f:
                    for video_url in video_urls:
                        f.write(video_url + "\n")
            except Exception as err:
                log.critical('Could not write to output file', exc_info=True)
                raise
        else:
            for video_url in video_urls:
                print(video_url)
        log.info('Done!')
    except Exception as err:
        log.critical('An error occurred', exc_info=True)
        sys.exit(2)
if __name__ == '__main__':
    main()