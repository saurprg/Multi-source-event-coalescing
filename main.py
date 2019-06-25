"""
Multi-source event coalehscing:
Event data coming from logs such as server logs, windows or linux logs etc are very common
in an infrastructure management world. Often multiple events across logs refer to the same problem.
Matching these events is key to reducing noise. Given a set of event data,
find events that are similar based on inherent patterns in them.
*similar based on inherent patterns*

Events come from varying sources and have different structures of key:value pairs in a JSON format.
Given an incoming event, you are required to find other events that have occurred in the past
that this one is a close match to. In order to do this, you have to
generate a signature of events based on the key:value pairs within it.
Identifying these matches across 1000s of events is where the computational challenge is.

Tools:
You can code this in any language, we will give you a set of event data.
Deliverables:
A presentation of the approach to matching and how scale and performance is handled.
The code
A working demo
"""

# imports
import simplejson as json
from pprint import pprint
import sqlitedict as sql
from os import listdir
import time
from barplt import barplotter as plt
from HLL import HyperLogLog as hyp
from dictDB import dictDBHelper
from pprint import pprint

def Hllandcount(hl,cl,level,sign):
    hl[level-1].add(sign)
    cl[level-1]+=1

def is_unique_event(sign,dbhelper,index_of_events):
    if not over_half_million:
        return index_of_events.get(sign)==None
    else:
        db = dbhelper.getDB()
        return db.get(sign)==None

if __name__=='__main__':
        # giving path of json file and database
        database = "event_database.db"
        json_files_directory = 'jsonfiles'
        hllList = [hyp(5) for i in range(5)]
        cList = [0 for i in range(5)]
        t = time.time()
        #looking for json files
        filenames = listdir(json_files_directory)
        json_files = [filename for filename in filenames if filename.endswith('.json')]

        # initialising variables
        index_of_events = {}
        events_list = []
        count = 0
        no_of_similar_events = 0
        over_half_million = False
        half_million = 500000
        temp = 0
        dbhelper=dictDBHelper(database)

        #testing DB
        if over_half_million:
            db=dbhelper.getDB()
            dbhelper.shift_all_records_in_db(events_list)

        # loading json files
        for json_file in json_files:
            event_list = json.load(open(json_files_directory+'/'+json_file))
            # iterating each event of json_file
            for event in event_list:
                signature = dbhelper.get_sign(event)
                Hllandcount(hllList,cList,event["Level"],signature)
                if (not over_half_million) and (count+no_of_similar_events > half_million):
                    over_half_million = True
                    db=dbhelper.getDB()
                    dbhelper.shift_all_records_in_db(events_list)
                if is_unique_event(signature,dbhelper,index_of_events):
                    #event is unique hence create a new cluster for this type of event
                    print("Inserted",signature)
                    if not over_half_million:
                        new_list=[event,]
                        events_list.append(new_list)
                        index_of_events[signature] = count
                        count += 1
                    else:
                        db = dbhelper.getDB()
                        db[signature] = [event]
                else :
                    # Printing cluster of all previously occured similar event
                    print('\n==========\nEvent aleardy occurred\n')
                    if not over_half_million:
                        no_of_similar_events += 1
                        similar_events=events_list[index_of_events[signature]]
                        for j in similar_events:
                            pprint(j)
                        #adding current event to event_list having same signature
                        events_list[index_of_events[signature]].append(event)
                    else :
                        dbhelper.update_in_database(event,signature)

        if over_half_million:
            db = dbhelper.getDB()
            db.close()

        obj=['Level 1','Level 2','Level 3','Level 4','Level 5']
        performance0=[hllList[i].cardinality() for i in range(5)]
        bar=plt(obj,performance0,cList,'Bohot sahi','post','pre')
        bar.plot()
