
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint


class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        
        # example list of members
        self._members = [
        {
            "first_name": "John",
            "id": 0,
            "age": 33,
            "lucky_numbers": [7, 13, 12]
        },
        {
            "first_name": "Jane",
            "id": 1,
            "age": 35,
            "lucky_numbers": [10, 14, 3]
        },
        {
            "first_name": "Jimmy",
            "id": 2,
            "age": 5,
            "lucky_numbers": [1]
        }]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        # fill this method and update the return
        _id = ""
        if member["id"] == 0:
            _id = self._generateId()
        else:
            _id = member["id"]

        self._members.append({
            "id" : _id,
            "first_name": member["first_name"],
            "age": member["age"],
            "lucky_numbers": member["lucky_numbers"]
        })

    def delete_member(self, idd):
        # fill this method and update the return
        for i in self._members:
            if i["id"] == idd:
                cual_es_index = self._members.index(i)
                self._members.pop(cual_es_index)
                
        return {"done" : True}

    def get_member(self, id):
        # fill this method and update the return
        def id_filter(memb):
            return memb["id"] == id 

        member_id = list(filter(id_filter, self._members))
        
        return member_id

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
