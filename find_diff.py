import os
xs = os.listdir("/media/sf_Dropbox/_References/BOOKSCAN_tune/")
xs = [x.replace("iphone5_", "").replace(".pdf", "") for x in xs]
xs.sort()
print xs[0]
ys = os.listdir("/media/sf_Dropbox/_References/txt/bookscan/")
ys = [y.replace(".txt", "") for y in ys]
ys.sort()
import difflib
ds = difflib.unified_diff(xs, ys)
print "\n".join(d for d in ds if d[0] == "-")
print
print "\n".join(d for d in ds if d[0] == "+")
#print "\n".join(ds)

