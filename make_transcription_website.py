import codecs
import os
import csv

##output_dir = "/Users/halperta/Downloads/neh_transcribedBooks_12-18-17"
# output_dir = "/Users/halperta/Downloads/testhtml/"
# github_dir = "/Users/halperta/GitHub/firstbooks/"
# website = "http://www.halperta.com/firstbooks"
# transcriptions_dir = "%s/finalTranscriptions" % (github_dir)
# website_image_size = "800"  # 400, 800, 1000
# csvPath = "/Users/halperta/GitHub/ocr-auxiliary-data/pl-works-11-10-16.csv"

output_dir = "/Users/hra288/Github/neh/TranscribedBooks"
github_dir = "/Users/hra288/Github/neh/firstbooks/"
website = "http://www.halperta.com/firstbooks"
transcriptions_dir = "%s/finalTranscriptions" % (github_dir)
website_image_size = "800"  # 400, 800, 1000
csvPath = "/Users/hra288/Github/neh/pl-works_newdata_170314.csv"


# output_dir = "/Users/hra288/Github/neh/testTranscribedBooks"
# github_dir = "/Users/hra288/Github/neh/testfirstbooks/"
# website = "http://www.halperta.com/testfirstbooks"
# transcriptions_dir = "%s/finalTranscriptions" % (github_dir)
# website_image_size = "800"  # 400, 800, 1000
# csvPath = "/Users/hra288/Github/neh/pl-works_newdata_170314.csv"


all_pages = dict()  # all_pages[book_name] = page_names

metadata_dict = dict()
with open(csvPath) as csvfile:
  reader = csv.DictReader(csvfile, delimiter='|')
  for row in reader:
    metadata_dict[row['wks_book_id']] = row 

