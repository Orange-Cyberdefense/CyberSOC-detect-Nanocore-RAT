#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# Orange Cyberdefense - Cyber SOC Paris 
# https://orangecyberdefense.com

import csv

# values extract from nanocore source code
string2 = ['ss', 'mon', 'mgr', 'sv', 'svc', 'host']
string3 = ['Subsystem', 'Monitor', 'Manager', 'Service', 'Service', 'Host']
string4 = ['dhcp', 'upnp', 'tcp', 'udp', 'saas', 'iss', 'smtp', \
            'dos', 'dpi', 'pci', 'scsi', 'wan', 'lan', 'nat', 'imap', \
            'nas', 'ntfs', 'wpa', 'dsl', 'agp', 'arp', 'ddp', 'dns']

if __name__ == "__main__":
    #comprehension list to create all possible combinations of keys and values
    key = [s4.upper() + ' ' + s3 for s4 in string4 for s3 in string3]
    val = [s4 + s2 + '.exe' for s4 in string4 for s2 in string2]
    
    #build a csv file
    with open('nanocore_pattern.csv', 'w') as f:
        f.write('{0},{1},{2}\n'.format('RUN Key Name', 'Value', 'Description'))
        for k,v in zip(key, val):
            f.write('{0},*\{1},{2}\n'.format(str(k), str(v), 'Nanocore-RAT'))
