### Service Quality Improvement Targeted for CDNs | 针对CDN的服务质量提升

#### 1. Measuring Procedure | 测量流程
(1). Get media file URLs from many CP websites (selenium). 
| 获取内容提供网站的媒体文件对应的URL

_**v.qq.com**_: locate *txpdiv* element with attribute 
*data-role* set as **txp-ui-console-cdn**, its innerHTML
 (if not empty) will be CDN server's domain for this web 
 page. These domains are in the form of 
 https://apd-4ca339c635848992779008d33f0ee5a5.v.smtcdns.com. 
 See data_crawler/crawler.py. Name server: _smtcdns.com_. 
 | 获取页面中的<txpdiv>标签，如果其data-role属性为txp-ui-console-cdn，
 那么这个标签的内容（innerHTML）就会是当前页面会使用到的CDN。
 形式为*.v.smtcdns.com。

_**youku.com**_: no element can indicate CDN server's address 
information, but inferring from network information its CDN 
server is fixed as https://valipl.cp31.ott.cibntv.net. 
Name server: _cibntv.net_. 
| 页面中的元素不能说明CDN服务器的地址信息，但是通过Chrome的
Network功能发现，CDN服务器是固定的。

_**iqiyi.com**_: CDN servers' domain are like 
https://v-3acdc404.71edge.com, which in this case is 
a _CERNET_ machine. Name server: _71edge.com_.
| 与优酷类似，页面元素不能说明CDN服务器的地址信息。

As conclusion, all these CP websites host their media 
files on certain CDN servers, which differ only in the 
first entry of domain. 
| 上述三个内容提供网站都只使用一个CDN。

(2). Check if ECS is supported for each domain (EDNS).
| 检查每个媒体文件所属的CDN域名是否支持ECS选项。

Judging from simple tests, CDNs listed above all support 
ECS option. Supposedly, local DNS cache might lead to 
elimination of support in following DNS responses.
| 简单测试来看，上述三个网站使用的CDN服务器都支持ECS，但是本地的
DNS服务器似乎会缓存之前的DNS结果，导致后续的DNS响应中不会显示对
ECS的支持性。

(3). Get suggested replicas from ENDS. | 获取推荐的复制服务器

With URLs of CDN servers acquired, replicas are actually 
IP list contained in DNS response while resolving these 
domain names. 
| 复制服务器指的是一个域名对应的所有IP地址，因此使用DNS查询即可。

(4). Trace route these replicas to identify hops along the path.
| 路由追踪这些复制服务器，来获取到服务器各跳的IP。

Currently, this procedure is conducted by manually type 
_tracert_ command in terminal. All results are stored in 
**data** folder, with filename in the form of _traces*.txt_.
| 目前是通过在命令行手动输入tracert命令，然后记录输出的内容来获取。
下一步会使用代码来实现。

(5). Assimilate each hop to get its suggested replicas.
| 模拟每一条，来获取其推荐的复制品服务器。

Altering _subnet_ field in EDNS packet, then recommended 
replicas for each hop are contained in each relative EDNS 
response. Results are stored in **data** folder, with 
filename in the form of _subnet-assimilation*.txt_.
| 将EDNS包的subnet域修改成各跳的IP，可以获得各跳对应的推荐IP。

_Home experiments need re-conduct. -- finished._

(6). Measure link qualities to these replicas.
| 测量到这些复制服务器的链路质量。

Currently ping delay is used as the sole metric to measure 
link quality, however other metrics might be better 
(or more accurate). However, with experiments so far, 
**replicas recommended for each hop are all identical**, 
which raises another question (See Question 2). 
| 当前只是用ping获得的延迟作为衡量链路质量的标准，之后可以
添加其他衡量标准。然而由于目前对于特定CDN域名，各跳获得的IP
都是相同的，因此这种情况下并没有测量的必要。

(7). Measure using virtual machines located in different geographical regions. 
| 在位于不同地理位置的虚拟机上进行测量。

_**Result 1**_: although _Tencent Videos (v.qq.vom)_ uses 
CDN domains that seem randomly produced, they are actually
fixed in number and content. Totally 119 CDN domains are
used in Beijing and Shenzhen, and they are exactly the same. 
| 尽管腾讯视频使用了看起来像是随机生成的CDN域名地址，但是实际上在北京
和在深圳的测量结果完全一致，均使用了119个相同的CDN域名。因此，实际上
并没有考虑到客户端的IP来分配域名。

#### 2. Measurement Discovery | 测量发现

接下来有两个问题：
1. 这些域名中是否存在与地理位置相关的DNS解析结果？
2. 这些域名对应的服务器是怎样分布的？有没有可能手动选择这些CDN服务器，
而不使用腾讯视频随机分配的CDN服务器？

结果：
1. 在北京和深圳进行DNS解析，结果完全相同，并且每个域名只有一个IP。
同时，ping这些域名发现，在北京ping的结果普遍**小于10ms**，而在深圳，
延迟则达到了**50ms左右及以上**。
