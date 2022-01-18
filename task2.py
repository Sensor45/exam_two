# ------------------------------------------ Задание 2-------------------------------------------------------

text = 'Advertising companies say advertising is necessary and important. ' \
       'It informs people about new products. Advertising hoardings in the ' \
       'street make our environment colourful. And adverts on TV are often ' \
       'funny. Sometimes they are mini-dramas and we wait for the next programme' \
       ' in the mini-drama. Advertising can educate, too. Adverts tell us about ' \
       'new, healthy products. And adverts in magazines give us ideas for how to ' \
       'look prettier, be fashionable and be successful. Without advertising, life ' \
       'is boring and colourless. But some consumers argue that advertising is a bad' \
       ' thing. They say that advertising is bad for children. Adverts make children' \
       ' ‘pester’ their parents buy things for them. Advertisers know we love our ' \
       'children and want to give them everything. So they use children’s ‘pester power’' \
       ' to sell their products. Finally, consumers say, if there is advertising there must' \
       ' be rules. Some adverts advertise unhealthy things like cigarettes and make people waste their money.'

text = text.lower()
def find_s_t(text):
    return text.count('s'), text.count('t')

print(find_s_t(text))

text = text.lower()
text=text.replace('.', '')
text=text.replace(',', '')
text=text.replace('-', '')
text=text.replace('‘', '')
text=text.replace('’', '')

new_text = text.split()
new_list = list(new_text)

for i in range(len(new_list)):
       if new_list[i].find('advert') == 0:
              new_list[i] = new_list[i].upper()

print(' '.join(new_list))