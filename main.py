from urllib.request import Request, urlopen
from bs4 import BeautifulSoup


def get_top_hashtags_and_links(country):
    site = f"https://twitter-trends.iamrohit.in/{country}"
    hdr = {'User-Agent': 'Mozilla/5.0'}
    req = Request(site, headers=hdr)
    page = urlopen(req)
    soup = BeautifulSoup(page, "html.parser")

    top_hashes_part = soup.find(id="copyData").find_all('a')

    top_hastags = []
    for item in top_hashes_part:
        top_hastags.append(
            {"hashtag": item.get_text(),
             "link": item.get('href')}
        )

    return top_hastags


if __name__ == '__main__':
    data = get_top_hashtags_and_links(country="indonesia")
    print(data)
