import smtplib
import datetime
import sys
from configparser import ConfigParser
import argparse
import bs4
from pip._vendor import requests


def read_file():
    config_object = ConfigParser()
    try:
        open('mycontacts.config')
        config_object.read('mycontacts.config')
    except FileNotFoundError:
        print('Wrong folder selected!')
    login = str(config_object['Username']['username'])
    password = str(config_object['Password']['password'])
    receiver = str(config_object['Receiver']['receiver'])
    content = (login, password, receiver)
    return content


def get_arg():
    arg = argparse.ArgumentParser()
    arg.add_argument('--cat-facts', type=int)
    arg.add_argument('--teachers', type=str)
    arg.add_argument('--mail', type=str)
    return arg.parse_args()


def mail_sender(args):
    config_content = read_file()
    username = (config_content[0])[1:-1]
    password = (config_content[1])[1:-1]
    receiver = (config_content[2])[1:-1]
    sender = username
    smtpSrv = smtplib.SMTP('mail.pwr.wroc.pl', 587)
    time = datetime.datetime.now()
    smtpSrv.ehlo()
    smtpSrv.starttls()
    message_body = '\r\n'.join([
        'From:' + sender,
        'To:' + receiver,
        'Subject:Test',
        str(args.mail),
        str(time.strftime('%Y-%m-%d %H:%M:%S')),
        'Best Regards,\nAykhan Imanov.',
        ])
    smtpSrv.login(username, password)
    smtpSrv.sendmail(sender, receiver, message_body)
    smtpSrv.quit()


def fact_reader(args):
    url = 'https://cat-fact.herokuapp.com/facts'
    no = args.cat_facts
    page = requests.get(url).json()
    for fact in range(no):
        print(page['all'][fact]['text'])


def teacher_agenda(args):
    url = 'https://wiz.pwr.edu.pl/pracownicy?letter=' \
        + str(args.teachers)
    page = requests.get(url)
    content = bs4.BeautifulSoup(page.text, 'html.parser')
    a_class_title = content.select('a.title')
    p_email = content.select('p')
    print('The list of researches -' + args.teachers)
    if not a_class_title:
        print('No teacher found out')
    for (idx, name) in enumerate(a_class_title):
        print (name.get('title'))
        print(str(p_email[idx])[3:-4] + '\n')


if __name__ == '__main__':
    args = get_arg()

    if (sys.argv[1] == '--cat-facts'):
        fact_reader(args)
    elif (sys.argv[1] == '--teachers'):
        teacher_agenda(args)
    else: mail_sender(args)
