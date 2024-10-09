import unicodedata

from youseedee import ucd_data

string = "◌ٰ◌ٓ◌ٔ◌ٕ◌ً◌ٌ◌ٍ◌َ◌ُ◌ِ◌ّ◌ْ"

arr = []

def get_joining_type(char: str) -> str:
    return ucd_data(ord(char)).get("Joining_Type", "U")


def check(string):
    for i in string:
        if unicodedata.category(i) == "Mn":
            arr.append([i, unicodedata.name(i)])

    return True


check(string)

MANUALLY_DEFINED_MARKS = {
    'ar_Arab': [
        ["\u064E\u0651", 'FATHA+SHADDA'],
        ["\u064B\u0651", 'FATHATAN+SHADDA'],
        ["\u0650\u0651", 'KASRA+SHADDA'],
        ["\u064D\u0651", 'KASRATAN+SHADDA'],
        ["\u064F\u0651", 'DAMMA+SHADDA'],
        ["\u064C\u0651", 'DAMMATAN+SHADDA'],
    ]
}
arr.extend(MANUALLY_DEFINED_MARKS['ar_Arab'])

joining_type = get_joining_type("آ")
print(joining_type)

print(arr)
