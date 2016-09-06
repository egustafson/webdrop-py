# -*- coding: utf-8 -*_

from datetime import datetime


class MemoryNotes:

    def __init__(self, config):
        print("TRACE - MemoryNotes created.")
        self._notes = {}


    def close(self):
        print("TRACE - MemoryNotes.close()")
        pass


    def reset(self):
        print("TRACE - MemoryNotes.reset(), content erased")
        self._notes = {}


    def add(self, key, value):
        print("TRACE - MemoryNotes.add('{}', ...)".format(key))
        ts = datetime.now()
        self._notes[key] = (key, value, ts)


    def remove(self, key):
        print("TRACE - MemoryNotes.remove('{}')".format(key))
        if key in self._notes:
            del self._notes[key]


    def get(self, key):
        return self._notes.get(key, None)


    def list(self):
        return self._notes.values()


##
## Notes Factory
##
def factory(config, db):
    if db:
        ## TODO - implement DbNotes(db, config)
        pass
    return MemoryNotes(config)


## Local Variables:
## mode: python
## End:
