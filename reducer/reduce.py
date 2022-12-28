import sys

prev_key = None
key_count = 0

for line in sys.stdin:
    key, one = line.strip().split(',')
    one = int(one)

    if prev_key:
        if prev_key == key:
            key_count += 1
        else:
            print(prev_key, key_count)
            prev_key = key
            key_count = one
    else:
        prev_key = key
        key_count = one

print(prev_key, key_count)
