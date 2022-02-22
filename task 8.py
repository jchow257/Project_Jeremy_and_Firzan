import unittest
class GoogleSpider(unittest.TestCase):
    name = 'google'
    allowed_domains = ['https://www.google.com/']
    start_urls = ['https://www.google.com//']

    def test_parse(self,):
        css_selector = 'img'
        for x in response.css(css_selector):
            newsel = '@src'
            yield {
                'Image Link':x.xpath(newsel).extract_first()
            }
if __name__ == '__main__':
    unittest.main()