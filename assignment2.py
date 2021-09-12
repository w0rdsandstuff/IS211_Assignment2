import argparse
import urllib.request
import logging
import datetime

def downloadData(url):
    """Downloads the data"""
    request = urllib2.Request(url)
    urldata = urllib2.urlopen(request)
    return urldata.read()

def processData(file_content):
    csv_reader = csv.reader(csvdata)
    personData = {}
    line_count = 0
    date_format = '%d/%m/%Y'
    csv_data = []
    for csv_data in csv_reader:
        id = csv_data[0]
        username = csv_data[1]
        birthday = csv_data[2]
        if id != 'id':
            id = int(id)
            # csv_data[0] = int(csv_data[0])
            line_count += 1
            try:
                birthday = datetime.datetime.strftime(csv_data[2], date_format)
            except Exception as e:
                logging.error('Error processing line # %s for id # %s' % (line_count, id))
            finally:
                personData[id] = {'name': username, 'birthday': birthday}
            return personData


def displayPerson(id, personData):
    try:
        print 'Person # %s is %s with a birthday of %s' % (id, personData[id][name], personData[id][dob])
    except Exception, e:
        logging.warning('No user found with that id')

def main(url):
    """

    :return:
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--url', help='Type the URL of csv file', action="store", dest="url", type=str)
    args = parser.parse_args()

    csvdata1 = processData(args.url)

    if args.url:
        csvdata1 = downloadData(url)
        personData = processData(csvdata1)

    while True:
        try:
            user_input = int(raw_input('Please enter and ID # . Enter 0 or a negative $ to exit:'))
        except ValueError:
            logging.info('User typed wrong id')
            print 'Invalid Input. Please try agaiin'
            continue
        if user_input > 0:
            displayPerson(user_input, personData)
        else:
            print 'Thank you'
            sys.exit()

    print(f"Running main with URL = {url}...")
    
if __name__ == "__main__":
    main()


if __name__ == "__main__":
    """Main entry point"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", help="URL to the datafile", type=str, required=True)
    args = parser.parse_args()
    main(args.url)
