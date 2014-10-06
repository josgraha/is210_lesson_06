#!usr/bin/env python
# -*- coding: utf-8 -*-
""" W6 Task 04 """

import data

SALT = 'monosodium-glutamate'


def test_passwords(user_accounts=[]):
    ret = []
    for user_account in user_accounts:
        fields = user_account.split(':')
        cracked = crack_it(fields[1], SALT)
        if cracked:
            ret.append((cracked, fields[4]))
            #ret.append({acct, cracked})
    return ret


def crack_it(passwd=None, salt=SALT):
    '''
    Returns the matching word from the word list for the given passwd, if exists.
    :param passwd:
    :param salt:
    :return word or None:
    '''
    print 'crack_it: passwd: {}, salt: {}'.format(passwd, salt)
    if passwd is None:
        return None
    for word in data.WORDS:
        hashed_passwd = data.crypt(word, salt)
        if passwd == hashed_passwd:
            return word
    return None


def report():
    line_items = ''
    output = """
    Cracked passwords
    -------------------------------
      {}
    """
    cracked_passwords = test_passwords(data.PASSWD)
    for acct_pass_pair in cracked_passwords:
        # print acct_pass_pair
        acct, passwd = acct_pass_pair
        line_item = '\t{}\t\t  {}'
        str = line_item.format(acct, passwd)
        str += '\n'
        line_items += str
    print output.format(line_items)