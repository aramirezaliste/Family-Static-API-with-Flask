
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint


class FamilyStructure:
    def __init__(self, last_name, first_name=str(),age=int(),lucky_numbers=list()):
        self.last_name = last_name
        self.first_name = first_name
        self.age = age
        self.lucky_numbers = lucky_numbers
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
        self._members.append({
            "id": self._generateId(),
            "first_name": self.first_name,
            "age": self.age,
            "lucky_numbers": self.lucky_numbers
        })

    def delete_member(self, id):
        # fill this method and update the return
        for i in self._members:
            if i["id"] == id:
                cual_es = i
                self._members.pop(id)
                #self._members.pop(cual_es)
                #index = self._members.index(self._members[i])
                #self._members.pop(index)
        return cual_es

    def get_member(self, id):
        # fill this method and update the return
        def id_filter(memb):
            return memb["id"] == id 

        member_id = list(filter(id_filter, self._members))
        
        return member_id

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
