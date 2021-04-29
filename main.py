from app import get_top_hashtags_and_links

if __name__ == '__main__':
    data = get_top_hashtags_and_links(country="indonesia")
    print(data)
