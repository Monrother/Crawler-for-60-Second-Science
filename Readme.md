## 60-Second Science Crawler
This project is for those who want to practise their English listening ability.

The project provides a crawler that can download the mp3 audio files from the [60-Second Science](https://www.scientificamerican.com/podcast/60-second-science/) official site automatically, and you can listen to these materials from you PC player, player on your phone, or upload them to your cloud storage such as Netease Cloud Music or Ximalaya, etc.

This crawler uses the Scrapy tool, so before using this repo, make sure there are Python and Scrapy already installed on your machine, and run the following command in the current directory
``` bash
scrapy runspider crawler_scientific_american.py
```
and the files will be downloaded to the current folder.

Note: The current version just download the ~20 materials on the home page of 60-Second Science.