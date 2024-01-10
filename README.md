# TransferMarket Scraper & Twitter Bot 
Juan Camilo Montoya

## Description

This Python script leverages Selenium for web scraping on TransferMarket to fetch the latest confirmed transfers in the football transfer market. The gathered data is then transformed into a tweet using the Twitter API through Tweepy.

## Features

- Web scraping of TransferMarket for the latest confirmed football transfers.
- Utilizes Selenium for dynamic content extraction.
- Converts scraped data into a tweet using the Twitter API and Tweepy.
- Customizable tweet format and content.
- Easy-to-use and configure.

## Prerequisites

Before running the script, make sure you have the following installed:

- Python 3.x
- Selenium
- Tweepy

Install the required dependencies using the following command:

```bash
pip install selenium tweepy
```

Additionally, you need to have the appropriate web driver for Selenium. Download the appropriate driver for your browser and update the `PATH` variable in the script accordingly.

## Configuration

1. Set up a Twitter Developer account and create an app to obtain API keys and access tokens.
2. Replace the placeholders in the `config.py` file with your TransferMarket URL and Twitter API credentials.

## Disclaimer

This script is intended for educational purposes only. Respect the terms of service of TransferMarket and Twitter while using this script. The developer is not responsible for any misuse or violation of third-party terms.
