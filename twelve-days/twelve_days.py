def recite(start_verse, end_verse):
    start_index = start_verse-1
    answer = []
    
    numbers = "a two three four five six seven eight nine ten eleven twelve".split(' ')

    days = "first second third fourth fifth sixth seventh eighth ninth tenth eleventh twelfth".split(' ')

    gifts = ["Partridge in a Pear Tree",
             "Turtle Doves",
             "French Hens",
             "Calling Birds",
             "Gold Rings",
             "Geese-a-Laying",
             "Swans-a-Swimming",
             "Maids-a-Milking",
             "Ladies Dancing",
             "Lords-a-Leaping",
             "Pipers Piping",
             "Drummers Drumming"]
    
    for day in days[start_index:end_verse]:
        stanza = f"On the {day} day of Christmas my true love gave to me:"
        the_gifts = gifts[0:(days.index(day)+1)]
        the_gifts.reverse()
        for items in the_gifts:
            stanza += f" {numbers[gifts.index(items)]} {items}"
            if items is not the_gifts[(len(the_gifts)-1)]:
                stanza += ","
            if items == the_gifts[(len(the_gifts)-2)] and len(the_gifts) is not 1:
                stanza += ' and'
        stanza += '.'
        answer.append(stanza)
    return answer

if __name__=='__main__':
    print (recite(int(input()), int(input())))