with codecs.open("%s/index.html" % (github_dir), 'w', encoding='utf8') as index_fout:
  # fout.write('<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">\n')
  # fout.write('<head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/></head>\n')
  # fout.write('<body>\n')
  index_fout.write('<font size=+2>Reading the First Books</font>')
  index_fout.write('<br/>\n')
  index_fout.write('<br/>\n')
  index_fout.write("""
    This website is a temporary staging site for books transcribed for the 
    <a href="http://sites.utexas.edu/firstbooks/">Reading the First Books</a> project. The project used the <a href="http://www.github.com/tberg12/ocular">Ocular Optical
    Character Recognition</a> system to transcribe fifty books from the <a href="http://primeroslibros.org/">Primeros Libros</a> collection. 
    Follow the links to see page transcriptions, or to download the transcription for an entire book. The transcriptions have not been reviewed or undergone post-processing of any kind.<br/><br/>\n""")
  index_fout.write("""Download the transcribed corpus. [<a href='allTranscriptions.zip'>.zip</a>] <br> 
    View sample transcriptions from the <a href ="sympsium/index.html">Reading the First Books symposium.</a>
    <br/><br/>\n""")
  index_fout.write("""
   For more information about the project or the data, contact <a href="http://www.halperta.com">Hannah Alpert-Abrams</a> (halperta@gmail.com).
    <br/><br/>\n""")
  index_fout.write('<div>')
  index_fout.write("""
    <script>
      (function() {
        var cx = '012497753802185401351:krmz1a5vprq';
        var gcse = document.createElement('script');
        gcse.type = 'text/javascript';
        gcse.async = true;
        gcse.src = 'https://cse.google.com/cse.js?cx=' + cx;
        var s = document.getElementsByTagName('script')[0];
        s.parentNode.insertBefore(gcse, s);
      })();
    </script>
    <gcse:search></gcse:search> 
  """)
  # index_fout.write('<\div>')
  index_fout.write('<p style="margin-left: 40px">')

  if not os.path.exists("%s" % (transcriptions_dir)):
    os.makedirs("%s" % (transcriptions_dir))
  for book_name in os.listdir(output_dir):
    if book_name[0] != '.':  # skip hidden files
      if book_name in metadata_dict:
        bookTitle = metadata_dict[book_name]['wks_title'].decode('utf-8') #haaupdate
        bookPrinter = metadata_dict[book_name]['wks_printer'].decode('utf-8') #haaupdate
        bookDate = metadata_dict[book_name]['wks_pub_date'].decode('utf-8') #haaupdate
      else:
        bookTitle = book_name
        bookPrinter = "printer unknown"
        bookDate = "date unknown"
      if book_name not in all_pages:
        all_pages[book_name] = []
      if not os.path.exists("%s/%s" % (transcriptions_dir, book_name)):
        os.makedirs("%s/%s" % (transcriptions_dir, book_name))
      book_dir = '%s/%s/' % (output_dir, book_name)
      for filename in os.listdir(book_dir):
        # pl_blac_012_00019-1000_iter-3_transcription_normalized.txt
        suffix = "-1000_transcription.txt" #haaupdate TODO: fix to match actual outputs.
        if filename.endswith(suffix):
          page_name = filename[:-len(suffix)]
          page_number = page_name[-5:]
          all_pages[book_name].append(page_name)
      for (i, page_name) in enumerate(all_pages[book_name]):
        print('Writing %s/%s/%s.html' % (transcriptions_dir, book_name, page_name))
        with codecs.open("%s/%s/%s.html" % (transcriptions_dir, book_name, page_name), 'w', encoding='utf8') as fout:
          if i > 0:
            fout.write('<a href="%s.html">Prev</a>&nbsp;\n' % (all_pages[book_name][i-1]))
          fout.write('<a href="index.html">Up</a>&nbsp;\n' % ())
          if i < len(all_pages[book_name])-1:
            fout.write('<a href="%s.html">Next</a>\n' % (all_pages[book_name][i+1]))
          fout.write('<br/>\n')
          fout.write('<br/>\n')
          fout.write('<a href="http://primeroslibros.org/page_view.php?id=%s&lang=en&page=1"><font size="+1">%s</font></a>' % (book_name, bookTitle)) #haaupdate
          fout.write('<br/>\n')
          fout.write('%s, %s.' % (bookPrinter,bookDate))
          fout.write('<br/>\n')
          fout.write('page: %s' % (page_number))
          fout.write('<br/>\n')
          fout.write('<br/>\n')
          fout.write('<br/>\n')
          fout.write('<br/>\n')

          fout.write('<table><tr><td>\n')
          with codecs.open("%s/%s%s" % (book_dir, page_name, suffix), 'r', encoding='utf8') as fin:
            for line in fin:
              fout.write("%s<br/>\n" % (line.strip()))
          fout.write('</td><td>\n')
          fout.write('<img src="http://primeroslibros.org/primeros_media/%s/%s/%s-%s.jpg">\n' % (book_name, website_image_size, page_name, website_image_size))
          fout.write('</td></tr></table>\n')
          fout.write('</html>\n')
      with codecs.open("%s/%s/index.html" % (transcriptions_dir, book_name), 'w', encoding='utf8') as fout:
        fout.write('<a href="../../index.html">Home</a><br/><br/>\n' % ())
        fout.write('<br/>\n')
        fout.write('<a href="http://primeroslibros.org/page_view.php?id=%s&lang=en&page=1"><font size="+1">%s</font></a>' % (book_name, bookTitle)) #haaupdate
        fout.write('<br/>\n')
        fout.write('%s, %s.' % (bookPrinter,bookDate))
        fout.write('<br/>\n')
        fout.write('Each link points to a page in the book and its accompanying transcriptions.')
        fout.write('<br/>\n')
        fout.write('<br/>\n')
        for page_name in all_pages[book_name]:
          fout.write('<a href="%s.html">%s</a><br/>\n' % (page_name, page_name))
      index_fout.write('<a href="finalTranscriptions/%(book_name)s/index.html">%(bookTitle)s (%(bookPrinter)s, %(bookDate)s)</a><br/>\n' % {"book_name": book_name, "bookTitle": bookTitle, "bookPrinter": bookPrinter, "bookDate": bookDate})
      index_fout.write('</body>\n')

