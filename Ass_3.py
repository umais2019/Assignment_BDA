import json
import functools
import datetime



My_Dict = {
"person_1":{ "name" : "Abdul Rafay", "age":22, "Interests":["football","cricket"], "amount_deposited":
[24000,26000] },
"person_2":{ "name" : "Nancy James", "age":23, "Interests":["baseball","cricket"], "amount_deposited":
[24000,27000] },
"person_3":{ "name" : "Selena Gomez", "age":26, "Interests":["baseball","table tennis"],
"amount_deposited":[24000,28000] }
}


a_g=[chr(x) for x in range(97,104)]
s_m_k = [chr(x) for x in [107,109,115]]

CURRENT_DATE = datetime.date.today()


def check(item):
    if item[1]["name"][0].lower() in a_g:
        item[1]["name"] = 'Mr. '+ item[1]["name"]
    else:
        item[1]["name"] = 'Ms. ' + item[1]["name"]
    a= item[1].pop('amount_deposited')
    item[1]["Year"] = str(int(CURRENT_DATE.year) - int(item[1]["age"]))
    item[1]["amount_deposited"] = int(functools.reduce(lambda x,y: x+y, a))
    return item


def write_file(Data):
    try:
        with open('names.json', 'w') as file:
            json.dump(Data, file, indent=4)
        return True
    except Exception as e:
        return False


def main():
    x = dict(list(map(check, list(filter(lambda record: record[1]["name"][0].lower() not in s_m_k, My_Dict.items())))))
    data = {
        'Current_Date': CURRENT_DATE.strftime('%d-%b-%Y'),
        'Data': x
    }

    if write_file(data):
        print('Successfully Written.')
    else:
        print('Check Again')


if __name__ == '__main__':
    main()

