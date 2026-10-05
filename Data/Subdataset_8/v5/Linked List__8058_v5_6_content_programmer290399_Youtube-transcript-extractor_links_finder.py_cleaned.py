import urllib.request
import json
import time
import datetime
import sys
import argparse
import logging
from rfc3339 import rfc3339
parser = argparse.ArgumentParser(description='Find all videos in a given Youtube channel')
parser.add_argument('-k', '--api-key', dest='apiKey', action='store', required=True, help='Google Data API key to use. Get one here: https:
parser.add_argument('-c', '--channel', dest='channel', action='store', required=True, help='Youtube channel to get videos from')
parser.add_argument('-o', '--output-file-path', dest='outputFilePath', action='store', default='', help='File to write found video links to (content replaced each time). If not specified, links are sent to standard output')
parser.add_argument('-x', '--date-from', dest='dateFrom', action='store', help='Videos published after this date will not be retrieved (expected format: yyyy-mm-dd). If not specified, the current date is taken')
parser.add_argument('-y', '--date-to', dest='dateTo', action='store', help='Videos published before this date will not be retrieved (expected format: yyyy-mm-dd). If not specified, we go back one month (related to -b / --date-from)')
parser.add_argument('-i', '--interval', dest='interval', action='store', help='Longest period of time (in days) to retrieve videos at a time for. Default: 30 days')
outputDetailLevel = parser.add_mutually_exclusive_group()
outputDetailLevel.add_argument('-q', '--quiet', dest='quiet', action='store_true', default=False, help='Only print out results or fatal errors')
outputDetailLevel.add_argument('-v', '--verbose', dest='verbose', action='store_true', default=False, help='Print out detailed information during execution (e.g., invoked URLs)')
outputDetailLevel.add_argument('-d', '--debug', dest='debug', action='store_true', default=False, help='Print out all details')
parser.add_argument('-l', '--log-file-path', dest='logFilePath', action='store', help='File to write the logs to (content replaced each time). If not specified, logs are sent to standard output (according to verbosity level)')
parser.add_argument('--version', action='version', version='1.0')
args = parser.parse_args()
logging.basicConfig(level=logging.INFO if args.verbose else logging.DEBUG if args.debug else logging.ERROR if args.quiet else logging.WARN,
                    format='[%(asctime)s] [%(levelname)s] - %(message)s',
                    filename=args.logFilePath,
                    filemode='w' if args.logFilePath else 'a')
log = logging.getLogger('_name_')
log.debug('Starting execution')
dateToStartFrom = datetime.datetime.strptime(args.dateFrom, '%Y-%m-%d') if args.dateFrom else datetime.datetime.now()
log.info('Date to start from: %s', dateToStartFrom)
dateToGoBackTo = datetime.datetime.strptime(args.dateTo, '%Y-%m-%d') if args.dateTo else dateToStartFrom - datetime.timedelta(weeks=4)
log.info('Date to go back to: %s', dateToGoBackTo)
totalTimePeriod = dateToStartFrom - dateToGoBackTo
log.info('Total period of time to find videos for: %s', str(totalTimePeriod))
timeInterval = datetime.timedelta(days=int(args.interval)) if args.interval else datetime.timedelta(weeks=4)
log.info('Time interval: %s', timeInterval)
youtubeApiUrl = 'https:
youtubeChannelsApiUrl = youtubeApiUrl + 'channels?key={0}&'.format(args.apiKey)
youtubeSearchApiUrl = youtubeApiUrl + 'search?key={0}&'.format(args.apiKey)
requestParametersChannelId = youtubeChannelsApiUrl + 'forUsername={0}&part=id'
requestChannelVideosInfo = youtubeSearchApiUrl + 'channelId={0}&part=id&order=date&type=video&publishedBefore={1}&publishedAfter={2}&pageToken={3}&maxResults=50'
youtubeVideoUrl = 'https:
def getChannelId(channelName):
    log.info('Searching channel id for channel: %s', channelName)
    try:
        url = requestParametersChannelId.format(channelName)
        log.debug("Request: %s", url)
        log.debug('Sending request')
        with urllib.request.urlopen(url) as response:
            responseAsJson = json.load(response)
        log.debug('Response: %s', json.dumps(responseAsJson, indent=4))
        channelId = responseAsJson['items'][0]['id']
        log.info('Channel id found: %s', channelId)
        return channelId
    except Exception as err:
        log.error('An exception occurred while trying to retrieve the channel id', exc_info=True)
        return -1
def getChannelVideosPublishedInInterval(channelId, publishedBefore, publishedAfter):
    log.info('Getting videos published before %s and after %s', publishedBefore, publishedAfter)
    retVal = []
    nextPageToken = ''
    while True:
        try:
            url = requestChannelVideosInfo.format(channelId, publishedBefore, publishedAfter, nextPageToken)
            log.debug('Request: %s', url)
            log.debug('Sending request')
            with urllib.request.urlopen(url) as response:
                responseAsJson = json.load(response)
            returnedVideos = responseAsJson['items']
            log.debug('Response: %s', json.dumps(returnedVideos, indent=4))
            retVal.extend(returnedVideos)
            nextPageToken = responseAsJson.get('nextPageToken')
            if not nextPageToken:
                break
        except Exception as  err:
            log.error('An exception occurred while trying to retrieve a subset of the channel videos. Stopping search.', exc_info=True)
            break
    log.info('Found %d video(s) in this time interval', len(retVal))
    return retVal
def getChannelVideos(channelId, dateToStartFrom, dateToGoBackTo, timeInterval):
    log.info('Searching for videos published in channel between %s and %s', dateToStartFrom, dateToGoBackTo)
    retVal = []
    startFrom = dateToStartFrom
    while startFrom > dateToGoBackTo:
        goBackTo = min(startFrom, dateToGoBackTo + timeInterval)
        log.debug('Converting timestamps to RFC3339 format')
        goBackTo_rfc3339 = rfc3339(goBackTo, utc=True)
        startFrom_rfc3339 = rfc3339(startFrom, utc=True)
        videosPublishedInInterval = getChannelVideosPublishedInInterval(channelId, startFrom_rfc3339, goBackTo_rfc3339)
        log.debug('Adding videos found in the interval to the results list')
        retVal.extend(videosPublishedInInterval)
        log.debug('Total video(s) found so far: %d', len(retVal))
        startFrom = goBackTo - datetime.timedelta(seconds=1)
    log.info('Found %d video(s) in total', len(retVal))
    return retVal
def getVideoURL(video):
    videoId = video['id']['videoId']
    return youtubeVideoUrl.format(videoId)
def main():
    try:
        channelId = getChannelId(args.channel)
        if channelId == -1:
            raise Exception('Impossible to continue without the channel id')
        channelVideos = getChannelVideos(channelId, dateToStartFrom, dateToGoBackTo, timeInterval)
        if not channelVideos:
            log.info("No video found for that channel! Either there's none or a problem occurred. Enable verbose or debug logging for more details..")
            sys.exit(0)
        log.info('Generating links for found videos')
        videoURLs = [getVideoURL(video) for video in channelVideos]
        if args.outputFilePath:
            log.info('Links will be written to %s', args.outputFilePath)
            with open(args.outputFilePath, 'w') as f:
                for videoURL in videoURLs:
                    f.write(videoURL + "\n")
        else:
            for videoURL in videoURLs:
                print(videoURL)
        log.info('Done!')
    except Exception as  err:
        log.critical('An error occurred:', exc_info=True)
        sys.exit(2)
if __name__ == '__main__':
    main()