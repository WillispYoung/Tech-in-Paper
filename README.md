### User Quality Improvement Targeted for CDNs
***

##### 1. Get media file URLs from many CP websites (selenium).

**v.qq.com**: locate *txpdiv* element with attribute *data-role* set as **txp-ui-console-cdn**, its innerHTML (if not empty) will be CDN server's domain for this web page. These domains are in the form of https://apd-4ca339c635848992779008d33f0ee5a5.v.smtcdns.com. See data_crawler/crawler.py. Name server: _smtcdns.com_.

**youku.com**: no element can indicate CDN server's address information, but inferring from network information its CDN server is fixed as https://valipl.cp31.ott.cibntv.net. Name server: _cibntv.net_.

**iqiyi.com**: CDN servers' domain are like https://v-3acdc404.71edge.com, which in this case is a _CERNET_ machine. Name server: _71edge.com_.

As conclusion, all these CP websites host their media files on certain CDN servers, which differ only in the first entry of domain. 

***
##### 2. Check if ECS is supported for each domain (EDNS).

***
##### 3. Get suggested replicas from ENDS.

***
##### 4. Trace route these replicas to identify hops along the path.

***
##### 5. Assimilate each hop to get its suggested replicas.

***
##### 6. Measure link qualities to these replicas.

***
##### 7. Measure using virtual machines located in different regions.
