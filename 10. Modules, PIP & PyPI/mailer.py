from send_mail import SendMail

new_mail = SendMail(
	# List (or string if single recipient) of the email addresses of the recipients
	['perumandlasaikrishnateja@gmail.com', 'gopaganisunny97@gmail.com','giridher.sadineni@gmail.com'], 
	# Subject of the email
	'Welcome to skillverse ',
	# Body of the email
	'Skillverse Computer Computer education welcomes to the Python Demo Class today at 7 Pm', 
	# Email address of the sender
	# Leave this paramter out if using environment variable 'EMAIL_ADDRESS'
	'perumandlasaikrishnateja@gmail.com' 
)

new_mail.add_html_message('<h1>Hello, Students</h1>')



curl -X POST https://rest.messagebird.com/messages \\
        -H 'Authorization: AccessKey YOUR-API-KEY' \\
        -d "recipients=+31XXXXXXXXX" \\
        -d "originator=+31XXXXXXXXX" \\
        -d "body=Hi! This is your first message."

print(new_mail)

new_mail.send('9177701985')
