import argparse
import urllib.request
import logging
import datetime

def downloadData(url):
    """Downloads the data"""
    response = urllib.request.urlopen(url)
    data = response.read().decode('utf-8')
    return data

def processData(file_contents):
        empty_dict = {}
    header = True
    for line in file_contents.splitlines():
        if header:
            header = False
            continue
        parts = line.split(',')
        try:
            user_id = int(parts[0])
            name = parts[1]
            birthday = datetime.datetime.strptime(parts[2],'%d/%m/%Y') 
            empty_dict[int(parts[0])] = (name, birthday)
        except ValueError as e:
            print(e)
            print(f'Error on line {line}')
        

    return empty_dict

def displayPerson(user_id, empty_dict):
    name, birthday = empty_dict[user_id]
    print(f'{user_id},{name} born on {birthday}')


if __name__ == "__main__":
    """Main entry point"""
    url = 'https://s3.amazonaws.com/cuny-is211-spring2015/birthdays100.csv'
    data = downloadData(url)
    results = processData(data)
    while True:
        userid = int(input('Please enter an ID number:  ').strip())
        if userid <= 0:
            break
        displayPerson(userid, results
