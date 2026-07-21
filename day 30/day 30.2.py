facebook_posts = [
    { 'likes': 21, 'comments': 20},
    { 'likes': 31, 'comments': 2, 'shared': True},
    { 'likes': 41, 'comments': 4, 'shared': True},
    { 'likes': 42, 'comments': 8},
    { 'likes': 51, 'comments': 4},
    { 'likes': 65, 'comments': 7},
    { 'likes': 24, 'comments': 6},
]

total_likes = 0

for post in facebook_posts:
    try:
        total_likes += post['likes']
    except KeyError:
        total_likes += 0

print(total_likes)
