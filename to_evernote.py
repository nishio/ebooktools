import os
import codecs
INDIR = "/media/sf_Dropbox/_References/txt/bookscan/"
OUTDIR = "/media/sf_win_home/Documents/import_to_evernote_bookscan"
for f in os.listdir(INDIR):
    outpath = os.path.join(OUTDIR, f)
    if os.path.isfile(outpath):
        print 'already exists', f
        continue
    data = file(os.path.join(INDIR, f)).read()
    fo = file(outpath, "w")
    fo.write(f.decode("utf-8", "ignore").encode("sjis", "ignore") + "\n")
    fo.write(data.decode("utf-8", "ignore").encode("sjis", "ignore"))
    fo.close()
    print 'done', f



