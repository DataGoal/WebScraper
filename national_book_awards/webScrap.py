Wimport scrapy
import csv
from scrapy.crawler import CrawlerProcess

class NationalBookAwardsSpider(scrapy.Spider):
    name = "national_book_awards"

    def start_requests(self):
        base_url = "https://www.nationalbook.org/awards-prizes/national-book-awards-{}"
        years = range(1950, 2024)

        for year in years:
            yield scrapy.Request(base_url.format(year), self.parse, meta={'year': year})

    def parse(self, response):
        year = response.meta['year']
        links = response.css('div.row.winners-list-row a::attr(href)').getall()

        data = {
            'year': year,
            'fiction': extract_last_two_segments(links[0] if links and len(links) >= 1 else 'null'),
            'non-fiction': extract_last_two_segments(links[1] if links and len(links) >= 2 else 'null'),
            'poetry': extract_last_two_segments(links[2] if links and len(links) >= 3 else 'null'),
            'TL': extract_last_two_segments(links[3] if links and len(links) >= 4 else 'null'),
            'YL': extract_last_two_segments(links[4] if links and len(links) >= 5 else 'null')
        }

        with open('C:\\Users\\bbala\\Downloads\\national_book_awards.csv', 'a', newline='') as csvfile:
            fieldnames = ['year', 'fiction', 'non-fiction', 'poetry', 'TL', 'YL']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            if csvfile.tell() == 0:
                writer.writeheader()

            writer.writerow(data)

def extract_last_two_segments(url):
    segments = url.split('/')
    if len(segments) >= 2:
        return segments[-2] + '/' + segments[-1]
    else:
        return 'null'

def run_spider():
    process = CrawlerProcess(settings={
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
    })

    process.crawl(NationalBookAwardsSpider)

    process.start()

if __name__ == "__main__":
    run_spider()
