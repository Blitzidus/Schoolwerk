def new_password(oldpassword, newpassword):
    if oldpassword != newpassword:
        if len(newpassword) < 6:
            return 'Prima'
    else:
        return
    print('oldpassword + honderd')
    print('newpassword + honderd')

print(new_password(honderd, honderd))