# -*- coding: cp1252 -*-
def encode(input):
        base64_table = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/="
        equal_flag = False
        bits_to_encode = ""
        encoded = ""
        number_of_equals = 0
        for letter in input:
                letter_in_binary = str(bin(ord(letter)))
                letter_in_binary = letter_in_binary[0]+letter_in_binary[2:]
                if len(letter_in_binary) == 7:
                        letter_in_binary = '0' + letter_in_binary
                bits_to_encode += letter_in_binary
        if (len(bits_to_encode)/8)%3 is not 0:
                number_of_equals+=1
                equal_flag = True
        if ((len(bits_to_encode)/8)+1)%3 is not 0 and equal_flag:
                number_of_equals+=1  
        while bits_to_encode is not None and len(bits_to_encode) >= 6:
                letter_to_add = base64_table[int(bits_to_encode[:6],2)]
                encoded += letter_to_add
                bits_to_encode = bits_to_encode[6:]
        if len(bits_to_encode) < 6 and len(bits_to_encode)>0:
                while len(bits_to_encode) < 6:
                        bits_to_encode+='0'       
                letter_to_add = base64_table[int(bits_to_encode,2)]
                encoded += letter_to_add
        while number_of_equals > 0:
                encoded+='='
                number_of_equals-=1    
        return encoded
def decode(input):
        base64_table = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/="
        bits_to_decode = ""
        decoded = ""
        special_binary_to_append= ""
        has_equals = 0
        save_input = input
        if input[len(input)-1] == '=':
                has_equals +=1
                input = input[:len(input)-1]
        if input[len(input)-1] == '=':
                has_equals+=1
                input = input[:len(input)-1]
        if has_equals > 0:
                special_char = input[len(input)-1]
                index = base64_table.find(special_char)
                special_binary_to_append =str(bin(index))[0]+str(bin(index))[2:]
                while len(special_binary_to_append) < 6:
                        special_binary_to_append = '0' + special_binary_to_append
                while len(special_binary_to_append) > 6:
                        special_binary_to_append = special_binary_to_append[1:]
                special_binary_to_append = special_binary_to_append[:(4/has_equals)]
                input = input[:len(input)-1]
        for letter in input:
                index = base64_table.find(letter)
                binary_to_append =str(bin(index))[0]+str(bin(index))[2:]
                while len(binary_to_append) < 6:
                        binary_to_append = '0' + binary_to_append
                while len(binary_to_append) > 6:
                        binary_to_append = binary_to_append[1:]
                bits_to_decode+=binary_to_append[:6]
        bits_to_decode += special_binary_to_append
        while len(bits_to_decode) >0:
                bits = bits_to_decode[:8]
                char_to_append = chr(int(bits,2))
                decoded+= char_to_append
                bits_to_decode= bits_to_decode[8:]
        return decoded
print decode(encode(""))
