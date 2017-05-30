import codecs
import os

output_dir = "/Users/dhg/workspace/symposiumPrep/train_output_17-05-24"
website_dir = "/Users/dhg/workspace/halperta/firstbooks/transcriptions"

for book_name in os.listdir(output_dir):
  if book_name[0] != '.':  # skip hidden files
    if not os.path.exists("%s/%s" % (website_dir, book_name)):
      os.makedirs("%s/%s" % (website_dir, book_name))
    book_dir = '%s/%s/all_transcriptions/1000/' % (output_dir, book_name)
    for filename in os.listdir(book_dir):
      # pl_blac_012_00019-1000_iter-3_transcription_normalized.txt
      suffix = "-1000_iter-3_transcription.txt"
      if filename.endswith(suffix):
        output_filename = "%s/%s/%s.html" % (website_dir, book_name, filename[:-len(suffix)])
        print 'Writing %s' % (output_filename)
        with codecs.open(output_filename, 'w', encoding='utf8') as fout:
          with codecs.open("%s/%s" % (book_dir, filename), 'r', encoding='utf8') as fin:
            for line in fin:
              fout.write("%s<br/>\n" % (line.strip()))

