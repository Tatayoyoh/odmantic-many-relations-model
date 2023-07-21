from odmantic import Model, Reference
from odmantic import Field
from typing import List
from database.model_utils import ModelObjectId

class School(Model):
    name:str = Field()

class Skill(Model):
    description:str = Field()

class Student(Model):
    class SkillObjectId(ModelObjectId):
        _model = Skill

    fullname:str = Field()
    school:School = Reference()  # Single Reference relation
    skills:List[SkillObjectId]   # Many References relation. Here we use a specific type to retrieve data on the fly
    """
    skills:List[ObjectId]        # Many References relation (ODMantic original way)
    """
