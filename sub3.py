#https://www.geeksforgeeks.org/polybius-square-cipher/
# Python Program to implement polybius cipher
# function to display polybius cipher text
#https://ja.wikipedia.org/wiki/ポリュビオスの暗号表

def polybiusCipher(s):
    # convert each character to its encrypted code
    for char in s:

        # finding row of the table
        #ordは文字をunicord値に変換する関数
        row = int((ord(char) - ord('a')) / 5) + 1

        # finding column of the table
        col = ((ord(char) - ord('a')) % 5) + 1

        # if character is 'k'
        if char == 'k':
            row = row - 1
            col = 5 - col + 1

        # if character is greater than 'j'
        elif ord(char) >= ord('j'):
            if col == 1:
                col = 6
                row = row - 1
            col = col - 1

        print(row, col, end='', sep='')

# Driver's Code
if __name__ == "__main__":
    s = "yuito"

    # print the cipher of "geeksforgeeks"
    polybiusCipher(s)
