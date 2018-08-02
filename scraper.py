from bs4 import BeautifulSoup
import requests
import re
import os
import urllib.request
import argparse
import sys
import json
from io import BytesIO
from PIL import Image

def get_soup(query):
    querysplit=query.split()
    querysplit='+'.join(querysplit)
    url="https://www.google.co.in/search?q="+querysplit+"&source=lnms&tbm=isch"
    header={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"}
    souped=BeautifulSoup(urllib.request.urlopen(urllib.request.Request(url, headers=header)),'html.parser')
    imginfo=[]
    for a in souped.find_all("div", { "class": "rg_meta" }):
        link, Type = json.loads(a.text)["ou"], json.loads(a.text)["ity"]
        imginfo.append((link,Type))
    return imginfo

def main(args):
    parser = argparse.ArgumentParser(description='Scrape Google images')
    parser.add_argument('-s', '--search', default='bananas', type=str, help='search term')
    parser.add_argument('-n', '--num_images', default=10, type=int, help='num images to save')
    parser.add_argument('-d', '--directory', default='/Users/thevest/Downloads/crawlinz/', type=str, help='save directory')
    args = parser.parse_args()

    query = args.search
    max_images = args.num_images
    save_directory = args.directory
    print("running-----------------")
    print("query="+query)
    print("max_imgs="+str(max_images))
    print("save_dir="+save_directory)

    soup = get_soup(query)
    imgtitle=''.join(query.split(" ")).lower()

    for i, (img, Type) in enumerate(soup[0:max_images]):
        try:
            resp = requests.get(img)
            imgfile = Image.open(BytesIO(resp.content))
            fpath = '{}-{}-{}-{}'.format(save_directory, imgtitle, i, '.jpeg')
            imgfile.save(fpath, "jpeg")
            print("saved " + img)
        except Exception as e:
            print("could not load: "+img)
            print(e)

if __name__ == '__main__':
    from sys import argv
    try:
        main(argv)
    except KeyboardInterrupt:
        pass
    sys.exit()
