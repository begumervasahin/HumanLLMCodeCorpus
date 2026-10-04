import sys
import json
from getFile import getFile
from filter import Filter
from format import formatToLines
from utils import dealArgs
from writeFile import writeFile, writeCSV
from getStats import getStats
def get_and_filter(options):
    filter_instance = Filter(options)
    words = getFile(options['file'], filter_instance.filter)
    return words
def process_options(options, words):
    if options.get('stats'):
        return getStats(words)
    if options.get('format'):
        return formatToLines(words)
    return words
def write_output(options, data):
    if options.get('output'):
        if options.get('csv'):
            columns = ['Name']
            if isinstance(data, dict):
                columns.append('Count')
            writeCSV(data, options['output'], columns)
        else:
            output_data = json.dumps(data, indent=4)
            writeFile(output_data, options['output'])
        print(f"\nThe requested data has been written to file {options['output']}.")
    else:
        print_output(data)
def print_output(data):
    if isinstance(data, dict):
        if len(data) <= 1:
            print('No stats to print.')
        else:
            print('STATS:')
            for stat, value in data.items():
                print(f'{stat}: {value}')
    else:
        if len(data) <= 1:
            print('No words to print.')
        else:
            print('WORDS:')
            for word in data:
                print(word)
def run(args):
    options = dealArgs(args).to_object()
    words = get_and_filter(options)
    data = process_options(options, words)
    write_output(options, data)
if __name__ == '__main__':
    run(sys.argv)