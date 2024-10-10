import os


def sort_helper(dict):
    return (dict['count'])


def count_words(string):
    return len(string.split())


def count_chars(string):
    string = string.lower()
    chars = list(string)

    count = {}

    for char in chars:
        if char not in count:
            count[char] = 1
        else:
            count[char] += 1

    count_plus = []
    for key, value in count.items():
        if key.isalpha():
            temp = {"char": key, "count": value}
            count_plus.append(temp)

    count_plus.sort(reverse=True, key=sort_helper)

    return count_plus


def main():
    books_path = './books'
    for bookname in os.listdir(books_path):
        book_path = os.path.join(books_path, bookname)
        with open(book_path) as f:
            print('--- Begin report of ', book_path, ' ---')
            book = f.read()

            print(count_words(book), ' words found in the document\n')

            char_count = count_chars(book)

            for char in char_count:
                print(f"The '{char['char']}' character was "
                      f"found {char['count']} times")

            print('--- End report ---')


if __name__ == '__main__':
    main()
