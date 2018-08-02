# scrapery scrape - imagescrape

script to download a batch of images based on a google query

# to install

```sh
# you need python and virtualenv (preferably)
brew install python
sudo easy_install pip
pip install --upgrade virtualenv
# get the repo
git clone git@github.com:thevest/imagescrape.git
cd imagescrape
# create a python3 virtualenv and install requirements
virtualenv --system-site-packages -p python3 env
source env/bin/activate # once in this mode enter `deactivate` to leave
pip3 install -r requirements.txt

```

# actual usage

```sh

-s | --search     => The search term
-d | --directory  => The output dir
-n | --max_images => Number of image

python3 scraper.py -s "Search Term (i.e. google search term)" -d "/some-dir-relative/to-this-one" -n 8 # (how many)

```
