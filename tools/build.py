"""Build both pages from data/tracker.json.
private: data inline (published as the private Claude page)
public : data encrypted to the public key; only the password unlocks it (GitHub Pages)"""
import os, json, base64, sys
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
W = sys.argv[1]
data = open(f"{W}/data/tracker.json", encoding="utf-8").read()
json.loads(data)
tpl = open(f"{W}/src/template.html", encoding="utf-8").read()
safe = data.replace("</", "<\\/")
priv = tpl.replace("/*__BOOT__*/", 'const BOOT={mode:"plain",data:' + safe + '};')
open(f"{W}/dist/private/index.html","w",encoding="utf-8").write(priv)
pub = serialization.load_pem_public_key(open(f"{W}/keys/public.pem","rb").read())
wp = json.load(open(f"{W}/keys/wrapped_private.json"))
dk, iv = os.urandom(32), os.urandom(12)
ct = AESGCM(dk).encrypt(iv, data.encode("utf-8"), None)
ek = pub.encrypt(dk, padding.OAEP(mgf=padding.MGF1(hashes.SHA256()), algorithm=hashes.SHA256(), label=None))
b = lambda x: base64.b64encode(x).decode()
payload = dict(wp=wp, ek=b(ek), iv=b(iv), ct=b(ct))
public = tpl.replace("/*__BOOT__*/", "const BOOT={mode:\"locked\",payload:" + json.dumps(payload) + "};")
public = ('<!doctype html><html lang="en"><head><meta charset="utf-8">'
          '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
          '<meta name="robots" content="noindex,nofollow"><meta name="referrer" content="no-referrer">'
          '<style>:root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}body{margin:0}[hidden]{display:none!important}img{max-width:100%}</style>'
          '</head><body>' + public + '</body></html>')
open(f"{W}/dist/public/index.html","w",encoding="utf-8").write(public)
print("built", len(priv)//1024, "KB private,", len(public)//1024, "KB public")
