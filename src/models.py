# Dependencies
import uuid
import datetime

class BaseModel:
    '''
        this model is responsible for generating;
        - object ids
        - date created timestamps
    '''
    def __init__(self):
        self.object_id = str(uuid.uuid4())
        self.date_created = datetime.datetime.utcnow()

class DbModel(BaseModel):
    '''
        this is the database model
        holds the user table for now
    '''
    def __init__(self):
        '''
            constructor
            :param user_table:
        '''
        BaseModel.__init__(self)
        self.user_table = list()
    def add_obj(self, obj_data, table_name):
        '''
            this method adds an object to a corresponding table in the database
        '''
        if table_name == 'users':
            self.user_table.append(obj_data)
            return True
        return False
    def dup_check(self, email):
        '''
            this method checks for duplicates
        '''
        for user in self.user_table:
            if user.email == email:
                return True
        return False
class UserModel(BaseModel):
    '''
        this model holds properties of a user object
        - name
        - username
        - age
        - email
        - password
        - gender
        - bio
    '''
    def __init__(self, input_tuple):
        '''
            constructor
            :param name:
            :param username:
            :param age:
            :param email:
            :param password:
            :param gender:
            :param bio:
        '''
        self.name = input_tuple[0]
        self.username = input_tuple[1]
        self.age = input_tuple[2]
        self.email = input_tuple[3]
        self.password = input_tuple[4]
        self.gender = input_tuple[5]
        self.bio = str()
    def display_details(self):
        '''
            this method displays user details
        '''
        display_dict = dict()
        display_dict['name'] = self.name
        display_dict['username'] = self.username
        display_dict['age'] = self.age
        display_dict['email'] = self.email
        display_dict['gender'] = self.gender
        return display_dict

