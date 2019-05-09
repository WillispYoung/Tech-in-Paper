#### 1. Why EDNS field in subsequent DNS responses is missing?
Supposed local DNS cached such results. Caching policy actually 
should not stop us from conducting subnet assimilation, as lack 
of support for EDNS option is harmless to such operations.

****

#### 2. How URLs of CDN servers with random first entry produced? 
In another word, how does **Name Server** work while cooperating 
with **Content Providers**? Is provided CDN URL __produced with the 
knowledge of client presence__, or is it hard coded and __only DNS 
resolution will take client presence into consideration__?

Solution:

1. Capture CDN URLs from **Content Providers** in different 
geographical locations, check if appeared URLs have any 
intersection. In what **space scale** would results differ?

****

#### 3. How to locate and select optimal replicas?