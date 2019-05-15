#### 1. Why EDNS field in subsequent DNS responses is missing? | 为什么后续的DNS请求中没有EDNS域？
Supposedly local DNS cached such results. Caching policy actually 
should not stop us from conducting subnet assimilation, as lack 
of support for EDNS option is harmless to such operations. 
| 猜测是本地的DNS服务器缓存了这些结果。然而EDNS域的消失不应当作为
不进行子网同化测试的根据，因为子网同化实际上是不需要依赖这一域的。

****

#### 2. How URLs of CDN servers with random first entry produced? | 随机的CDN服务器的域名是怎样生成的？
In another word, how does **Name Server** work while cooperating 
with **Content Providers**? Is provided CDN URL __produced with the 
knowledge of client presence__, or is it hard coded and __only DNS 
resolution will take client presence into consideration__? 
| 换言之，域名服务器是怎样与内容提供网站合作来生成这些CDN服务器的URL的？
这一生成过程是否考虑了客户端的IP，还是在进行DNS解析的过程中考虑到了客户端的IP?

Solution: | 解决方案

1. Capture CDN URLs from **Content Providers** in different 
geographical locations, check if appeared URLs have any 
intersection. In what **space scale** would results differ?
| 从不同的地理位置获取内容提供网站的CDN服务器域名，检查不同地点的
所有CDN域名是否有重叠。在怎样的空间尺度上，结果才会有所不同呢？（见主README）

****

#### 3. How to locate and select optimal replicas? | 怎样定位和选择最佳的复制服务器？

对于腾讯视频来说，使用到的CDN服务器和地理位置无关，并且DNS解析的结果也无关。
因此仿照Drongo来从链路各跳中获取最佳的推荐的复制服务器是不可行的。
初步考虑是从所有可行的CDN服务器中选取最佳的服务器，
来代替腾讯视频本身给出的推荐CDN服务器。