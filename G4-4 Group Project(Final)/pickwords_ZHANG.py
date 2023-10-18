from wordlist_ZHANG import WordList
import store_ZHANG

file = open('dict_ZHANG.txt', 'r')

lines = [line.lower() for line in file]
with open('dict_ZHANG.txt', 'w') as out:
     out.writelines(sorted(lines))              #uppercase to lower case

select_word = None
def select():
    global word
    theWordList = WordList('dict_ZHANG.txt')
    word = theWordList.pickWord()[0]
    print(word)


def word_checking(final_word_list):
    word_duplicate = list(set(word))
    word_duplicate.sort()
    final_word_list = list(set(final_word_list))
    final_word_list.sort()
    select_word = word_duplicate
    select_word.sort()
    if final_word_list == select_word:
        select_word.clear()
        name = store_ZHANG.a
        score = str(int(store_ZHANG.num))
        new_score = str(int(score) + 1)
        combine1 = '{},{}'.format(name, score)
        combine2 = '{},{}'.format(name, new_score)
        store_ZHANG.changetext(combine1, combine2)
        store_ZHANG.login(name)
        print('Yes')
    else:
        final_word_list.clear()
        print('No')






