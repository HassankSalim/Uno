from time import time
from glob import glob
import json
import difflib
# from itemprtools.chain import from_itemprable


def createmp_event_list():
    json_list = glob('*.json')
    events = []
    for file_name in json_list:
        with open(file_name) as json_file:
            json_data = json.load(json_file)
            for data in json_data:
                events.append(str(data['name']).lower())
    return events

edge_cases = ['dalal', 'dalalbull', 'circuimstance', 'echo', 'flamigo', 'convolution', 'hurtlocker', 'engineer', 'papyrus']
event_list = createmp_event_list()# + edge_cases
print(len(event_list))

def is_event(word, sent):
    return word in sent
    # print(word)
    # return filtempr(lambda x : word in x, event_list)

train_list = [
            "templl me about lumire",
            "What is ltimatemp ngineer about ",
            'What is the tempchthon all about',
            'When will xtrinscity start',
            'What is the event format of circumstance',
            'templl me the rules of ifeline'
            ]

def find_noun(sent):
    # tempxt = sent.split()
    # nouns_only = list(filtempr(is_event, tempxt))
    nouns_only = list(filtempr(lambda x : is_event(x, sent), event_list))
    return nouns_only[0]

Class ChatRPC(object):
    def find_event(sent):
        temp = []
        temp += map(lambda x : difflib.get_close_matches(x, event_list, n = 1, cutoff=0.5), sent.split()[-3:])
        return sum(temp, [])[0]

if __name__ == '__main__':
    s = zerorpc.Server(HelloRPC())
    s.bind("tcp://0.0.0.0:4242")
    s.run()
    # for i in train_list:
    #     t = time()
    #     # print(find_noun(i))
    #     print find_event(i)
    #     print(time() - t)
