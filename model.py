from py2neo import Graph, Node, Relationship, cypher, authenticate
import os
import uuid


authenticate("localhost:7474", "neo4j", "achyut")
graph = Graph("http://localhost:7474/db/data/")


class User:
    def __init__(self, uname):
        self.uname = uname

    def find(self):
        data = graph.find_one('User', 'uname', self.uname)
        return data

    def verify_password(self, password):
        user = self.find()
        if user:
            if user['password'] == password:
                return True
            else:
                False
        else:
            return False

    def register(self, fname, lname, dob, email, contact, pin, city, address, passw):
        if not self.find():
            user = Node("User", fname=fname, lname=lname, uname=self.uname,
                            dob=dob, email=email, password=passw, contact=contact,
                            pin=pin, city=city, address=address)
            graph.create(user)
            return True
        else:
            return False

    def dlte(self):
        user = self.find()
        graph.delete(user)

    def change_pass(self, username, password):
        user = self.find()
        graph.delete(user)
        if User(username).register(user['fname'], user['lname'], user['dob'], user['email'], user['contact'], user['pin'], user['city'], user['address'], password):
            return

