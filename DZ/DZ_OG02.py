print ('\n\nTest 5-10')
current_users=['sergei','vlad','EgoR','toNya','admIn','Sveta','AlEx']
current_users_title=[Tit.lower() for Tit in current_users]
new_users=['roman','Anton','Sergei','TImur','NAtasha','Alex']
for new_user in new_users:
	if new_user.lower() in current_users_title:
		print('The name '+new_user+' was used earlier')
	else:
		print('Name '+new_user.lower().title()+' is free')