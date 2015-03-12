# -*- coding: utf-8 -*-
import os
import re
import subprocess
INDIR = '/media/sf_win_home/Documents/BOOKSCAN/'
#OUTDIR = '/Users/nishio/Dropbox/_References/txt/bookscan'
OUTDIR = '/media/sf_Dropbox/_References/txt/bookscan'

def cleaning_for_japanese(filename):
    data = file(filename).read()

    # UTF-8以外の文字を無視する
    data = data.decode('utf-8', 'ignore')
    # ハイフネーションを潰す
    data = re.sub('-[\r\n]+', '', data)
    # 改行・空白を無視する
    data = re.sub('[ \r\n\x0c]+', '', data)
    # タグを無視する
    data = re.sub('\(cid:\d+\)', '', data)
    # 合字を元に戻す
    data = data.replace(u'ﬃ', u'ffi')
    data = data.replace(u'ﬂ', u'fl')
    data = data.replace(u'ﬁ', u'fi')
    data = data.replace(u'ﬀ', u'ff')
    # 約物などを空白に置き換える
    data = re.sub('\.\.\.+', ' ', data)
    data = re.sub('[•・、（）()「 」『 』｛ ｝［ ］〔 〕〈 〉《 》【 】〖 〗‥…゠]', ' ', data)

    # 句点で分割して書き戻す
    fo = file(filename, 'w')
    for line in data.split(u'。'):
        if not line: continue
        line = line.encode('utf-8')
        fo.write(line)
        fo.write('\n')
    fo.close()

for filename in os.listdir(INDIR): # (1)
    if filename.startswith('iphone4_'): continue
    if filename.startswith('iphone5_'): continue
    if filename.startswith('.'): continue
    if not filename.endswith('.pdf'): continue
    print filename
    outfile = os.path.join(OUTDIR, filename).replace('.pdf', '.txt')
    infile = os.path.join(INDIR, filename)
    if os.path.isfile(outfile):
        print 'already exists'
        continue
    subprocess.check_call(['pdf2txt.py', '-V', '-o', outfile, infile]) # (2)
    cleaning_for_japanese(outfile) # (3)
