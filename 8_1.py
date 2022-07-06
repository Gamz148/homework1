import re

mail_template = "([a-zA-Z0-9\_\.'+-]+)@([a-zA-Z0-9\.-]+\.{1}[a-zA-Z0-9\.-]+)"

mail_template = "([\w\_\.'+-]+)@([\w\.-]+\.{1}[\w\.-]+)"

def email_parse(email, regex_template=mail_template):
    rez = re.fullmatch(regex_template, email)
    if rez is None:
        raise ValueError(f"wrong email: {email}")
    rez = rez.groups()
    return {'username': rez[0], 'domain': rez[1]}


lst_data = [
"user0_name@domenname.ru",
"user1'name@domenname.ru",
"user2.name@domenname.ru",
"user3+name@domenname.ru",
"user4-name@domenname.ru",
"user5=name@domenname.ru",
"user6*name@domenname.ru",
"user7&name@domenname.ru",
"user8^name@domenname.ru",
"user9%name@domenname.ru",
"user10$name@domenname.ru",
"user11#name@domenname.ru",
"user12_name@domenna.me.ru",
"user13_name@domennameru",
"user14_name@domen-name.ru",
"user16_name@domen+name.ru",
"user17_name@domen=name.ru",
"user18_name@domen)name.ru",
"user19_name@domen*name.ru",
"user20_name@domen/name.ru",
"user21_name@domen&name.ru",
"user22_name@domen%name.ru",
"Юзер23_name@domenname.ru",
"user24_name@доменname.ru",
"user25_name@domen,name.ru",
"user26_name@domen<name.ru",
"user27>name@domenname.ru",
]

for email in lst_data:
    print(f"{email:34s}", end = "")
    try:
        print(f"{email_parse(email)}")
    except ValueError:
        print(f"Error")