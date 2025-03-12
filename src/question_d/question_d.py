#write functions here, don't add input('') statements here!
def get_person_category(age):
    if age < 0 or age > 125:
        return "Invalid number"
    elif age <= 1:
        return "infant"
    elif age < 13:
        return "child"
    elif age < 20:
        return "teenager"
    else:
        return "adult"

def test_get_person_category():
    assert get_person_category(1) == "infant", "Test failed for age 1"
    assert get_person_category(2) == "child", "Test failed for age 2"
    assert get_person_category(14) == "teenager", "Test failed for age 14"
    assert get_person_category(20) == "adult", "Test failed for age 20"
    
    print("All tests passed!")  

test_get_person_category()