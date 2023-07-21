from test_utils import request

if __name__ == '__main__':
    # Check FastAPI Backend is running 
    request("GET", "/")

    # Create some Student's Skills
    skill1 = { "description":"C++"}
    skill2 = { "description":"Python3"}
    skill3 = { "description":"MongoDB"}
    
    print('Create Skills')
    skill1 = request("POST", "/skill", skill1, print_response=True)
    skill2 = request("POST", "/skill", skill2, print_response=True)
    skill3 = request("POST", "/skill", skill3, print_response=True)
    
    print('List Skills')
    request("GET", "/skills", print_response=True)

    print('\nCreate Student with skills as references')
    student = {
        "fullname": "John Doe",
        "skills": [
            skill1['id'],
            skill2['id'],
            skill3['id']
        ],
        "school": {
            "name": "Santai School"
        }
    }
    request("POST", "/student", student, print_response=True)

    print('\nGet Students list (note that Skills are not only IDs but full Model data)')
    request("GET", "/students", print_response=True)
