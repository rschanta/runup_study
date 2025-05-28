def convert_to_number(value):
    try:
        # Convert float: will work for ints/floats, strings fail
        float_value = float(value)
        
        # Convert to inter if not '.' is found in the original input string
        if '.' in str(value).strip():
            return float_value
        # Case to return int: if no decimal point is provided
        else: 
            return int(float_value)
        
    # Case to return string: if conversion to float fails
    except ValueError:
        return value
    