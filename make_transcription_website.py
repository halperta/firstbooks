import codecs
import os

output_dir = "/Users/dhg/workspace/symposiumPrep/train_output_17-05-24"
website_dir = "/Users/dhg/workspace/halperta/firstbooks/transcriptions"
website_image_size = "800"  # 400, 800, 1000



all_pages = dict()  # all_pages[book_name] = page_names

with codecs.open("%s/index.html" % (website_dir), 'w', encoding='utf8') as index_fout:
  index_fout.write("""
    This website was designed to accompany the
    <a href="http://sites.utexas.edu/firstbooks/symposium">Reading the First Books Symposium</a>,
    held May 30, 2017, at the University of Texas at Austin. Each link represents a book in the 
    <a href="http://primeroslibros.org/">Primeros Libros</a> collection. Follow the links to see rough transcriptions
    of sample pages produced using the <a href="github.com/tberg12/ocular">Ocular Optical
    Character Recognition</a> system. The transcriptions have not been reviewed or undergone post-processing of
    any kind, and were produced for experimental purposes using very limited amounts of data.<br/><br/>\n""")
  index_fout.write("""
   For more information about the project or the data, contact <a href="http://www.halperta.com">Hannah Alpert-Abrams</a> (halperta@gmail.com).
    <br/><br/>\n""")
  index_fout.write('<br/><br/>\n')

  for book_name in os.listdir(output_dir):
    if book_name[0] != '.':  # skip hidden files
      if book_name not in all_pages:
        all_pages[book_name] = []
      if not os.path.exists("%s/%s" % (website_dir, book_name)):
        os.makedirs("%s/%s" % (website_dir, book_name))
      book_dir = '%s/%s/all_transcriptions/1000/' % (output_dir, book_name)
      for filename in os.listdir(book_dir):
        # pl_blac_012_00019-1000_iter-3_transcription_normalized.txt
        suffix = "-1000_iter-3_transcription.txt"
        if filename.endswith(suffix):
          page_name = filename[:-len(suffix)]
          all_pages[book_name].append(page_name)
      for (i, page_name) in enumerate(all_pages[book_name]):
        output_filename = "%s/%s/%s.html" % (website_dir, book_name, page_name)
        print 'Writing %s' % (output_filename)
        with codecs.open(output_filename, 'w', encoding='utf8') as fout:
          if i > 0:
            fout.write('<a href="%s/%s/%s.html">Prev</a>&nbsp;\n' % (website_dir, book_name, all_pages[book_name][i-1]))
          fout.write('<a href="%s/%s/index.html">Up</a>&nbsp;\n' % (website_dir, book_name))
          if i < len(all_pages[book_name])-1:
            fout.write('<a href="%s/%s/%s.html">Next</a>\n' % (website_dir, book_name, all_pages[book_name][i+1]))
          fout.write('<br/>\n')

          fout.write('<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">\n')
          fout.write('<head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/></head>\n')
          fout.write('<body>\n')
          fout.write('<table><tr><td>\n')
          with codecs.open("%s/%s%s" % (book_dir, page_name, suffix), 'r', encoding='utf8') as fin:
            for line in fin:
              fout.write("%s<br/>\n" % (line.strip()))
          fout.write('</td><td>\n')
          fout.write('<img src="http://primeroslibros.org/primeros_media/%s/%s/%s-%s.jpg">\n' % (book_name, website_image_size, page_name, website_image_size))
          fout.write('</td></tr></table>\n')
          fout.write('</body>\n')
          fout.write('</html>\n')
      with codecs.open("%s/%s/index.html" % (website_dir, book_name), 'w', encoding='utf8') as fout:
        fout.write('<a href="%s/index.html">Home</a><br/><br/>\n' % (website_dir))
        for page_name in all_pages[book_name]:
          fout.write('<a href="%s/%s/%s.html">%s</a><br/>\n' % (website_dir, book_name, page_name, page_name))
      index_fout.write('<a href="%s/%s/index.html">%s</a><br/>\n' % (website_dir, book_name, book_name))


