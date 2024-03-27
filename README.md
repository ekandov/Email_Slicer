# Email_Slicer
Email slicer python project that uses conditionals to evaluate whether the input is valid.

## Features

- Takes user's input.
- Runs validity checks such as:
    1. Whether input is a valid email address by looking for '@' symbol;
    2. If any disllowed special characters were used;
    3. If the input follows email length standards (total of 320 characters/64 for username/
       255 for domain name); and
    4. If domain has at least one dot or a max of two dots (e.g. schools.nyc.gov or gmail.com).
- Returns error message specific to determined case from above list and requests user's input again.
- Upon successful passing of test, returns message to user showing them their username and domain
  name.

## How to Use

- Must have python.
- Command to run program in terminal: "python emailslicer_func.py"
- Input example: "abctest@gmail.com"
