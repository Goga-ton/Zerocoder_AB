print ('Test 5-8, 5-9')
personals = ['Sergei','vlad','Egor','tonya','admin','Sveta']
if personals:
    for personal in personals:
	    if personal == ('admin'):
		    print('\nHellow '+personal+', would you like to see a status report\n')
	    else:
		    print('Hellow '+personal.title()+', thank you for logging in agsain')
else:
	print('We need to find some user')