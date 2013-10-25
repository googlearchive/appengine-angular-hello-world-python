from google.appengine.ext import ndb

class Guest(ndb.Model):
  first = ndb.StringProperty()
  last = ndb.StringProperty()


def AllGuests():
  return Guest.query()


def UpdateGuest(id, first, last):
  guest = Guest(id=id, first=first, last=last)
  guest.put()
  return guest


def InsertGuest(first, last):
  guest = Guest(first=first, last=last)
  guest.put()
  return guest


def DeleteGuest(id):
  key = ndb.Key(Guest, id)
  key.delete()
