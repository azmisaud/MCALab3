def count_total_characters(*args):
    total=sum(len(arg) for arg in args)
    return total

print(count_total_characters("HELLO","WORLD","RIZWAN"))