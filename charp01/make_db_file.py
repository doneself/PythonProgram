dbfilename = 'people-file'
ENDDB = 'enddb.'
ENDREC = 'emdrec.'
RECSEP = '=>'

def storeDbase(db, dbfilename=dbfilename):
    dbfile = open(dbfilename, 'w')
