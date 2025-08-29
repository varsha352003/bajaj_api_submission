def alternating_caps(s):
    result = ""
    upper = True
    for ch in s:
        if ch.isalpha():
            result += ch.upper() if upper else ch.lower()
            upper = not upper
    return result


def process_data(array, user):
   
    even_numbers = [x for x in array if x.isdigit() and int(x) % 2 == 0]
    odd_numbers = [x for x in array if x.isdigit() and int(x) % 2 != 0]
    alphabets = [x.upper() for x in array if x.isalpha()]
    special_chars = [x for x in array if not x.isalnum()]
    sum_numbers = str(sum(int(x) for x in array if x.isdigit()))

    concat_alpha_reverse_alt_caps = alternating_caps("".join([x for x in array if x.isalpha()][::-1]))

  
    return {
        "is_success": True,
        "user_id": f"{user['full_name']}_{user['dob']}",
        "email": user["email"],
        "roll_number": user["roll_number"],
        "odd_numbers": odd_numbers,
        "even_numbers": even_numbers,
        "alphabets": alphabets,
        "special_characters": special_chars,
        "sum": sum_numbers,
        "concat_string": concat_alpha_reverse_alt_caps
    }
