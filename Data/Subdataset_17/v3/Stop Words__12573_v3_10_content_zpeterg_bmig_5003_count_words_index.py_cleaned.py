import sys
import json
from getFile import getFile
from filter import Filter
from format import formatToLines
from utils import dealArgs
from writeFile import writeFile, writeCSV
from getStats import getStats
def get_and_filter(options):
    word_filter = Filter(options)
    return getFile(options['file'], word_filter.filter)
def process_words(words, options):
    if options.get('stats'):
        return getStats(words), True
    elif options.get('format'):
        return formatToLines(words), False
    return words, False
def write_output(data, options, is_stats):
    if options.get('output'):
        if options.get('csv'):
            columns = ['Name'] if not is_stats else ['Name', 'Count']
            writeCSV(data, options['output'], columns)
        else:
            output_data = json.dumps(data, indent=4)
            writeFile(output_data, options['output'])
        print(f"\nThe requested data has been written to file {options['output']}.")
    else:
        print_output(data, is_stats)
def print_output(data, is_stats):
    if is_stats:
        if not data:
            print("\nNo stats to print.")
        else:
            print("\nSTATS:")
            for stat, value in data.items():
                print(f"{stat}: {value}")
    else:
        if not data:
            print("\nNo words to print.")
        else:
            print("\nWORDS:")
            for word in data:
                print(word)
def run(args):
    options = dealArgs(args).to_object()
    words = get_and_filter(options)
    processed_data, is_stats = process_words(words, options)
    write_output(processed_data, options, is_stats)
if __name__ == '__main__':
    run(sys.argv)