################################################################################
# 1. fill in tumblr oauth client information & blog_identifier:
#      https://api.tumblr.com/console/calls/user/info
#
# 2. run the script (cron it if u want):
#      it creates /distribute and index.index
#
# /distribute:
#     where you place your images for distribution
# index.index:
#     keeps track of what files have been distributed (delete to re-upload)
################################################################################

import pytumblr
import os
import shutil

client = pytumblr.TumblrRestClient(
  '...............YOUR_MAGIC_KEYS_AND_TOKENS_HERE...............',
  '...............YOUR_MAGIC_KEYS_AND_TOKENS_HERE...............',
  '...............YOUR_MAGIC_KEYS_AND_TOKENS_HERE...............',
  '...............YOUR_MAGIC_KEYS_AND_TOKENS_HERE...............'
)

blog_identifier = "YOUR_TUMBLR_BLOG_IDENTIFIER_HERE"

rootfiles = os.listdir('.')

# if no 'uploaded' and or 'fresh' dirs, create them
if "distribute" not in rootfiles:
    os.mkdir("distribute")

# ensure index.index exists (non-destructive)
open("index.index", "a").close()

indexread = open("index.index", "r")
index_files = indexread.read().splitlines()
indexread.close()

files = os.listdir('./distribute')
for f in files:
    thefile = "./distribute/" + f
    filename, file_extension = os.path.splitext(thefile)
    if file_extension in [".png", ".jpg", ".gif"]:
        # is file not in index?
        if (f not in index_files):

            indexappend = open("index.index", "a")

            # post to tumblr (with the 'my art' tag)
            print("uploading " + thefile)
            client.create_photo(blog_identifier, tags=["my art"], data=thefile)

            # append to index
            indexappend.write(f+"\n")

            indexappend.close()
