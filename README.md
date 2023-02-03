# Kickstarter Scrapy Crawler

This project currently only consists of one spider. 

This project can be hosted on Scrapy Cloud.  
It uses Zyte Smart Proxy Manager.  
The dataset can be found [here](https://www.kaggle.com/datasets/patkle/most-funded-kickstarter-projects).  
A Jupyter Notebook with some EDA on that data can be found [here](https://www.kaggle.com/patkle/kickstarter-s-most-funded-projects/edit).  

## Spider: most_funded

The spider can be ran with
```zsh
python3 -m scrapy crawl most_funded -a pages=5 -O most_funded.csv
```

### Arguments

With `-a` you can specify arguments for the spider.  

|argument   |type  |description   | 
|---|---|---|
|pages   |int   |number of pages to scrape   |

## Setting up locally

When setting up this project locally you must create a **.env** file with `ZYTE_SMARTPROXY_APIKEY` equal to your smart proxy manager api key.  

## Deploy to Scrapy Cloud

There's a shortcut in the Makefile, just running `make deploy` will deploy the project to Scrapy Cloud (given that you provided the project ID in `scrapinghub.yml`).  
Don't forget to add the ZYTE_SMARTPROXY_APIKEY setting in your cloud project's settings!  

## Disclaimer
You could [buy me a coffe](https://www.buymeacoffee.com/kleinp) if you wanted to. I'd really appreciate that.  
