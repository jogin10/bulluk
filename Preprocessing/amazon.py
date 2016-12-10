# -*- encoding: utf-8 -*-

import codecs
import urllib2 # import der Funktion urlopen



def remove_entities(text):
    text = text.replace('<br />','')
    text = text.replace('&#34;','"')
    text = text.replace('&eacute;','e')
    text = text.replace('&egrave;','E')
    text = text.replace('&#60;','<')
    text = text.replace('&szlig;','ß')
    text = text.replace('&uuml;','ü')
    text = text.replace('&Auml;','Ä')
    text = text.replace('&quot;','"')
    text = text.replace('&nbsp;',' ')
    text = text.replace('&#62;','>')
    text = text.replace('&auml;','ä')
    text = text.replace('&ouml;','ö')
    text = text.replace('&Uuml;','Ü')
    text = text.replace('&Ouml;','Ö')
    text = text.replace('&gt;','<')
    text = text.replace('&agrave;','E')
    text = text.replace('&amp;','&')
    text = text.replace('&lt;','<')
    text = text.replace('&aacute;','á')
    text = text.replace('&iacute;','í')
    text = text.replace('&uacute;','ú')
    
    return text


def postprocess_text(filename):
    f = codecs.open(filename)
    content = f.read()
    f.close()

    import re
    for item in set(re.findall("&[a-zA-Z0-9#]+;", content)):
        print '%s: %s' % (filename, item)

    print '%s was successfully created.' % filename


def get_amazon():

    review_URLs = ['https://www.amazon.de/product-reviews/B00TX5O8WE/ref=cm_cr_arp_d_viewopt_srt?ie=UTF8&reviewerType=all_reviews&showViewpoints=1&sortBy=recent&pageNumber=',\
                    'https://www.amazon.de/product-reviews/B00TX5PG3E/ref=cm_cr_dp_see_all_btm?ie=UTF8&reviewerType=all_reviews&showViewpoints=1&sortBy=recent&pageNumber=',\
                    'https://www.amazon.de/product-reviews/B01BTZFM0W/ref=cm_cr_dp_see_all_btm?ie=UTF8&reviewerType=all_reviews&showViewpoints=1&sortBy=recent&pageNumber=',\
                    'https://www.amazon.de/product-reviews/B01BTZFSTC/ref=cm_cr_dp_see_all_btm?ie=UTF8&reviewerType=all_reviews&showViewpoints=1&sortBy=recent&pageNumber=' \
                   ]
    

    delim = 'µ'
    for review_URL in review_URLs:
        a = 0
        filename = review_URL.split('product-reviews/')[1].split('/')[0]+'.csv'
        f = codecs.open(filename, 'w', "utf-8-sig")
        f.write('id%sstars%stopic%susername%sdate%scontent\n' % (delim, delim, delim, delim, delim))
        
        for i in range(1,10000):

            # URL Variabledefinition
            review_URLx = review_URL+str(i-a)
            dividing_tag = '<i data-hook="review-star-rating"'

            div_tag_text_start = '<span data-hook="review-body" class="a-size-base review-text">'
            div_tag_text_end = '</span>'
			
	    div_tag_stars_start = '<span class="a-icon-alt">'
	    div_tag_stars_end = '</span>'

	    div_tag_topic_1 = '<a data-hook="review-title"'
	    div_tag_topic_2 = '</a>'
	    div_tag_topic_3 = '>'

	    div_tag_username_1 = '<a data-hook="review-author"'
	    div_tag_username_2 = '</a>'
	    div_tag_username_3 = '>'

	    div_tag_date_start = 'review-date">'
	    div_tag_date_end = '</span>'


            try:
                # Abzug des HTML-Quellcodes von der oben definirten URL
                source_txt = urllib2.urlopen(review_URLx).read()
            except:
                print "%s: %s wird nochmal abgezogen" % (filename, str(i-a))
                a = a + 1
                continue

            # Endbedingung
            if not source_txt.count(dividing_tag): break

            # Aufteilung des Quellcodes
            reviews = source_txt.split(dividing_tag)[1:]


	    x = 1
            for review in reviews:
		# get text
                review_text = (remove_entities(review.split(div_tag_text_start)[1].split(div_tag_text_end)[0])).decode('utf-8')
				
		# get stars
		stars = (remove_entities(review.split(div_tag_stars_start)[1].split(div_tag_stars_end)[0])).decode('utf-8')

                # get topic
		topic = (remove_entities(review.split(div_tag_topic_1)[1].split(div_tag_topic_2)[0].rpartition(div_tag_topic_3)[2])).decode('utf-8')

		# get username
		username = (remove_entities(review.split(div_tag_username_1)[1].split(div_tag_username_2)[0].rpartition(div_tag_username_3)[2])).decode('utf-8')

		# get date
		date = (remove_entities((review.split(div_tag_date_start)[1].split(div_tag_date_end)[0])).replace('am ','')).decode('utf-8')
				
                f.write('%s%s%s%s%s%s%s%s%s%s%s\n' % (str((i-a-1)*10+x), delim, stars, delim, topic, delim, username, delim, date, delim, review_text))
		x = x + 1

            print '%s: %s' % (filename, str(i-a))

        f.close()

        postprocess_text(filename)


def remove_entities_manually(filename):
    f = codecs.open(filename)
    a = f.read()
    f.close()
    out = remove_entities(a)
    g = codecs.open(filename.split('.')[0]+'_sauber.csv', "w", "utf-8-sig")
    g.write(out)
    g.close()



get_amazon()

#filename = 'B00TX5O8WE_sauber.txt'
#remove_entities_manually(filename)
