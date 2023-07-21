from bson import ObjectId
from database.client import sync_engine

def fetch_database_model(modelClass, obj_id:ObjectId):
    # SYNC Mongo engine is used because Pydantic validation in synchrone
    data = sync_engine.find_one(modelClass, modelClass.id == obj_id)   
    if not data:
        raise ValueError("No %s found with ObjectId(%s)"%(modelClass.__name__, obj_id))
    
    res = data.dict()
    res['id'] = str(res['id']) # convert ObjectId to str
    return res


class ModelObjectId(ObjectId):
    """
        This is a ODMantic / Pydantic custom field type
            ODMantic Doc : https://art049.github.io/odmantic/fields/#custom-field-types
            Pydantic Doc : https://docs.pydantic.dev/latest/usage/types/custom/#as-a-method-on-a-custom-type

        This Class in a parent Class. DO NOT USE IT DIRECTLY
    """

    _model = None # used for heritage to define DB Model to fetch

    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        # Security : do not use this Class direclty
        if cls._model == None:
            raise ValueError("No model provided")
        
        # Handle data coming from FastAPI request
        if isinstance(v, str):
            return ObjectId(v)
        
        # Handle data coming from MongoDB
        if isinstance(v, ObjectId):
            # SYNC engine for validation
            return fetch_database_model(cls._model, v)
        
        raise ValueError("%s data validation error"%(cls.__name__))

