from bs4 import BeautifulSoup
import re
import urlparse

class HtmlParser(object):
    
    
    def _get_new_urls(self, page_url, soup):
        new_urls = set();

        links = soup.find_all('a', href=re.compile(r"/item/(.*)"))
        for link in links:
            new_url = link['href']
            new_full_url = urlparse.urljoin(page_url, new_url)
            new_urls.add(new_full_url)
        return new_urls
    
    def _get_new_data(self, page_url, soup):
        res_data = {}

        res_data["url"] = page_url
        """
        <dd class="lemmaWgt-lemmaTitle-title">
            <h1>Python</h1>
        """
        dd_data = soup.find_all("dd")
        for dditem in dd_data:
            if dditem.find("h1") is not None:
                res_data['title'] = dditem.find("h1").get_text()
                break
        
        # <div class="lemma-summary" label-module="lemmaSummary">   
        summary_node = soup.find("div", attrs={"class": "lemma-summary"}) 
        res_data['summary'] = summary_node.get_text()
        return res_data
    
    def parse(self, page_url, html_cont):
        
        if page_url is None:
            return 
        
        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding = 'utf-8')

        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data
        
    
    



