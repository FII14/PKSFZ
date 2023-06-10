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

exec(base64.b64decode("IyEvdXNyL2Jpbi9lbnYgcHl0aG9uMwoKaW1wb3J0IHppcGZpbGUKaW1wb3J0IG9zCmltcG9ydCB0aW1lCmltcG9ydCBzeXMKCmlmIG9zLm5hbWUgPT0gIm50IjoKICAgIG9zLnN5c3RlbSgiY2xzIikKZWxzZToKICAgIG9zLnN5c3RlbSgiY2xlYXIiKQoKcHJpbnQoIiIiCistLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0rCnwgUHJvZ3JhbSA6IFBlbWVjYWgga2F0YSBzYW5kaSBmaWxlIFpJUCAgICB8CnwgUGVtYnVhdCA6IFJvZmkgW0ZJSTE0XSAgICAgICAgICAgICAgICAgICB8ICAKfCBHaXRodWIgIDogaHR0cHM6Ly9naXRodWIuY29tL0ZJSTE0L1BLU0ZaIHwKKy0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLSsKfCBDT1BZUklHSFQgKEMpIDIwMjMgRklJMTQgICAgICAgICAgICAgICAgIHwKKy0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLSsKIiIiKQoKd2hpbGUgVHJ1ZToKICAgIHRyeToKICAgICAgICAjIE1lbWludGEgaW5wdXQgbmFtYSBmaWxlIFpJUAogICAgICAgIG5hbWFfZmlsZV96aXAgPSBpbnB1dCgiTWFzdWtrYW4gbmFtYSBmaWxlIFpJUDogIikKCiAgICAgICAgIyBNZW1lcmlrc2EgYXBha2FoIGZpbGUgWklQIGFkYQogICAgICAgIGlmIG5vdCBvcy5wYXRoLmlzZmlsZShuYW1hX2ZpbGVfemlwKToKICAgICAgICAgICAgcHJpbnQoIkZpbGUgWklQIHRpZGFrIGRpdGVtdWthbi4iKQogICAgICAgIGVsc2U6CiAgICAgICAgICAgIGJyZWFrCiAgICBleGNlcHQgS2V5Ym9hcmRJbnRlcnJ1cHQ6CiAgICAgICAgcHJpbnQoIlxuS2VsdWFyIGRhcmkgcHJvZ3JhbSBQS1NGWiIpCiAgICAgICAgZXhpdCgwKQoKd2hpbGUgVHJ1ZToKICAgIHRyeToKICAgICAgICAjIE1lbWludGEgaW5wdXQgbmFtYSBmaWxlIHdvcmRsaXN0CiAgICAgICAgbmFtYV9maWxlX3dvcmRsaXN0ID0gaW5wdXQoIk1hc3Vra2FuIG5hbWEgZmlsZSB3b3JkbGlzdDogIikKCiAgICAgICAgIyBNZW1lcmlrc2EgYXBha2FoIGZpbGUgd29yZGxpc3QgYWRhCiAgICAgICAgaWYgbm90IG9zLnBhdGguaXNmaWxlKG5hbWFfZmlsZV93b3JkbGlzdCk6CiAgICAgICAgICAgIHByaW50KCJGaWxlIHdvcmRsaXN0IHRpZGFrIGRpdGVtdWthbi4iKQogICAgICAgIGVsc2U6CiAgICAgICAgICAgIGJyZWFrCiAgICBleGNlcHQgS2V5Ym9hcmRJbnRlcnJ1cHQ6CiAgICAgICAgcHJpbnQoIlxuS2VsdWFyIGRhcmkgcHJvZ3JhbSBQS1NGWiIpCiAgICAgICAgZXhpdCgwKQoKIyBNZW1iYWNhIGZpbGUgd29yZGxpc3QgZGFuIG1lbmNvYmEga2F0YSBzYW5kaQp3aXRoIG9wZW4obmFtYV9maWxlX3dvcmRsaXN0LCAncicpIGFzIHdvcmRsaXN0OgogICAga2F0YV9zYW5kaV9kaXRlbXVrYW4gPSBGYWxzZQogICAgZm9yIGthdGFfc2FuZGkgaW4gd29yZGxpc3Q6CiAgICAgICAga2F0YV9zYW5kaSA9IGthdGFfc2FuZGkuc3RyaXAoKQogICAgICAgIHRyeToKICAgICAgICAgICAgd2l0aCB6aXBmaWxlLlppcEZpbGUobmFtYV9maWxlX3ppcCwgJ3InKSBhcyBmaWxlX3ppcDoKICAgICAgICAgICAgICAgIHN5cy5zdGRvdXQud3JpdGUoZiJcck1lbmNvYmEga2F0YSBzYW5kaToge2thdGFfc2FuZGl9ICIpCiAgICAgICAgICAgICAgICBzeXMuc3Rkb3V0LmZsdXNoKCkKICAgICAgICAgICAgICAgIHRpbWUuc2xlZXAoMC4xKSAgIyBXYWt0dSBqZWRhIGFuaW1hc2kKICAgICAgICAgICAgICAgIGZpbGVfemlwLmV4dHJhY3RhbGwocHdkPWthdGFfc2FuZGkuZW5jb2RlKCkpCiAgICAgICAgICAgICAgICBzeXMuc3Rkb3V0LndyaXRlKCJcbiIpCiAgICAgICAgICAgICAgICBwcmludChmIlxuS2F0YSBzYW5kaSBkaXRlbXVrYW46IHtrYXRhX3NhbmRpfSIpCiAgICAgICAgICAgICAgICBrYXRhX3NhbmRpX2RpdGVtdWthbiA9IFRydWUKICAgICAgICAgICAgICAgIGJyZWFrCiAgICAgICAgZXhjZXB0IEV4Y2VwdGlvbjoKICAgICAgICAgICAgc3lzLnN0ZG91dC53cml0ZSgiXHJNZW5jb2JhIGthdGEgc2FuZGk6ICAgICAgICAgICAgICAgICAgICAiKQogICAgICAgICAgICBzeXMuc3Rkb3V0LmZsdXNoKCkKCiAgICBpZiBub3Qga2F0YV9zYW5kaV9kaXRlbXVrYW46CiAgICAgICAgc3lzLnN0ZG91dC53cml0ZSgiXHJNZW5jb2JhIGthdGEgc2FuZGk6ICAgICAgICAgICAgICAgICAgICBcbiIpCiAgICAgICAgcHJpbnQoIlxuS2F0YSBzYW5kaSB0aWRhayBkaXRlbXVrYW4gZGFsYW0gd29yZGxpc3QuIikKCg=="))