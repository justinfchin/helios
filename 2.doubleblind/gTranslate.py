from googletrans import Translator
#from BingTranslator import Translator # need to 
#ISO Code for the Language. 

translator = Translator()

sInput = [	'I am so hungry.'
'Get me food',
'Let go of my bag',
'how do you do',
'i am the greatest good you are ever gonna get',
'You talking to me?',
'I will be back.',
'You did not heard nothing yet!',
'unhand me',
'A martini. Shaken, not stirred.',
'I have been looking at you for a long time',
'mary had a little lamb',
'I must dance with you today',
'come downstairs and eat dinner before it gets cold.',
'All of my senses are asking for more',
'We cannot do this in a rush',
'I want to see your hair dance',
'beautiful roses have thorns',
'i will send you back in time',
'you cannot stop me',
'You better run',
'It would be nice for you to tell the truth',
'This reminds me of my childhood',
'This is gonna be a piece of cake',
'Do not worry, leave it to me!'
			]

for i in sInput:
	print(translator.translate(i, src='en', dest='id').text)
	

	


