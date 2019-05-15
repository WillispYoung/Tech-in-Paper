### Service Quality Improvement Targeted for CDNs

#### 1. Measuring Procedure
(1). Get media file URLs from many CP websites (selenium).

_**v.qq.com**_: locate *txpdiv* element with attribute 
*data-role* set as **txp-ui-console-cdn**, its innerHTML
 (if not empty) will be CDN server's domain for this web 
 page. These domains are in the form of 
 https://apd-4ca339c635848992779008d33f0ee5a5.v.smtcdns.com. 
 See data_crawler/crawler.py. Name server: _smtcdns.com_.

_**youku.com**_: no element can indicate CDN server's address 
information, but inferring from network information its CDN 
server is fixed as https://valipl.cp31.ott.cibntv.net. 
Name server: _cibntv.net_.

_**iqiyi.com**_: CDN servers' domain are like 
https://v-3acdc404.71edge.com, which in this case is 
a _CERNET_ machine. Name server: _71edge.com_.

As conclusion, all these CP websites host their media 
files on certain CDN servers, which differ only in the 
first entry of domain. 

(2). Check if ECS is supported for each domain (EDNS).

Judging from simple tests, CDNs listed above all support 
ECS option. Supposedly, local DNS cache might lead to 
elimination of support in following DNS responses.

(3). Get suggested replicas from ENDS.

With URLs of CDN servers acquired, replicas are actually 
IP list contained in DNS response while resolving these 
domain names. 

(4). Trace route these replicas to identify hops along the path.

Currently, this procedure is conducted by manually type 
_tracert_ command in terminal. All results are stored in 
**data** folder, with filename in the form of _traces*.txt_.

(5). Assimilate each hop to get its suggested replicas.

Altering _subnet_ field in EDNS packet, then recommended 
replicas for each hop are contained in each relative EDNS 
response. Results are stored in **data** folder, with 
filename in the form of _subnet-assimilation*.txt_.

_Home experiments need re-conduct. -- finished._

(6). Measure link qualities to these replicas.

Currently ping delay is used as the sole metric to measure 
link quality, however other metrics might be better 
(or more accurate). However, with experiments so far, 
**replicas recommended for each hop are all identical**, 
which raises another question (See Question 2).

(7). Measure using virtual machines located in different geographical regions.

_**Result 1**_: although _Tencent Videos (v.qq.vom)_ uses 
CDN domains that seem randomly produced, they are actually
fixed in number and content. Totally 119 CDN domains are
used in Beijing and Shenzhen, and they are exactly the same.

