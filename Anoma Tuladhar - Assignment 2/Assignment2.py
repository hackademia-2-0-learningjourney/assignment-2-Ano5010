import json

def assignment(saver):
    with open('data.json','w') as f:
        json.dump(saver,f)

def load():
    try:
        with open('data.json','r') as f:
            return json.load(f)
    except FileNotFoundError:
        return{}
    
print('Enter 1 to Sign Up or, Enter 2 to Sign In: ')
entry=int(input('Enter: '))
if entry==1:
    print('Chosen: Sign up')
    user=input('Create username: ')
    passw=input('Create password: ')
    phone=int(input('Enter your mobile number: '))
    saver=load()
    saver[user]={'password':passw,'number':phone}
    assignment(saver)
elif entry==2:
    print('Chosen: Sign In')
    user=input('Enter your username: ')
    passw=input('Enter your password: ')
    saver=load()
    if(user in saver and saver[user]['password']==passw):
        print('Welcome to your device')
        print('Your mobile number is: ', saver[user]['number'])
    else:
        print('Invalid credentials.')
else:
    print('Error. Enter 1 for Sign Up or, Enter 2 for Sign In')


