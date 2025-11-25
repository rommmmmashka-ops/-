def generator(file, *pairs):
    pairs_list = []
    for p in pairs:
        pairs_list.append(p.lower())
    with open(file, 'r', encoding='utf-8') as f:
        for line in f:
            text = line.lower().rstrip('\n')
            counts = {}
            for p in pairs_list:
                counts[p] = 0
                i = 0
                while i < len(text)-1:
                    if text[i:i+2] == p:
                        counts[p] += 1
                    i += 1
                        
            yield counts
           
                    
def main():
    result = generator('text.txt', 'ун', 'но', 'аб')
    for r in result:
        print(r)

if __name__=="__main__":
    main()