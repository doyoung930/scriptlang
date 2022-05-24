import http.client
import urllib.request
from xml.dom.minidom import parseString

server = "openapi.gg.go.kr"
#key_value = 3cccb5986c79462dae3acd235fa8a54f

conn = http.client.HTTPSConnection(server)

conn.request(
    "GET",
    "/PublicLivelihood?KEY=3cccb5986c79462dae3acd235fa8a54f"
)

res = conn.getresponse()

if int(res.status) == 200:
    print("읽어 오는데 성공")
    print(parseString(res.read().decode('utf-8')).toprettyxml())
else:
    print('HTTP request failed : ', res.reason)