def get_artwork(title, artist):
    import random
    import requests
    #import io
    #import PIL.Image as Image
    from bs4 import BeautifulSoup

    title = title.replace('_', '')
    URL = f"https://www.discogs.com/ru/search/?type=all&title={title}&artist={artist}"
    Folder='/home/tururu/Downloads/ICONS/Folders'
    headers = {
        'User-Agent': random.choice([
            "Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0",
            "Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/78.0",
            "Mozilla/5.0 (X11; Linux x86_64; rv:95.0) Gecko/20100101 Firefox/95.0"
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4495.0 Safari/537.36"
            ])
    }

    s = requests.Session().get(URL, headers=headers)
    html = s.text
    soup = BeautifulSoup(html, 'lxml')
    tables = soup.findAll('span', class_="thumbnail_center")

    links=[]
    for table in tables:
        url_on_img = table.find('img').get('data-src')
        if url_on_img is not None:
            links.append(url_on_img)

    if links:
        response = requests.get(links[0], headers=headers)
        #image = Image.open(io.BytesIO(response.content))
        image = response.content
        return image




if __name__=='__main__':
    print(get_artwork('Океанами стали', 'ALEKSEEV'))
#
    
