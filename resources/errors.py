class InternalServerError(Exception):
    pass

class SchemaValidationError(Exception):
    pass

class WrongParameterError(Exception):
    pass

# Error Types used in ~/routes/<files>
errors = {
    "InternalServerError": {
        "message": "Something went wrong",
        "status": 500
    },
     "SchemaValidationError": {
         "message": "Request is missing required fields",
         "status": 400
     },
     "WrongParameterError": {
         "message": "Parameter has incorrect value",
         "status": 400
     }
}