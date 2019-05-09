#### 1. Why EDNS field in subsequent DNS responses is missing?
Supposed local DNS cached such results. Caching policy actually 
should not stop us from conducting subnet assimilation, as lack 
of support for EDNS option is harmless to such operations.

****

#### 2. How URLs of CDN servers with random first entry produced? 
In another word, how does **Name Server** work while cooperating 
with **Content Providers**?

Solution:

1. Capture CDN URLs from **Content Providers** in different 
geographical locations, check if appeared URLs have any 
intersection as a case study.

1.1 Locations: <span style="color:blue">cloud 203</span>, dormitory, home. 


****

#### 3. How to locate and select optimal replicas?