#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 8/7/19 8:20 PM
# @Author  : Archerx
# @Blog    : https://blog.ixuchao.cn
# @File    : json_format.py

import json
di = {'hostnames': [{'name': '', 'type': ''}], 'addresses': {'ipv4': '149.129.89.93'}, 'vendor': {}, 'status': {'state': 'up', 'reason': 'user-set'}, 'tcp': {21: {'state': 'filtered', 'reason': 'no-response', 'name': 'ftp', 'product': '', 'version': '', 'extrainfo': '', 'conf': '3', 'cpe': ''}, 22: {'state': 'open', 'reason': 'syn-ack', 'name': 'ssh', 'product': 'OpenSSH', 'version': '7.2p2 Ubuntu 4ubuntu2.2', 'extrainfo': 'Ubuntu Linux; protocol 2.0', 'conf': '10', 'cpe': 'cpe:/o:linux:linux_kernel'}, 23: {'state': 'filtered', 'reason': 'no-response', 'name': 'telnet', 'product': '', 'version': '', 'extrainfo': '', 'conf': '3', 'cpe': ''}, 25: {'state': 'filtered', 'reason': 'no-response', 'name': 'smtp', 'product': '', 'version': '', 'extrainfo': '', 'conf': '3', 'cpe': ''}, 80: {'state': 'open', 'reason': 'syn-ack', 'name': 'http', 'product': 'nginx', 'version': '1.10.3', 'extrainfo': 'Ubuntu', 'conf': '10', 'cpe': 'cpe:/o:linux:linux_kernel'}, 110: {'state': 'filtered', 'reason': 'no-response', 'name': 'pop3', 'product': '', 'version': '', 'extrainfo': '', 'conf': '3', 'cpe': ''}, 115: {'state': 'filtered', 'reason': 'no-response', 'name': 'sftp', 'product': '', 'version': '', 'extrainfo': '', 'conf': '3', 'cpe': ''}, 139: {'state': 'filtered', 'reason': 'no-response', 'name': 'netbios-ssn', 'product': '', 'version': '', 'extrainfo': '', 'conf': '3', 'cpe': ''}, 143: {'state': 'filtered', 'reason': 'no-response', 'name': 'imap', 'product': '', 'version': '', 'extrainfo': '', 'conf': '3', 'cpe': ''}, 443: {'state': 'open', 'reason': 'syn-ack', 'name': 'http', 'product': 'nginx', 'version': '1.10.3', 'extrainfo': 'Ubuntu', 'conf': '10', 'cpe': 'cpe:/o:linux:linux_kernel'}, 445: {'state': 'filtered', 'reason': 'no-response', 'name': 'microsoft-ds', 'product': '', 'version': '', 'extrainfo': '', 'conf': '3', 'cpe': ''}, 547: {'state': 'filtered', 'reason': 'no-response', 'name': 'dhcpv6-server', 'product': '', 'version': '', 'extrainfo': '', 'conf': '3', 'cpe': ''}, 1433: {'state': 'filtered', 'reason': 'no-response', 'name': 'ms-sql-s', 'product': '', 'version': '', 'extrainfo': '', 'conf': '3', 'cpe': ''}, 1521: {'state': 'filtered', 'reason': 'no-response', 'name': 'oracle', 'product': '', 'version': '', 'extrainfo': '', 'conf': '3', 'cpe': ''}, 3306: {'state': 'filtered', 'reason': 'no-response', 'name': 'mysql', 'product': '', 'version': '', 'extrainfo': '', 'conf': '3', 'cpe': ''}, 3389: {'state': 'filtered', 'reason': 'no-response', 'name': 'ms-wbt-server', 'product': '', 'version': '', 'extrainfo': '', 'conf': '3', 'cpe': ''}, 3690: {'state': 'filtered', 'reason': 'no-response', 'name': 'svn', 'product': '', 'version': '', 'extrainfo': '', 'conf': '3', 'cpe': ''}, 5432: {'state': 'filtered', 'reason': 'no-response', 'name': 'postgresql', 'product': '', 'version': '', 'extrainfo': '', 'conf': '3', 'cpe': ''}, 5901: {'state': 'filtered', 'reason': 'no-response', 'name': 'vnc-1', 'product': '', 'version': '', 'extrainfo': '', 'conf': '3', 'cpe': ''}, 5902: {'state': 'filtered', 'reason': 'no-response', 'name': 'vnc-2', 'product': '', 'version': '', 'extrainfo': '', 'conf': '3', 'cpe': ''}, 5903: {'state': 'filtered', 'reason': 'no-response', 'name': 'vnc-3', 'product': '', 'version': '', 'extrainfo': '', 'conf': '3', 'cpe': ''}, 6379: {'state': 'filtered', 'reason': 'no-response', 'name': 'redis', 'product': '', 'version': '', 'extrainfo': '', 'conf': '3', 'cpe': ''}, 7001: {'state': 'filtered', 'reason': 'no-response', 'name': 'afs3-callback', 'product': '', 'version': '', 'extrainfo': '', 'conf': '3', 'cpe': ''}, 8080: {'state': 'filtered', 'reason': 'no-response', 'name': 'http-proxy', 'product': '', 'version': '', 'extrainfo': '', 'conf': '3', 'cpe': ''}, 11211: {'state': 'filtered', 'reason': 'no-response', 'name': 'memcache', 'product': '', 'version': '', 'extrainfo': '', 'conf': '3', 'cpe': ''}, 27017: {'state': 'filtered', 'reason': 'no-response', 'name': 'mongod', 'product': '', 'version': '', 'extrainfo': '', 'conf': '3', 'cpe': ''}}}

print (json.dumps(di, indent=4))