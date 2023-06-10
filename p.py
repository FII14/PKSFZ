#!/usr/bin/env python3
#+------------------------------------------+
#| Program : Pemecah kata sandi file ZIP    |
#| Pembuat : Rofi [FII14]                   |  
#| Github  : https://github.com/FII14/PKSFZ |
#+------------------------------------------+
#| COPYRIGHT (C) 2023 FII14                 |
#+------------------------------------------+

# MAU NYOLONG SC YA 🗿

import base64

exec(b64decode("IyEvdXNyL2Jpbi9lbnYgcHl0aG9uMwoKaW1wb3J0IHppcGZpbGUKaW1wb3J0IG9zCmltcG9ydCB0aW1lCmltcG9ydCBzeXMKCmlmIG9zLm5hbWUgPT0gJ250JzoKICAgIG9zLnN5c3RlbSgnY2xzJykKZWxzZToKICAgIG9zLnN5c3RlbSgnY2xlYXInKQoKCnByaW50KCIiIgorLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tKwp8IFByb2dyYW0gOiBQZW1lY2FoIGthdGEgc2FuZGkgZmlsZSBaSVAgICAgfAp8IFBlbWJ1YXQgOiBSb2ZpIFtGSUkxNF0gICAgICAgICAgICAgICAgICAgfCAgCnwgR2l0aHViICA6IGh0dHBzOi8vZ2l0aHViLmNvbS9GSUkxNC9QS1NGWiB8CistLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0rCnwgQ09QWVJJR0hUIChDKSAyMDIzIEZJSTE0ICAgICAgICAgICAgICAgICB8CistLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0rCgoiIiIpCgp3aGlsZSBUcnVlOgogICAgdHJ5OgogICAgICAgICMgTWVtaW50YSBpbnB1dCBuYW1hIGZpbGUgWklQCiAgICAgICAgbmFtYV9maWxlX3ppcCA9IGlucHV0KCJNYXN1a2thbiBuYW1hIGZpbGUgWklQOiAiKQoKICAgICAgICAjIE1lbWVyaWtzYSBhcGFrYWggZmlsZSBaSVAgYWRhCiAgICAgICAgaWYgbm90IG9zLnBhdGguaXNmaWxlKG5hbWFfZmlsZV96aXApOgogICAgICAgICAgICBwcmludCgiRmlsZSBaSVAgdGlkYWsgZGl0ZW11a2FuLiIpCiAgICAgICAgZWxzZToKICAgICAgICAgICAgYnJlYWsKICAgIGV4Y2VwdCBLZXlib2FyZEludGVycnVwdDoKICAgICAgICBwcmludCgiXG5LZWx1YXIgZGFyaSBwcm9ncmFtIFBLU0ZaIikKICAgICAgICBleGl0KDApCgp3aGlsZSBUcnVlOgogICAgdHJ5OgogICAgICAgICMgTWVtaW50YSBpbnB1dCBuYW1hIGZpbGUgd29yZGxpc3QKICAgICAgICBuYW1hX2ZpbGVfd29yZGxpc3QgPSBpbnB1dCgiTWFzdWtrYW4gbmFtYSBmaWxlIHdvcmRsaXN0OiAiKQoKICAgICAgICAjIE1lbWVyaWtzYSBhcGFrYWggZmlsZSB3b3JkbGlzdCBhZGEKICAgICAgICBpZiBub3Qgb3MucGF0aC5pc2ZpbGUobmFtYV9maWxlX3dvcmRsaXN0KToKICAgICAgICAgICAgcHJpbnQoIkZpbGUgd29yZGxpc3QgdGlkYWsgZGl0ZW11a2FuLiIpCiAgICAgICAgZWxzZToKICAgICAgICAgICAgYnJlYWsKICAgIGV4Y2VwdCBLZXlib2FyZEludGVycnVwdDoKICAgICAgICBwcmludCgiXG5LZWx1YXIgZGFyaSBwcm9ncmFtIFBLU0ZaIikKICAgICAgICBleGl0KDApCgojIE1lbWJhY2EgZmlsZSB3b3JkbGlzdCBkYW4gbWVuY29iYSBrYXRhIHNhbmRpCndpdGggb3BlbihuYW1hX2ZpbGVfd29yZGxpc3QsICdyJykgYXMgd29yZGxpc3Q6CiAgICBrYXRhX3NhbmRpX2RpdGVtdWthbiA9IEZhbHNlCiAgICBmb3Iga2F0YV9zYW5kaSBpbiB3b3JkbGlzdDoKICAgICAgICBrYXRhX3NhbmRpID0ga2F0YV9zYW5kaS5zdHJpcCgpCiAgICAgICAgdHJ5OgogICAgICAgICAgICB3aXRoIHppcGZpbGUuWmlwRmlsZShuYW1hX2ZpbGVfemlwLCAncicpIGFzIGZpbGVfemlwOgogICAgICAgICAgICAgICAgc3lzLnN0ZG91dC53cml0ZShmIlxyTWVuY29iYSBrYXRhIHNhbmRpOiB7a2F0YV9zYW5kaX0gIikKICAgICAgICAgICAgICAgIHN5cy5zdGRvdXQuZmx1c2goKQogICAgICAgICAgICAgICAgdGltZS5zbGVlcCgwLjEpICAjIFdha3R1IGplZGEgYW5pbWFzaQogICAgICAgICAgICAgICAgZmlsZV96aXAuZXh0cmFjdGFsbChwd2Q9a2F0YV9zYW5kaS5lbmNvZGUoKSkKICAgICAgICAgICAgICAgIHN5cy5zdGRvdXQud3JpdGUoIlxuIikKICAgICAgICAgICAgICAgIHByaW50KGYiS2F0YSBzYW5kaSBkaXRlbXVrYW46IHtrYXRhX3NhbmRpfSIpCiAgICAgICAgICAgICAgICBrYXRhX3NhbmRpX2RpdGVtdWthbiA9IFRydWUKICAgICAgICAgICAgICAgIGJyZWFrCiAgICAgICAgZXhjZXB0IEV4Y2VwdGlvbjoKICAgICAgICAgICAgc3lzLnN0ZG91dC53cml0ZSgiXHJNZW5jb2JhIGthdGEgc2FuZGk6ICAgICAgICAgICAgICAgICAgICAiKQogICAgICAgICAgICBzeXMuc3Rkb3V0LmZsdXNoKCkKCiAgICBpZiBub3Qga2F0YV9zYW5kaV9kaXRlbXVrYW46CiAgICAgICAgc3lzLnN0ZG91dC53cml0ZSgiXHJNZW5jb2JhIGthdGEgc2FuZGk6ICAgICAgICAgICAgICAgICAgICBcbiIpCiAgICAgICAgcHJpbnQoIkthdGEgc2FuZGkgdGlkYWsgZGl0ZW11a2FuIGRhbGFtIHdvcmRsaXN0LiIpCg=="))
