'''
A super simple HTTPS, SSL webserver for python 3.1 (py3k) without using any
external library.
 
You can make a cert/key with openssl using:
openssl req -new -x509 -days 365 -nodes -out cert.pem -keyout cert.pem
as taken from http://docs.python.org/dev/library/ssl.html#certificates
 
If you want to test this with htto://localhost/ you can use this certificate
and key, just dump this in the file 'localhost.pem' next to this code:
 
-----BEGIN RSA PRIVATE KEY-----
MIICXQIBAAKBgQDuYevSemcuxxZgjQt6j1KmPt60o5RfOJWFwic7knnQ5Hgfkuqk
yUObKhZMhYLpe1FYr9wo20YeA+XKm2q+celiwqbzNM3FIM5ytF/pGfrNmqVI2NVd
FUVwfwhlDEWXR1+PGs1TEPXHSyX7rR0EmQaswfrVN27e1OvQKh2L62EoDQIDAQAB
AoGASl+Usstrq+WDbsYyoZ9buvB8jUFIBlliFSRZFzYA+ZJ+g+NTf+wnQp7j7CXv
jSbjX1cmyjx3aN/wbsEEkbx6grJmXUxJ7GMq7fE94Q7uP5JnWn2CJM3P4AVWpL2H
wkxareRe+rUi88yliwe60b3rQFn5BH5E/tcgUAL6TskhVAECQQD8uQojryg2GOrC
9A5gn3ELjMeZ/wnv5obaUwvnJSCgvjCIJsDzDu/gYMeaHGCu1SkpTpkyq9HiZHWL
Bto3/+MNAkEA8XlGuNyyw23qDIrQImW1novqytE82R1ItNatCmChqzaIHTm+kxHc
kWDVTjzBmnpAvGAuWwHc5+wW7wnZ9ckZAQJASQVOILFjdP4OFvZdkR2AlE3A/oXq
YR7CqCKGterMWqWZcD2CUrhmJvbPtX+tj9aXZhAHw9RReJB+RgVc2AFfoQJBANPf
RFVpmBRveZ/doHe95FijjbS9WHVsA2Jgxl3HobKXW2DBTNzAHFcWrrJCDuFbCTf/
8Ex72vdHqGu+qhbFhwECQQC3cmrASJZbRU7By5nZmz+Vgl9nvR2CNg/Tmd4SYvBK
dyXCbEHZp84F+3nuCNAtTV1/RsB+qr6HJoMNeXizMs7Q
-----END RSA PRIVATE KEY-----
-----BEGIN CERTIFICATE-----
MIIDuDCCAyGgAwIBAgIJALuyVKnJVXpSMA0GCSqGSIb3DQEBBQUAMIGaMQswCQYD
VQQGEwJBVTETMBEGA1UECBMKU29tZS1TdGF0ZTEOMAwGA1UEBxMFQ2l0YXkxITAf
BgNVBAoTGEludGVybmV0IFdpZGdpdHMgUHR5IEx0ZDEOMAwGA1UECxMFVW5pdHkx
EjAQBgNVBAMTCWxvY2FsaG9zdDEfMB0GCSqGSIb3DQEJARYQbXJAY29ycG9yYXRl
LmNvbTAeFw0xMDAzMTUxNjExNDlaFw0xMTAzMTUxNjExNDlaMIGaMQswCQYDVQQG
EwJBVTETMBEGA1UECBMKU29tZS1TdGF0ZTEOMAwGA1UEBxMFQ2l0YXkxITAfBgNV
BAoTGEludGVybmV0IFdpZGdpdHMgUHR5IEx0ZDEOMAwGA1UECxMFVW5pdHkxEjAQ
BgNVBAMTCWxvY2FsaG9zdDEfMB0GCSqGSIb3DQEJARYQbXJAY29ycG9yYXRlLmNv
bTCBnzANBgkqhkiG9w0BAQEFAAOBjQAwgYkCgYEA7mHr0npnLscWYI0Leo9Spj7e
tKOUXziVhcInO5J50OR4H5LqpMlDmyoWTIWC6XtRWK/cKNtGHgPlyptqvnHpYsKm
8zTNxSDOcrRf6Rn6zZqlSNjVXRVFcH8IZQxFl0dfjxrNUxD1x0sl+60dBJkGrMH6
1Tdu3tTr0Codi+thKA0CAwEAAaOCAQIwgf8wHQYDVR0OBBYEFCu6OdDstIRhZd9U
ql9Ig3t9LFebMIHPBgNVHSMEgccwgcSAFCu6OdDstIRhZd9Uql9Ig3t9LFeboYGg
pIGdMIGaMQswCQYDVQQGEwJBVTETMBEGA1UECBMKU29tZS1TdGF0ZTEOMAwGA1UE
BxMFQ2l0YXkxITAfBgNVBAoTGEludGVybmV0IFdpZGdpdHMgUHR5IEx0ZDEOMAwG
A1UECxMFVW5pdHkxEjAQBgNVBAMTCWxvY2FsaG9zdDEfMB0GCSqGSIb3DQEJARYQ
bXJAY29ycG9yYXRlLmNvbYIJALuyVKnJVXpSMAwGA1UdEwQFMAMBAf8wDQYJKoZI
hvcNAQEFBQADgYEAsbQouDB+z/bhyumCXwOG1d1QljV2zlBnjIS8b3F3T+usJxe3
W61wqNM8E0B8vJwu0Tm7Tilwe9h73UIaKgJ/t8BohjnxpKo+MyiPwjYu6Y5FmdEX
c9ltsmsTtFFjIEX60XVyqz+x2A4bGebd3StVf+2L9jZn1MB18O5OkwzbBbM=
-----END CERTIFICATE-----

SimpleSecureHTTPServer.py - simple HTTP server supporting SSL.

- replace fpem with the location of your .pem server file.
- the default port is 443.

usage: python SimpleSecureHTTPServer.py
'''

import socket, os
from SocketServer import BaseServer
from BaseHTTPServer import HTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler
from OpenSSL import SSL


class SecureHTTPServer(HTTPServer):
    def __init__(self, server_address, HandlerClass):
        BaseServer.__init__(self, server_address, HandlerClass)
        ctx = SSL.Context(SSL.SSLv23_METHOD)
        #server.pem's location (containing the server private key and
        #the server certificate).
        fpem = 'test.pem'
        ctx.use_privatekey_file (fpem)
        ctx.use_certificate_file(fpem)
        self.socket = SSL.Connection(ctx, socket.socket(self.address_family,
                                                        self.socket_type))
        self.server_bind()
        self.server_activate()

    def shutdown_request(self,request):
        request.shutdown()

class SecureHTTPRequestHandler(SimpleHTTPRequestHandler):
    def setup(self):
        self.connection = self.request
        self.rfile = socket._fileobject(self.request, "rb", self.rbufsize)
        self.wfile = socket._fileobject(self.request, "wb", self.wbufsize)


def test(HandlerClass = SecureHTTPRequestHandler,
         ServerClass = SecureHTTPServer):
    server_address = ('', 443) # (address, port)
    httpd = ServerClass(server_address, HandlerClass)
    sa = httpd.socket.getsockname()
    print "Serving HTTPS on", sa[0], "port", sa[1], "..."
    httpd.serve_forever()


if __name__ == '__main__':
    test()
