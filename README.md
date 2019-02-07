# simple-siem-poc

Implementing host portscan detection with Elasticsearch and Python.

Don't forget install Elasticsearch and Logstash.

> $ sudo tcpdump -nS -i {DEVICE} -s0 -tttt | nc -unv {LOGSTASH_SERVER_ADDR} 5000

Referance:

[Elasticsearch and SIEM: implementing host portscan detection](https://www.elastic.co/blog/elasticsearch-and-siem-implementing-host-portscan-detection)