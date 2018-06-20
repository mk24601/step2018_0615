
def linksearch(num,t,reachedlist,wiki):
    nextlist = []
    if t  == 7:
        return
    else:
        print("見つかった単語の数 -> " + str(len(reachedlist)))
        print("t -> "+str(t)+", 到達率(網羅率) -> " + str(int(len(reachedlist))/1483277))
        for w in wiki[num]:
            if w not in reachedlist:
                reachedlist.append(w)
                nextlist.append(w)
        for w in nextlist:
            linksearch(w,t+1,reachedlist,wiki)

if __name__ == '__main__':
    wordnum = 0 #0番の単語から探索開始
    flinks = open('links.txt','r')
    wiki = []
    reachedlist = []
    reachedlist.append(int(wordnum))

    for i in range(1483277):
        wiki.append([])
        #print("wiki["+str(i)+"] = "+str(wiki[i]))
    for row in flinks:
        factors = row.split("\t")
        wiki[int(factors[0])].append(int(factors[1]))

    linksearch(int(wordnum),0,reachedlist,wiki)

    print("見つかった単語の数 -> " + str(len(reachedlist)))
    print("到達率(網羅率) -> " + str(int(len(reachedlist))/1483277))
