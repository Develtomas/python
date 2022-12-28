import sys
for line in sys.stdin:
    # get words
    keywords = line.strip().split(',')[0]
    keyword = keywords.split()

    # write
    for key in keyword:
        if not key.isdigit():
            print(f'{key},1')
