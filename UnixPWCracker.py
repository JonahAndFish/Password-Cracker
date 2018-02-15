import crypt


def testPass(cryptPassword):
    salt = cryptPassword[0:2]
    dictFile = open('dictionary.txt', 'r')
    for word in dictFile.readlines():
        word = word.strip(' \n\t')
        cryptword = crypt.crypt(word,salt)
        if cryptword == cryptPassword:
            print "[+] password found " + cryptword
            return
    print "[-] password not found"
    return

def main():
    passfile = open('password.txt','r')

    for line in passfile.readlines():
        user = line.split(':')[0]
        cryptPassword = line.split(':')[1].strip(' \n\t')
        print "cracking " + user
        testPass(cryptPassword)

if __name__ == "__main__":
    main()
