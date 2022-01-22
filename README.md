# SCRAPY PROJECT

## Installation

To use this app in all its glory you will need to make you you have the following installed:

Python 3 (app was built in 3.10.4) [Python](https://www.python.org/downloads/)

Scrapy (app was built in 2.5.1) [Scrapy](https://docs.scrapy.org/en/latest/intro/install.html)

MongoDB [Mongodb](https://www.mongodb.com/try/download/community?tck=docs_server&_ga=2.113342663.1751319021.1642779925-109559560.1642779925&_gac=1.229402094.1642779925.CjwKCAiA0KmPBhBqEiwAJqKK4-Cc638zRVxu0zUXUWYd-9k8E8mo-GEDSGqTeG9VsMtOzUapkdFAlhoCTTkQAvD_BwE)

To make your life easier you will probably want a package handler for python (I used Anaconda even though I hate snakes) and a GUI for Mongodb. I've been using 3T but Atlas might be a nicer experience.

Links to download and/or configure any missing software:

[Anaconda](https://docs.anaconda.com/anaconda/install/windows/)

[3T](https://studio3t.com/mongodb-compass-alternative/?utm_source=adwords&utm_medium=ppc&utm_term=mongodb%20compass&utm_campaign=GS+%7C+Competitors+%7C+US&hsa_net=adwords&hsa_ad=409331380077&hsa_src=g&hsa_ver=3&hsa_grp=49269852685&hsa_acc=1756351187&hsa_tgt=kwd-317301548309&hsa_mt=b&hsa_kw=mongodb%20compass&hsa_cam=1034583247&gclid=CjwKCAiA0KmPBhBqEiwAJqKK46aBZ6yCf3IGVki4Vd5niYqAj9eRBLz41so-Bg1F0LOEf1qv22TvmBoCVx0QAvD_BwE)

[Atlas](https://www.mongodb.com/cloud/atlas/register?utm_content=rlsapostreg&utm_source=google&utm_campaign=gs_americas_uscan_search_brand_dsa_atlas_desktop_rlsa_postreg&utm_term=&utm_medium=cpc_paid_search&utm_ad=&utm_ad_campaign_id=14383025495&adgroup=129270225274&gclid=CjwKCAiA0KmPBhBqEiwAJqKK4-4-JWAMYr-aexopgweWbfXQTcHscXlplnwnX6pGU9Br63F1rAca2BoCiiMQAvD_BwE)

## Running the Scraper

To run the scraper simply open a Python terminal and type:

scrapy crawl

To do this, you may need to select a Python Interpreter. In VSCode this is done with Ctrl + Shift + P and start typing Python: Select Interpreter

After the scraper crawls the sites it will insert the information into the amazon database.

## What Success Looks Like

Below we see a couple images from the created db called 'amazon' and the 2 collections inside it that were generated from the call:

### Product Info Collection

![Product_Info Data](https://raw.githubusercontent.com/reburke286/scrapy/main/installation/prod_info_coll.jpg)

### First Page of Review Collection

![First Page of Review Collection](https://raw.githubusercontent.com/reburke286/scrapy/main/installation/reviews_coll_pg1.JPG)

### Last Page of Review Collection

![Last Page of Review Collection](https://raw.githubusercontent.com/reburke286/scrapy/main/installation/review_col_pg8.JPG)

## Future Goals

Next steps for this project are building out the front end and using CRUD operations on the data.

Right now there is Express and Mongoose attached but no front-end rendering.
