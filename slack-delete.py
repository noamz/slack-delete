import argparse, slack

def _main(token, cname, just_list):
    client = slack.WebClient(token = token)

    response = client.conversations_list()
    if not response['ok']:
        print('Error loading channels: ' + response['error'])
        return(1)

    chans = [c for c in response['channels'] if c['name'] == cname]
    if len(chans) < 1:
        print('No channel named ' + cname + ' in workspace')
        return(1)
    
    cid = chans[0]['id']

    print('Listing messages in #' + cname + ':')
    hist = client.channels_history(channel=cid)
    msgs = hist['messages']
    msgs.reverse()
    for m in msgs:
        is_pinned = '[pinned]' if 'pinned_to' in m else ''
        print(m['ts'] + is_pinned + ' ' + m['text'])

    if just_list:
        return(0)
    
    print('Deleting unpinned messages in #' + cname + ':')
    delete_all = False
    for m in msgs:
        if 'pinned_to' in m:
            continue
        print(m['ts'], m['text'])
        while not delete_all:
            q = input('Delete ' + m['ts'] + '? ([n]o, [y]es, [a]ll delete) ')
            if len(q) > 0 and q[0] in ['n', 'y', 'a']:
                break
            print('Please enter n, y, or a')
        if q[0] == 'a':
            delete_all = True
        delete = delete_all or q[0] == 'y'

        if delete:
            print('Deleting ' + m['ts'] + '...')
            response = client.chat_delete(channel=cid, ts=m['ts'])
            if not response['ok']:
                print('Error: ' + response['error'])

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', required=True,
                        help='slack channel')
    parser.add_argument('-t', required=True,
                        help='slack token')
    parser.add_argument('-l', dest='just_list', action='store_const',
                        const=True, default=False,
                        help='just list messages (do not delete)')
    args = parser.parse_args()
    _main(args.t, args.c, args.just_list)
