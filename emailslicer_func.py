def main():
    email = input("What is your email address? ")
    isValidEmail(email)

def isValidEmail(address):
    if "@" not in address or address.count("@") > 2:
        return errorMessage(1)
    return isValidChar(address)

def isValidChar(address):

    char_list = ["!", "#", "$", "%", "^", "&", "*",
                 "(", ")", "=", "+", "-", "`", "~",
                 ";", "'", '"', "?", "<", ">", ",",
                 "{", "}", "\\", "|", "[", "]"]

    if any(char in address for char in char_list) == True:
        return errorMessage(2)
    return isValidLength(address)

def isValidLength(address):
    username, domain = address.split("@")
    if len(username) > 64 or len(domain) > 255:
        return errorMessage(3)

    if len(username) + len(domain) > 320:
        return errorMessage(4)
    return isValidDomain(username, domain)

def isValidDomain(username, domain):
    
    splitDomain = domain.split(".")
    
    if domain.count(".") > 2 or domain.count(".") < 1 or "".join(splitDomain).isalpha() == False:
        return errorMessage(5)

    if "".join(splitDomain).islower() == False:
        return errorMessage(6)

    for char in range(len(splitDomain)):
        if len(splitDomain[char]) == 0:
            return errorMessage(7)
    
    return print(f"Your username is {username} and domain name is {domain}.")

def errorMessage(value):
    match value:

        case 1:
            print("Invalid email address. Please try again.")
        case 2:
            print("Cannot use special characters. Valid characters are A-Z, a-z, and 0-9.")
        case 3:
            print("""Username or domain name exceeded character limit.\nUsername (max) = 64 characters, 
            Domain (max) = 255 characters.\n Please try again.""")
        case 4:
            print("Email address is too long. Max character limit is 320.")
        case 5:
            print("Domain is invalid. Please try again.")
        case 6:
            print("Domain cannot contain uppercase letters. Please try again.")
        case 7:
            print("Invalid domain, please try again.")
            
    return main()

main()

