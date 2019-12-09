import urllib.request
import re as r
file_out = open('output.txt','w')
file_out.close()

with open('input.txt') as inp_file:
    for line in inp_file.readlines():
        url = line
        f = urllib.request.urlopen(url)
        s = f.read()
        text = str(s)
        part_name = text.find('player-name')
        name = text[text.find('>',part_name)+1:text.find('&',part_name)]
        i = text.find('TOTAL')
        total = text[text.find('>',i)+1:text.find('</tr>',i)]
        d = total.find('</td>')
        m = total.find('<td>')
        string = ''
        c = 1
        all = total.rfind('<td>')
        all_2 = total.rfind('</td>')
        print(total[all+4:all_2])

        print(all)
        new = total[m+4:d]
        print(new)
        print(name)
        print(total)



