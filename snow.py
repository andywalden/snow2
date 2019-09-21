import argparse
import json
import requests
import sys

def post(url, headers, data):
    return requests.post(url, 
                          headers=headers, 
                          data=json.dumps(data))

def main():                      
    usage = '''\
    usage: snow 
            Required to create a ticket:
                -t "title" 
                -d "description" 
                -n "device_name" 
                -c "comments"
                
            Required to update a ticket:
                -k ticket_number 
                -c "comments"
            
            Optional:
                -s customer
                -a assignmentGroup
                -b businessService
                -u urgency (1-3)
                -i impact (1-3)
                -g category
                -b subcategory
            
                -h Show this help
            
            Quotes only required when there are spaces.
    '''
    if len(sys.argv) < 2:
        print(usage)
        sys.exit()

    parser = argparse.ArgumentParser(prog='snow',
                                     add_help=False,
                                     usage=argparse.SUPPRESS,                                 
                                     formatter_class=argparse.RawDescriptionHelpFormatter,
                                     description=usage)
    parser.add_argument('-t', '--title', dest='shortDescription', help=argparse.SUPPRESS)
    parser.add_argument('-d', '--description', dest='description', help=argparse.SUPPRESS)
    parser.add_argument('-n', '--name', dest='deviceName', help=argparse.SUPPRESS)
    parser.add_argument('-c', '--comments', dest='comments', help=argparse.SUPPRESS)
    parser.add_argument('-k', '--ticket', dest='correlationID', help=argparse.SUPPRESS)
    parser.add_argument('-s', '--customer', dest='customer', help=argparse.SUPPRESS)
    parser.add_argument('-g', '--group', dest='group', help=argparse.SUPPRESS)
    parser.add_argument('-b', '--business', dest='business', help=argparse.SUPPRESS)
    parser.add_argument('-u', '--urgency', dest='urgency', help=argparse.SUPPRESS)
    parser.add_argument('-i', '--impact', dest='impact', help=argparse.SUPPRESS)
    parser.add_argument('-e', '--category', dest='category', help=argparse.SUPPRESS)
    parser.add_argument('-r', '--subctegory', dest='subcategory', help=argparse.SUPPRESS)
    parser.add_argument('-h', '--help', action='help', help=argparse.SUPPRESS)
    pargs = parser.parse_args()
    
    print(pargs)
    
    #if pargs.help:
    #    print(usage)
    #    sys.exit()

    params = {k: v for k,v in vars(pargs).items() if v}
    
    headers = {'Accept:application/json',
                 'Content-Type:application/json'}
        
    url = 'https://attccmsdev.service-now.com/api/x_att3_mcafee_siem/v1/siem_integration'

    r = post(url, headers, params)
    
    print(r)
        

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        logging.warning("Control-C Pressed, stopping...")
        sys.exit()
