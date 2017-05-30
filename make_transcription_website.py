import codecs
import os

output_dir = "/Users/dhg/workspace/symposiumPrep/train_output_17-05-24"
website_dir = "/Users/dhg/workspace/halperta/firstbooks/transcriptions"
website_image_size = "800"  # 400, 800, 1000

for book_name in os.listdir(output_dir):
  if book_name[0] != '.':  # skip hidden files
    if not os.path.exists("%s/%s" % (website_dir, book_name)):
      os.makedirs("%s/%s" % (website_dir, book_name))
    book_dir = '%s/%s/all_transcriptions/1000/' % (output_dir, book_name)
    for filename in os.listdir(book_dir):
      # pl_blac_012_00019-1000_iter-3_transcription_normalized.txt
      suffix = "-1000_iter-3_transcription.txt"
      if filename.endswith(suffix):
        basename = filename[:-len(suffix)]
        output_filename = "%s/%s/%s.html" % (website_dir, book_name, basename)
        print 'Writing %s' % (output_filename)
        with codecs.open(output_filename, 'w', encoding='utf8') as fout:
          fout.write('<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">\n')
          fout.write('<head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/></head>\n')
          fout.write('<body>\n')
          fout.write('<table><tr><td>\n')
          with codecs.open("%s/%s" % (book_dir, filename), 'r', encoding='utf8') as fin:
            for line in fin:
              fout.write("%s<br/>\n" % (line.strip()))
          fout.write('</td><td>\n')
          fout.write('<img src="http://primeroslibros.org/primeros_media/%s/%s/%s-%s.jpg">\n' % (book_name, website_image_size, basename, website_image_size))
          fout.write('</td></tr></table>\n')
          fout.write('</body>\n')
          fout.write('</html>\n')

